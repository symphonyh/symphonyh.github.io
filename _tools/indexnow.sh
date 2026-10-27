#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# IndexNow 提交脚本 —— 让 Bing / Yandex / Seznam / Naver 立即抓取本站页面
#
# 为什么放在 _tools/ ：Jekyll 不发布任何以下划线开头的目录，
# 所以这个脚本不会出现在 _site 里被公开下载。
#
# 用法：
#   bash _tools/indexnow.sh                  # 从 sitemap 读全站 URL 全量提交
#   bash _tools/indexnow.sh --dry-run        # 只生成请求体，不真的发
#   bash _tools/indexnow.sh <url> [<url>...] # 只提交指定页面（改完文章后最常用）
#
# 依赖：bash + curl。不需要 jq / python。
#
# 关于 key：<key>.txt 必须放在站点根、内容与文件名一致，IndexNow 会去校验
#           https://www.cloudhan.me/9ef0b0093692b23781f60102fe409aca.txt
#           换 key = 换文件名 + 改下面这行，然后重新提交一次。
# ---------------------------------------------------------------------------
set -euo pipefail

SITE="${INDEXNOW_SITE:-https://www.cloudhan.me}"
HOST="${INDEXNOW_HOST:-www.cloudhan.me}"
KEY="${INDEXNOW_KEY:-9ef0b0093692b23781f60102fe409aca}"
ENDPOINT="${INDEXNOW_ENDPOINT:-https://api.indexnow.org/indexnow}"

DRY_RUN=0
URLS=()

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    -h|--help) sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    http://*|https://*) URLS+=("$arg") ;;
    *) echo "未知参数：$arg（只接受 URL 或 --dry-run）" >&2; exit 2 ;;
  esac
done

# 没给 URL 就从 sitemap 全量取。sitemap 里已经是百分号编码的纯 ASCII，
# 所以下面的 JSON 拼接不需要转义 —— 但还是拦一下引号和反斜杠，避免手输 URL 破坏 JSON。
if [ "${#URLS[@]}" -eq 0 ]; then
  echo "→ 未指定 URL，从 $SITE/sitemap.xml 读取全站清单"
  mapfile -t URLS < <(
    curl -sS --max-time 30 "$SITE/sitemap.xml" \
      | grep -o '<loc>[^<]*</loc>' \
      | sed 's/<[^>]*>//g'
  )
fi

if [ "${#URLS[@]}" -eq 0 ]; then
  echo "✗ 一条 URL 都没有，sitemap 抓取失败？" >&2
  exit 1
fi

for u in "${URLS[@]}"; do
  case "$u" in
    *\"*|*\\*) echo "✗ URL 含引号或反斜杠，会破坏 JSON：$u" >&2; exit 2 ;;
  esac
done

# 请求体放变量里、走 stdin 喂给 curl，不落临时文件（也就没有清理失败的隐患）。
PAYLOAD="$({
  printf '{"host":"%s","key":"%s","keyLocation":"%s/%s.txt","urlList":[' \
    "$HOST" "$KEY" "$SITE" "$KEY"
  first=1
  for u in "${URLS[@]}"; do
    if [ "$first" -eq 1 ]; then first=0; else printf ','; fi
    printf '"%s"' "$u"
  done
  printf ']}'
})"

echo "  待提交 ${#URLS[@]} 条，请求体 $(printf '%s' "$PAYLOAD" | wc -c | tr -d ' ') 字节"

if [ "$DRY_RUN" -eq 1 ]; then
  echo "→ --dry-run：不发送。请求体前 300 字节："
  printf '%s' "$PAYLOAD" | head -c 300; echo " ..."
  exit 0
fi

echo "→ POST $ENDPOINT"
CODE="$(printf '%s' "$PAYLOAD" | curl -sS -X POST "$ENDPOINT" \
  -H 'Content-Type: application/json; charset=utf-8' \
  --data-binary @- \
  -o /dev/null -w '%{http_code}' --max-time 60 || echo 000)"

case "$CODE" in
  200) echo "✓ 200 已接受，搜索引擎会自行安排抓取" ;;
  202) echo "✓ 202 已接收，key 校验排队中（首次提交 key 时常见，无需处理）" ;;
  400) echo "✗ 400 请求格式错误" >&2; exit 1 ;;
  403) echo "✗ 403 key 校验失败 —— 检查 $SITE/$KEY.txt 是否 200 且内容与文件名一致" >&2; exit 1 ;;
  422) echo "✗ 422 URL 与 host/key 不匹配 —— 检查 host 与 URL 的域名是否一致" >&2; exit 1 ;;
  429) echo "✗ 429 提交过于频繁，隔天再试" >&2; exit 1 ;;
  000) echo "✗ 连不上 IndexNow 接口（网络问题），稍后重试" >&2; exit 1 ;;
  *)   echo "✗ 未知返回码 $CODE" >&2; exit 1 ;;
esac
