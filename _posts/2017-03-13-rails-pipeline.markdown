---
layout: post 
title: Assets Pipeline 
date: 2017-03-13
comments: true
external-url:
categories: Rails
---


Assets Pipeline 的功能主要由两个重要的组件提供：Sprockets 以及 Tilt。Sprockets 用来从你的 assets 路径中打包压缩你所有的 assets 后组合成一个文件，然后放到你目的地路径(public/assets)，而 Tilt 主要是一个样板引擎，用来让 Sprockets 可以去解析像是 SCSS、CoffeeScript 或是 ERB 等各种样板。
  
Apppiple通常都是在 app/views/layouts/application.html 的视图中去包含`css` 或者`js` 文件，在生产环境中一般使用的语句为：

```erb
     <%= stylesheet_link_tag    "application", :media => "all" %>
     <%= javascript_include_tag "application" %>
```
较为完整的语句为：
halm：
```halm
    = stylesheet_link_tag 'application', media: 'all', data: {turbolinks_track: true}
    = javascript_include_tag 'application', data: {turbolinks_track: true}
```
erb：
```erb
      <%= stylesheet_link_tag "application", media: "all", "data-turbolinks-track" => true %>
      <%= javascript_include_tag "application", "data-turbolinks-track" => true %>
```
你会在 html 原始码中看见有包含 `application.js` 和 `application.css` 的文件对应的位置在 app/assets/javascripts/application.js 和 app/assets/stylesheets/application.css；assets是合并文件后的抽象路径。
>所谓合并文件就是app、lib和vendor 目录 assets文件夹下所有css文件合并成一个application.css文件，js同理。
 


###  Basic Usage

 1、 `require_self` 表示包含本文件内的程序代码

  &#167; app/assets/stylesheets/application.css

```
   /*
    *= require_self
    */
   .link {
     color: #FF0000;
   }
```
2、 `require` 其他文件 (免扩展名)

&#167; app/assets/stylesheets/application.css

```
   /*
    *= require ./link
    *= require_self
    */
```
>`./`代表当前目录

&#167; app/assets/stylesheets/link.css

```
   .link {
     color: ##FF0000;
   }
```
3、`require` 目录内的文件

&#167;app/assets/stylesheets/application.css

```
   /*
    *= require ./util/link
    *= require_self
    */
```
&#167;app/assets/stylesheets/util/link.css

```
   .link {
     color: ##FF0000;
   }
```
或用 `require_tree`

&#167;app/assets/stylesheets/application.css

```
   /*
    *= require_tree ./util
    *= require_self
    */
```
&#167;app/assets/stylesheets/util/link.css

```
   .link {
     color: ##FF0000;
   }
```
  > 一般不建议用 `require_tree .` ，但可以用 `require_tree ./xxx`  


4、放置图片

   图片文件通常是放在 app/assets/images/ 下，举例说明下：假设有张图放在`app/assets/images/foo/icon.png`

- view 下读取

```
   <%= image_tag "foo/icon.png" %>   => <img src="/assets/foo/icon.png" />
   <%= image_path "foo/icon.png" %>  => /assets/foo/icon.png
```
- css 读取

```
   background: url("<%= image_path("foo/icon.png")%>");
```

- js 读取

```
   alert("<%= image_path("foo/icon.png")%>");
```

5、 加深理解
例如，这些文件：

```
   app/assets/javascripts/home.js
   lib/assets/javascripts/moovinator.js
   vendor/assets/javascripts/slider.js
   vendor/assets/somepackage/phonebox.js
```
可这样引用：

```
   //= require home
   //= require moovinator
   //= require slider
   //= require phonebox
```
子目录中的资源也能够被访问到:`app/assets/javascripts/sub/something.js`

可以如此的引用：` //= require sub/something`

可以通过 控制台 命令来查看搜索路径:
```
rails c

2.3.3:001> Rails.application.config.assets.paths

``` 

<hr>

### 参考：
1、[http://gogojimmy.net/2012/07/03/understand-assets-pipline/](http://gogojimmy.net/2012/07/03/understand-assets-pipline/)
>原文中有些错误，`require_tree .` 只会搜索`app/assets/`当前目录，不会去搜索lib和vendor。
 通常有`= require link`,appline 会在app、lib和vendor 去搜索link.css，找不到再去gems中和
public下搜索;js 同理。

2、[https://github.com/sstephenson/sprockets](https://github.com/sstephenson/sprockets)



