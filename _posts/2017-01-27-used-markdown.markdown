---
layout: post
title:  Markdown 语法整理
date: 2017-01-27
comments: true
external-url:
categories: Template-language
---

Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式,更加便于书写和阅读。

## &sect;&nbsp;标题

   在`Markdown`当中设置标题，有两种方式：

   - 通过在文字下方添加`=`和`-`，他们分别表示一级标题二级标题。

   - 在文字开头加上 `#`，通过`#`数量表示几级标题。

   >共有1~6级标题，1级标题字体最大。

## &sect;&nbsp;块注释（blockquote）

   通过在文字开头添加`>`表示块注释。

>当`>`和文字之间添加五个空格时，块注释的文字会有变化。



## &sect;&nbsp;无序列表

在文字开头添加(\*, +, or -)实现无序列表。但是要注意在(\*, +, and -)和文字之间需要添加空格。

>建议：一个文档中只是用一种无序列表的表示方式

## &sect;&nbsp;有序列表

使用数字后面跟上句号。**记得还要有空格**

## &sect;&nbsp;链接 (Links)

   Markdown中有两种方式，实现链接，分别为内联方式和引用方式。

   - 内联方式：`This is an [example link](http://example.com/).`

   - 引用方式：


   I get 10 times more traffic from [Google][1] than from [Yahoo][2] or [MSN][3].  

   [1]: http://google.com/        "Google" 
   [2]: http://search.yahoo.com/  "Yahoo Search" 
   [3]: http://search.msn.com/    "MSN Search"

~~~
   I get 10 times more traffic from [Google][1] than from [Yahoo][2] or [MSN][3].  

   [1]: http://google.com/        "Google" 
   [2]: http://search.yahoo.com/  "Yahoo Search" 
   [3]: http://search.msn.com/    "MSN Search"
~~~

   - 链接跳转:

~~~
<a href="https://cloudhan.me"  target="_blank">跳到自己博客列表</a>

跳到自己博客列表：<a href="https://cloudhan.me" target="_blank">cloudhan</a>
~~~


## &sect;&nbsp; 图片(Images)

图片的处理方式和链接的处理方式，非常的类似。

   - 内联方式：`![alt text](/path/to/img.jpg "Title")`

   - 引用方式：

```
![alt text][id]

[id]: /path/to/img.jpg "Title"

```
- html的处理方式：

~~~
<img src="/assets/bella.jpg" alt="Het meisje met de parel" width="400px" height="200px" style="margin:0"> 

<div align=center><img width = '150' height ='150' src ="https://tse2-mm.cn.bing.net/th?id=OIP.rF3VYN1CRvtyWBPU0I7kyQDMEy&p=0&pid=1.1"/></div>
~~~

## &sect;&nbsp;代码块（code/pre）

实现方式有两种：
- 简单文字出现一个代码框(code)。使用`<blockquote>`。
>不是单引号而是左上角的ESC下面~中的"`"）

- 大片文字需要实现代码框(pre)，使用Tab和四个空格，或者`~~~`包围代码。


## &sect;&nbsp;脚注(footnote)

~~~
hello[^1]
...

[^1]: 这是一个注解。

~~~

## &sect;&nbsp;下划线

在**空白行**下方添加`---`横线。

>前面讲过在文字下方添加“-”，实现的2级标题


## &sect;&nbsp;注释 

HTML 以 `<!-- , --> `的闭包定义注释（支持跨行），不在正文中显示。Markdown 沿用 HTML Comment 注释格式：

`<!-- This text will not appear in the browser window. --> `


## &sect;&nbsp;关于字体 

*斜体*:将需要设置为斜体的文字两端使用1个`*`或者`_`夹起来

**粗体**:将需要设置为斜体的文字两端使用2个`*`或者`_`夹起来

- 字体颜色：

~~~
浅红色文字：<font color="#dd0000">浅红色文字：</font><br /> 

深红色文字：<font color="#bd4147">深红色文字</font><br /> 

~~~

文字颜色：<font color="#bd4147">当前文本文字</font> 

