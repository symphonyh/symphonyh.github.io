#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# Font Awesome 图标字体子集化脚本
#
# 为什么需要：站点的 fa-solid-900.woff2 / fa-brands-400.woff2 是子集，不是全量。
# 全量 solid 约 156 KB，子集只保留全站实际用到的十几个字形，约 2–3 KB。
# 代价是：新增一个 fa-xxx 图标时，若该字形不在子集里，浏览器会显示成缺字方块。
#
# 用法：
#   python _tools/subset-fonts.py --check
#       只体检：列出源码里用到但子集里缺失的图标，不写任何文件。
#   python _tools/subset-fonts.py <全量字体路径> [--brands] [--extra fa-x,fa-y]
#       用全量字体重新生成子集并覆盖 assets/vendor/fontawesome/webfonts/ 下的对应文件。
#
# 依赖：pip install fonttools brotli
#
# 全量字体来源（cdnjs 国内可达，jsdelivr 常常 000）：
#   https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/webfonts/fa-solid-900.woff2
#   https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/webfonts/fa-brands-400.woff2
#
# 注意：务必用与 assets/vendor/fontawesome/css/all.min.css 同版本的全量字体，
#       否则 codepoint 对不上，图标会错位。
# ---------------------------------------------------------------------------
import argparse
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(ROOT, 'assets/vendor/fontawesome/css/all.min.css')
WEBFONTS = os.path.join(ROOT, 'assets/vendor/fontawesome/webfonts')
SOLID = os.path.join(WEBFONTS, 'fa-solid-900.woff2')
BRANDS = os.path.join(WEBFONTS, 'fa-brands-400.woff2')

# 扫描源码的范围：模板、样式、页面、数据文件（_data/social.yml 里的图标名要算进来）
SCAN_DIRS = ['_includes', '_layouts', '_sass', 'assets/css', '_data']
SCAN_ROOT_EXT = ('.md', '.html')

# 非图标名的 fa-* 类：字体族名、文件名、尺寸/修饰类
NOT_ICONS = {
    'fa-solid', 'fa-brands', 'fa-regular', 'fa-light', 'fa-thin', 'fa-duotone',
    'fa-solid-900', 'fa-brands-400', 'fa-regular-400',
    'fa-fw', 'fa-ul', 'fa-li', 'fa-border', 'fa-pull-left', 'fa-pull-right',
    'fa-spin', 'fa-pulse', 'fa-rotate-90', 'fa-rotate-180', 'fa-rotate-270',
    'fa-flip-horizontal', 'fa-flip-vertical', 'fa-flip-both',
    'fa-stack', 'fa-stack-1x', 'fa-stack-2x', 'fa-inverse',
}
NOT_ICONS |= {f'fa-{n}x' for n in range(1, 11)}  # fa-1x … fa-10x

# 无论源码是否扫描到都强制保留的图标（防止动态拼接的类名漏掉）
ALWAYS = ['fa-feather', 'fa-envelope', 'fa-github', 'fa-book-open']


def load_css_map():
    """从 all.min.css 解析 图标名 -> codepoint。别名会指向同一个 codepoint。

    CSS 里别名是并列选择器的形式，例如
        .fa-rotate-left:before,.fa-undo-alt:before{content:"\f2ea"}
    只抓第一个会漏掉后面所有别名，所以按 { ... } 块反查前面的整串选择器。
    """
    css = open(CSS, encoding='utf-8').read()
    result = {}
    for m in re.finditer(r'([^{}]*?)\{content:"\\([0-9a-f]{4})"', css):
        cp = int(m.group(2), 16)
        for name in re.findall(r'\.fa-([a-z0-9-]+):before', m.group(1)):
            result['fa-' + name] = cp  # 键名统一带 fa- 前缀，与源码扫描到的类名对得上
    return result


def scan_source():
    """扫描源码，返回 {图标名: 出现次数}。"""
    hits = {}
    files = []
    for d in SCAN_DIRS:
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p):
            continue
        for dirpath, _dirs, names in os.walk(p):
            files += [os.path.join(dirpath, n) for n in names
                      if n.endswith(('.html', '.md', '.yml', '.yaml', '.scss', '.sass', '.css', '.js'))]
    for n in os.listdir(ROOT):
        if n.endswith(SCAN_ROOT_EXT):
            files.append(os.path.join(ROOT, n))

    for f in files:
        try:
            text = open(f, encoding='utf-8', errors='ignore').read()
        except OSError:
            continue
        for name in re.findall(r'\bfa-[a-z0-9-]+\b', text):
            if name in NOT_ICONS:
                continue
            hits[name] = hits.get(name, 0) + 1
    return hits