- 字体大小：
~~~
size为1：<font size="1">size为1</font><br /> 
size为2：<font size="2">size为2</font><br /> 
size为3：<font size="3">size为3</font><br /> 
~~~
size为1：<font size="1">size为1</font><br />
size为2：<font size="2">size为2</font><br /> 
size为3：<font size="3">size为3</font><br /> 

>字体大小为1-7,7号最大，3号为浏览器默认大小。

- 字体背景颜色：

~~~
<table><tr><td bgcolor="#FF00FF">背景色的设置是按照十六进制颜色值：#7FFFD4</td></tr></table>
<table><tr><td bgcolor="#FF83FA">背景色的设置是按照十六进制颜色值：#FF83FA</td></tr></table>
<table><tr><td bgcolor="#D1EEEE">背景色的设置是按照十六进制颜色值：#D1EEEE</td></tr></table>
<table><tr><td bgcolor="#C0FF3E">背景色的设置是按照十六进制颜色值：#C0FF3E</td></tr></table>
~~~

<table>
  <tr>
    <td bgcolor="#C0FF3E">
背景色的设置是按照十六进制颜色值：#C0FF3E
    </td>
  </tr>
</table>

>测试了下，除了表格可以用，其他标签不起作用，不建议使用这个属性。

- 文字居中：

~~~
<center>Hello</center>
~~~

- 文字左对齐：

~~~
<p align="left">Hello</p>
~~~

- 使用常用字体：

~~~
<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
~~~

---

## &sect;&nbsp;表格

~~~
| 左对齐标题 | 右对齐标题 | 居中对齐标题 |
| :------| ------: | :------: |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |
~~~

>注：对齐方式书写要求是`:`要和`-`相邻，与`|` 之间有空格。

页面效果：

| 左对齐标题 | 右对齐标题 | 居中对齐标题 |
| :------| ------: | :------: |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |



---

## &sect;&nbsp;插入音频
 

~~~
<audio id="audio" controls="" preload="none">
  <source id="mp3" src="http://music.163.com/song/media/outer/url?id=562598065.mp3">
</audio>
~~~


---

<audio id="audio" controls="" preload="none">
  <source id="mp3" src="http://music.163.com/song/media/outer/url?id=562598065.mp3">
</audio>


## &sect;&nbsp;插入视频

<!--- 第一种方式：-->

~~~
<iframe 
    width="800" 
    height="450" 
    src="https://v.miaopai.com/iframe?scid=SvyHaHOczsp7B6ftW86oqMMz62-h5ai6~Fwp8A__"
    frameborder="0" 
    allowfullscreen>
</iframe>
~~~

<iframe 
    width="800" 
    height="450" 
    src="https://v.miaopai.com/iframe?scid=SvyHaHOczsp7B6ftW86oqMMz62-h5ai6~Fwp8A__"
    frameborder="0" 
    allowfullscreen>
</iframe>

---

<!--
- 第二种方式，自动播放：

~~~
<iframe width="560" height="315" src="http://tv.sohu.com/upload/static/share/share_play.html#90268916_9365222_0_9001_0" frameborder="0" allowfullscreen></iframe>
~~~

---
- 第三种方式：

~~~
<video id="video" controls="" preload="none" poster="http://om2bks7xs.bkt.clouddn.com/2017-08-26-Markdown-Advance-Video.jpg">
      <source id="mp4" src="http://om2bks7xs.bkt.clouddn.com/2017-08-26-Markdown-Advance-Video.mp4" type="video/mp4">
      </video>
~~~


<video id="video" controls="" preload="none" poster="http://om2bks7xs.bkt.clouddn.com/2017-08-26-Markdown-Advance-Video.jpg">
      <source id="mp4" src="http://om2bks7xs.bkt.clouddn.com/2017-08-26-Markdown-Advance-Video.mp4" type="video/mp4">
      </video>

---
-->

<br>



### <a>参考</a><br>

>1、[Markdown 语法说明](http://wowubuntu.com/markdown/)；

>2、[本文转自互联网360doc](http://www.360doc.com/content/15/0216/11/8790037_448944940.shtml);

>3、[Markdown插入表格语法](https://www.jianshu.com/p/2df05f279331)