def current_codepoints(path):
    """读现有子集里已有的 codepoint 集合。"""
    from fontTools.ttLib import TTFont
    if not os.path.exists(path):
        return set()
    return set(TTFont(path).getBestCmap().keys())


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument('source', nargs='?', help='全量字体（.woff2 / .ttf / .otf）路径')
    ap.add_argument('--brands', action='store_true', help='这次子集化的是 brands 字体')
    ap.add_argument('--check', action='store_true', help='只体检，不写文件')
    ap.add_argument('--extra', default='', help='额外强制保留的图标名，逗号分隔')
    args = ap.parse_args()

    target = BRANDS if args.brands else SOLID
    css_map = load_css_map()
    used = scan_source()

    unknown = sorted(n for n in used if n not in css_map)
    if unknown:
        print('⚠ 源码里出现、但 all.min.css 里查不到的类名（忽略）：', ', '.join(unknown))

    wanted = {n: c for n, c in used.items() if n in css_map}
    for extra in ALWAYS + [e.strip() for e in args.extra.split(',') if e.strip()]:
        if extra in css_map:
            wanted.setdefault(extra, 0)

    # 品牌图标（github 等）在 fa-brands 里，实心图标在 fa-solid 里，分属两个文件。
    # 不区分的话，检查 solid 时会永远把 github 报成缺失。
    brands_cps = current_codepoints(BRANDS)
    brands_names = {n for n, cp in css_map.items() if cp in brands_cps}
    if args.brands:
        wanted = {n: c for n, c in wanted.items() if n in brands_names}
    else:
        wanted = {n: c for n, c in wanted.items() if n not in brands_names}

    have = current_codepoints(target)
    missing = sorted(n for n in wanted if wanted[n] >= 0 and css_map[n] not in have)

    print(f'编辑器目标文件：{os.path.basename(target)}')
    print(f'源码扫描到图标：{len(wanted)} 个 → ' + ', '.join(sorted(wanted)))
    print(f'当前子集字形数：{len(have)}')
    print(f'缺失字形：{len(missing)} 个' + ((' → ' + ', '.join(missing)) if missing else '（无）'))

    if args.check:
        if missing:
            print('\n结论：有缺失，浏览器会显示成方块。重新生成：')
            print('  python _tools/subset-fonts.py <全量字体路径>' + (' --brands' if args.brands else ''))
        else:
            print('\n结论：全部覆盖，无需处理。')
        return 0

    if not args.source:
        print('\n✗ 未指定全量字体路径。加 --check 可只体检。')
        return 2

    unicodes = sorted({css_map[n] for n in wanted} | have)
    spec = ','.join(f'U+{cp:04X}' for cp in unicodes)
    tmp_out = target + '.new'

    cmd = [
        sys.executable, '-m', 'fontTools.subset', args.source,
        f'--output-file={tmp_out}',
        '--flavor=woff2',
        f'--unicodes={spec}',
        '--layout-features=*',
        '--no-hinting',
        '--desubroutinize',
        '--drop-tables+=DSIG',
    ]
    print('\n执行子集化 …')
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print('✗ 失败\n', r.stdout[-800:], r.stderr[-800:])
        return 1

    from fontTools.ttLib import TTFont
    got = set(TTFont(tmp_out).getBestCmap().keys())
    lost = [n for n in wanted if css_map[n] not in got]
    if lost:
        print('✗ 子集缺少预期字形：', ', '.join(lost))
        os.remove(tmp_out)
        return 1

    shutil.copy2(target, target + '.bak')
    shutil.move(tmp_out, target)
    print(f'✓ 已覆盖 {os.path.basename(target)}')
    print(f'  字形 {len(got)} 个，{os.path.getsize(target)} B（旧文件备份为 .bak）')
    print('  验证：git diff --stat assets/vendor/fontawesome/webfonts/')
    return 0


if __name__ == '__main__':
    sys.exit(main())
