---
layout: post
title: Excel 使用技巧
date: 2018-09-30
comments: true
external-url:
categories: Office 
---


Excel 


## 1、统计不重复项的个数

     =SUMPRODUCT(1/COUNTIF(B2:B81,B2:B81))

>统计合同名称中不重复的单位数量，也就是实际合同总数量,

>SUMPRODUCT参数为一个数组时不做乘积，而是求和。


---

## 2、排名

     = SUMPRODUCT((D2<$D$2:$D$8)*1)+1

或

     = RANK(A2,($A$2:$A$4）


     = RANK(A2,($A$2:$A$4,$C$2:$C$4))

>在（）中用逗号连接多个区域

---
<br>

## 3、实现自动编号，档筛选和隐藏时重新自动编号

    =SUBTOTAL(103,B$2:B2) 


---

<br>

## 4、SUMPRODUCT多条件求和的案例讲解


<div class="cloud-tie-wrapper">
<iframe width="800" 
        height="480"
        src="//player.bilibili.com/player.html?aid=11711196&cid=19346720&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</div>


---

<br>

## 5、高级筛选的条件区域格式

| 范围 | 姓名 | 销售数量 |
| ------: | :------: | ------:|
| >=0.02| 张三 | >1000 |
| <2018-09-30 | 李四| >5000 |

>条件放在不同行是或`OR`的关系，同一行是与`AND`的关系;

<br>

<div class="cloud-tie-wrapper">
<iframe width="800" 
        height="480"
        src="//player.bilibili.com/player.html?aid=11712994&cid=19349313&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</div>

<br>

---

## 6、条件格式的公式应用

※ 实现整行记录标识

公式 =$A1="北京无线电测量研究所"

※ 满足多条件的数据突出显示

公式 = ($B2>=5000)*($C2>=300)

※ 关键词匹配

公式 = FIND ("股份",$A1)

>注意：规则通过管理进行设置，格式要自行定义

>参考：[为什么你的表格数据枯燥无味？原来是不会使用这个功能](https://mp.weixin.qq.com/s?__biz=MzA5NTI5NzUyNw==&mid=2666980346&idx=1&sn=3be2c1df3d6f7a92eb57cafee5f0805d&chksm=8b43c962bc344074bd45ac8f3b983b6d9398e3c538e06027041accc8f25f3086aee7089ec279&scene=0#rd)

---

## 7、如何同时显示日期和星期？

自定义格式:  `yyyy-y-d aaaa` 

---
<br>

## 8、自动生成报表目录并添加超链接

※ step1：`Ctrl + F3`在弹了的窗口中输入名称`getsh`, 在引用位置输入公式：

~~~
引用位置 = MID(GET.WORKBOOK(1),FIND("]",GET.WORKBOOK(1))+1,99)&T(NOW())
~~~

※ step2：在单元格输入公式并下拉即可生成工作表的目录。

~~~
公式 = IFERROR(HYPERLINK("#"&INDEX(getsh,ROW(A2))&"!a1",INDEX(getsh,ROW(A2))),"")
~~~

>注意：这里的名称用的是`getsh`，公式都是在目录页输入的

---
<br>
## 9、数据验证和条件格式结合使用突出显示目标数据

※ step1：在H6设置数据验证列表

※ step2：需要突出显示的数据，设置条件格式 公式 = $A3=$H$6

类似的还可以：

~~~
公式 =A1<>""
公式 =AND($C3="女"，YEAR($D3)>1980)
~~~

>参考：[Excel技巧精选](https://mp.weixin.qq.com/s?__biz=MzA5NTI5NzUyNw==&mid=2666972091&idx=1&sn=a177d23a8d9f23f3ca13e60cae88b177&mpshare=1&scene=1&srcid=1002iFIJEWTOx7xBPLyZuH8g#rd)                                    

---
<br>
## 10、不改变数据源实现二级联动下拉菜单


<div class="cloud-tie-wrapper">
<iframe width="800" 
        height="480"
        src="//player.bilibili.com/player.html?aid=11712829&cid=19348975&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</div>
<br>
提示：

※ 主要公式 = OFFSET(B$1,MATCH(G1,A:A,)-1,,COUNTIF(A:A,G1))

※ 数据-删除重复项

※ 取消合并单元格快速填充： F5 定位 - 选空值 - 输入第一个空单元格的取值公式（例如：=A2）- Ctrl + Enter

※ excel中合并单元格快速拉序号，输入公式 =MAX($A$1:A1)+1


>参考：[百度链接：取消合并单元格实现快速填充](https://jingyan.baidu.com/article/a681b0de7b0c3b3b18434632.html)

>本文内容的 13 合并单元格的取消和每行填充相同内容 提供了另一种解决方案！

---
<br>
## 11、一个关键字查找筛选对应的多行数据 `INDEX+SMALL+IF` 万金油函数

<div class="cloud-tie-wrapper">
<iframe width="800" 
        height="480"
        src="//player.bilibili.com/player.html?aid=8160452&cid=13420534&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</div>
<br>

=INDEX(A:A,SMALL(IF(B$2:B$17=G$1,ROW($2:$17),99),ROW(A1)))

=INDEX(C:C,<font color="#DC143C">SMALL(</font><font color="#6495ED">IF(B$2:B$17=G$1,<font color="#DAA520">ROW($2:$17)</font>,999)</font>,<font color="#DC143C">ROW(A1))</font>)

>[点击下载示例文件，   提取码`6w1q` ](https://pan.baidu.com/s/1ZXNePGwH7nrOhNkD-c--9A)

>扩展：[Excel双向查找的9种方法](https://mp.weixin.qq.com/s?__biz=MjM5NTk5NDk0Mg%3D%3D&idx=5&mid=2651539731&sn=824bf439219d1c03ded7e4d2226bcae1)

---
<br>
## 12、报价表文件，不等行的合并单元格对应数据快速求和

※ step1：选中求和列

※ step2：

= SUM( C2:$C$12 )- SUM( D3:$D$12 )

= SUM(数据首行：$数据尾行) - SUM(求和列次行：$求和列次行)

※ step3：Ctrl + Enter

>NC报价表涉及并发数和单价不适合

>[对不等行的合并单元格对应数据快速求和的函数技巧](https://www.bilibili.com/video/av8753926?from=search&seid=989465679353557003)

---

<br>
## 13、合并单元格的取消和每行填充相同内容

公式 = LOOKUP（"座", $D$3:D3)

>主要为VLOOKUP查找扫清道路，去掉合并单元格

---
<br>
## 14、当数字变 E+ , 一个？让它现原形！

`Ctrl + 1 `设置单元格格式 - 自定义 - 输入数字 `0 `

>如果输入 `0000000` 当0的个数大于整数位，会用0在数字前补齐

还可以输入`？`和`#` 达到同样效果，区别是：

- 当0的个数大于整数位时，会以0补齐位数

- 当？的个数大于整数位时，会以空格补齐位数

- 当#的个数大于整数位时，不补。


**设置** `e/mm/dd`  **日期对齐**

---
<br>
## 15、按单元格颜色求和

※ step1：定义名称，为提取颜色值做准备

公式 - 定义名称 ，在定义名称窗口中输入名称 mycolor（可以自定义），然后在下面引用来源中输入公式：


=GET.CELL(63,Sheet2!B2)&T(NOW())

>公式说明：

>Get.cell(63,单元格) 可以获取单元格填充颜色值

>&T(NOW()) 实现表格在更新时定义名称取值也可以更新

※ step2：获取颜色值

在C列和E列分别输入公式 =mycolor，即可获取B列和D列的单元格填充色。


※ step3：剩下的交给sumif函数吧

=SUMIF(C:C,E2,B:B)

---
<br>
## 16、制作二级联动下拉

※ step1：设置数据源区域。就是把手机名称和型号整理成如下图格式备用，存放的位置随意;

※ step2：批量定义名称。选取手机名称和型号区域后，公式选项卡 - 定义的名称组 - **根据所选内容创建**，选取窗口上的“首行”复选框;

※ step3：设置数据有效性。选取型号列，打开数据有效性窗口，在来源中输入=indirect(D5)


---
<br>
## 17、实现自动到期提醒

要求：离到期日30天内行填充红色，60天内填充黄色。要求可以修改G2:G3的期间，提醒色会自动更新

※ step1、添加到期天数列，计算出离还款还有多少天。

公式 =D2-TODAY()

※ step2、添加辅助表，可以用来动态调整提醒的天数。

15表示15天内，45表示45天内。

※ step3、选取表格（标题行不选），开始 - 条件格式 - 新建规则。然后进行如下设置：

- 类型：使用公式确定要设置格式的单元格

- 设置格式框中输入公式 =$E2<$G$2（按E列到期日判断，所在E前要加$）

- 点格式按钮，设置填充色为红色。

※ step4、按※ step3方法，再添加一个规则。公式为=$E2<$G$3，格式设置为黄色。

※ step5、开始 - 条件格式 - 管理规则，在规则管理窗口中，把30天内规则提升到最上面。

设置完成！



>16-17参考：[Excel表格的精选39个技巧](https://mp.weixin.qq.com/s?__biz=MjM5NDYyNzAzNQ==&mid=2652912144&idx=1&sn=70b9a4c5bd63b39bc3bcf005de563cfb&chksm=bd5076a48a27ffb2b73c90e199f81c437dfa487ce8af72bf9e9da2443e129cf072283214faff&mpshare=1&scene=1&srcid=1004HRwvrMVtPcTKG7CjGG9v#rd)

---
<br>
## 18、Mlookup函数来了

=Mlookup(查找内容，查找区域,返回值所在的列数,第N个)

语法说明：

查找内容：除了单个值外，还可以选取多个单元格，进行多条件查找。

查找区域：同VLOOKUP

返回值的在列数：同VLOOKUP

第N个：值为1就返回第1个符合条件的，值为2就返回第2个符合条件的....当值为0值时，返回最后1个符合条件的值，值为-1时返回所有查找结果并用逗号连接。

举例：

※ 查找第2次电视的进货数量。

=Mlookup(A11,A2:D8,4,2)

※ 查找电视的最后一次入库数量

=Mlookup(A11,A2:D8,4,0)

※ 查找47寸电视的第1次进货数量。

=Mlookup(A11:B11,A2:D8,4,1)

※ 实现筛选功能。

=Mlookup($B$10:$B$11,$A$1:$D$8,4,A14)

※ 实现多结果查找功能。（把所有符合条件结果用逗号连接起来）

=MLOOKUP(A11,B$1:C$8,2,-1)

>18 参考：[Mlookup函数来了](https://mp.weixin.qq.com/s?__biz=MjM5NDYyNzAzNQ==&mid=2652912073&idx=1&sn=deca355c82a286defed9f17bce4f2c05&chksm=bd50757d8a27fc6b8bc512f697d48677bfd6b2f70fe434e0cc7f416f3c5c36794fcc9ea2b457&mpshare=1&scene=1&srcid=1004rjYRGah9meoYlPJyBn5U#rd)

---
<br>
## 19、获取文件路径

文件-信息-打开文档位置


---
<br>
## 20、通过批注添加图片

在制作产品介绍表或员工信息表时，常需要添加产品图片和员工照片，这时用批注插入图片是最好的选择。

选取批注 - 右键“设置批注格式” - **颜色** - 填充效果 - 图片 -选择图片

---

<br>
## 21、利用批注完成快速合并两列文字

先插入一批注，然后复制多列数据，再选取批注按ctrl+v粘贴，然后再复制批注文字粘贴到表格中即可。

>注意：很多同学粘贴批注无效，是因为要点选批注边缘来选取批注，不要让批注进入文字编辑状态。


---
<br>
## 22、每页打印标题行

如果想在打印时每一页都显示标题，页面布局 - 打印标题 - 首端标题行：选取要显示的行

---
<br>
## 23、同时修改多个工作表

按shift或ctrl键选取多个工作表，然后在一个表中输入内容或修改格式，所有选中的表都会同步输入或修改。这样就不必逐个表修改了。

---
<br>
## 24、显示公式部分计算结果

选取公式中的要显示的部分表达式，按`F9`

---
<br>
## 25、选择性粘贴的计算（把所有数据进行计算）

按`Ctrl + Alt + v`  选择性粘贴 

常用的把财务数据转为万元版

※ step1： 在一个单元格输入1000,并且复制这个单元格 Ctrl + C


※ step2：选择数据区域全部数据


※ step3：选择性粘贴，选 `除` 确定即可。


用【万】显示金额数另一种方法：


同样选中更改区域，在字体选项卡下的自定义，输入代码：`0!.0,万`，然后确定即可

※ 显示万的自定义代码：`0!.0,万`

※ 百万元显示金额自定义格式代码为：`0.00,,`


>如果改为 `*1 `的话，可以把文本格式的数字全部变为数值！

---
<br>
## 26、高亮显示选中行列：聚光灯效果

※ step1：条件格式设置公式： =OR(CELL("row")=ROW())

                         =OR(CELL("col")=COLUMN())

                         =(CELL("row")=ROW())+(CELL("col")=COLUMN())

※ step2：VBA 工作表选择 Worksheet SelectionChange 加入代码

~~~

Private Sub Worksheet_SelectionChange(ByVal Target As Range)
ActiveSheet.Calculate
End Sub

~~~

>条件格式设置时，范围要设置整个数据区域;

>文件保存格式为 .xlsm ;

>以上步骤完成之后，聚光灯效果已经实现了，但可能会出现无法将单个或多个单元格复制粘贴数据,解决办法就是:

```
Private Sub Worksheet_SelectionChange(ByVal Target As Range)
On Error Resume Next
If Application.CutCopyMode = xlCopy Or Application.CutCopyMode = xlCut Then Exit Sub
ActiveSheet.Calculate
End Sub
```


纯VBA 实现方式：

~~~

Private Sub Worksheet_SelectionChange(ByVal Target As Range)
With Target
     .Parent.Cells.Interior.ColorIndex = xlNone
     .EntireRow.Interior.Color = RGB(230, 230, 250)
     .EntireColumn.Interior.Color = RGB(250, 235, 215)
End With
End Sub

~~~

>[颜色代码参考](http://tool.oschina.net/commons?type=3)

---
<br>

## 27、对齐的多种方式

※ 缩进对齐

按Ctrl选取区域，点工具栏中的“增加缩进量”可以批量向后缩进对齐

※ 文字竖排

选取表格的文字 -  开始 - 对齐 - 竖排文字

※ 跨列居中

选取标题和后面的空列，设置单元格格式 - 对齐 - 水平对齐 - 跨列居中

※ 姓名对齐

设置单元格格式 - 对齐 - 分散对齐 - 设置合适缩进量

※ 倾斜表头

开始- 对齐 -  逆时针角度

※ 填充对齐

可以重复输入的字符，常用于制作分隔线

※ 两端对齐

当单元格较少(一个格能容下)，两端对齐默认为左对齐样式。如果需要换行，它和自动换行的区别是，两端对齐是每一行文字都会两端顶格显示。

※ 自带页签目录的使用

鼠标放在excel 标签最前面 有两个方向箭头 `Ctrl+鼠标左键` 会调到第一个和最后一个表页，放在第一个箭头 点`右键` 打开工作表目录

---

## 28、切片器快速制作动态图表视频

<div class="cloud-tie-wrapper">
<iframe width="800" 
        height="480"
        src="//player.bilibili.com/player.html?aid=11711273&cid=19346828&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
</div>
<br>

>注意：切片的样式修改，需要先复制。
>[参考：透视表的常见错误](http://excel880.com/blog/archives/870)

---

## 29、隐藏部分数据，便于截图

单元格式，自定义，设置一个格式`;;;` 再截图就可以了。


---

## 30、防止重复录入

选取要防止重复录入的单元格区域，数据 - 有效性 - 自定义 - 公式：

=COUNTIF(A:A,A2)=1

---


## 31、实现间隔行标识 

公式 =(MOD(ROW(),2)=1) 首行有标识

公式 =MOD(ROW(),2)=0 首行无标识

  

公式=mod(row(),2)从内到外的解释：
ROW()为选中的所有列进行操作，返回该列所在的行号；

MOD为求余数，即ROW()返回的行号除以2的余数，这里判断余数是否为0，即选出了所有偶数行。

=mod(row(),3),表示对2列表标颜色

规则：=mod(column(),2),表示给一列标注颜色，标注多列则修改对应数值即可，如果给5列标颜色，将数值修改为6即可，以此类推。

---

## 31、实现间隔行插入空行


※ step1：首先我们在表格末尾，输入序列1、2、3……对需要在其后面插入空格的行标号。在最前面我们输入”序号“一方面后面排序。

※ step2：标号完之后，我们选择他们，然后点击【复制】

※ step3：在最后一个行号后面，选中后粘贴，

※ step4：然后我们头全部选择

※ step5：然后再点击【数据】，然后选择【排序】

※ step6：弹出排序的对话框，然后我们在主要关键词那输入序号，也就是我们编号1上方的名称，在排序依据那选择”数值“，在次序那选择升序，然后再点击【确定】

>[参考百度链接](https://jingyan.baidu.com/article/6525d4b164606eac7d2e94f2.html)

---

## 32、Ctrl+E 拆分数字和文字 

20分钟

50秒

快速拆分数字和单位此功能是Excel 2013后的版本才有哒，超好用。在A列输入需要拆分的数据在B1输入A1里的数字，光标移到B1单元格右下角，变成“+”时双击，填充方式选择为【快速填充】同理，在C1输入A1中的数据单位，光标移到C1单元格右下角，变成“+”时双击，填充方式选择为【快速填充】


从Excel97至现在的最新版本2016，如果评选Excel中最简单、易用、功能最强大的技巧，非2013版新增的"快速填充"（快捷键 Ctrl+E）莫属。向下拖动复制后，打开下拉菜单，就可以看到它的身影【快速填充】


※ 拆分姓名和手机号码

先输入第一个姓名，选取它和下面的空行（也可以只选取下面的第一个空格），按Ctrl+E，一秒搞定拆分（提取手机号码同样方法）

即使手机号码位置不定，也可以提取出来

※ 字符中统一添加特定字符

每个数字后添加 万元，先输入一个带万元的，再按按Ctrl+E,同样一秒完成！

※ 合并姓名和手机号码

想合并在一起呢？先输入一行，再按按Ctrl+E,同样一秒完成！

※ 从身份证号码中提取生日

填充前要把单元格格式设置成文本格式，然后在前2个单元格中输入日期，选C4单元格按Ctrl+E填充。

其实，用分列更方便，不需要设置文本格式，提取出的是日期格式。

※ 高难度的字符串乱序重组

单元格内的文字顺序调整，先输入一行，剩下的按Ctrl+E

※ 提取括号内的字符和数字

※ 手机号码分段显示和加密

※ 提取市区名称

※ 银行账号添加空格

>Ctrl+E很好用，但再次遗憾的告诉大家：只有excel2013和excel2016支持它。

>参考:[你会用 Ctrl + E 吗？](https://mp.weixin.qq.com/s?__biz=MjM5NDYyNzAzNQ==&mid=2652913571&idx=1&sn=21792ce6cdf475a36c96921a123a27ce&chksm=bd5073178a27fa018e7e5a9fe714840f354a0e8da81113ee8919be5d2abee4ee96b0f88111d6&mpshare=1&scene=1&srcid=1010gnQFDMg5m6yoBHIzKAeQ#rd)




---

## 33、剪贴板的调用

开始选项卡 右下角点击打开 剪贴板

多次复制后，可以选择全部粘贴 ，用于多次复制报表，合并粘贴到一起


---


## 34、多表合并

数据透视表向导，可以按Alt+D，然后再按P，切记不能一次性按！

参考：[有多个表格，格式相同，但姓名人数不同，要快速将所有费用汇总](https://mp.weixin.qq.com/s/L4GkHW3bg-5H1xNnHzsYrA)


---

## 35、分段显示手机号码
 
 =TEXE(B2,"000-0000-0000")

---

## 36、excel怎样快速修改全部字体

F5 定位常量 和 数字 再统一修改字体

---


## 37、图表突出显示最大值和最小值

在图表中，我们还可以突出显示最大值和最小值，如下图，我们对表格数据进行整理，建两列辅助列，分别输入公式：

`=IF(B2=MAX($B$2:$B$11),B2,NA())和=IF(B2=MIN($B$2:$B$11),B2,NA())`，下拉填充。插入折线图，选中图形，点击鼠标右键选择“更改系列图表类型”，在组合里把最大值和最小值的图形更改为带数据标记的折线图，分别选中最大值和最小值系列，鼠标右键选择“添加数据标签”和“设置数据标签格式”，勾选“系列名称”。


---


## 38、图表以平均值为界限双色显示

如果我们要根据数据的平均值，把大于平均值和小于平均值的数据用不同颜色的图形来展示，如何做到？ 

这里我们需要对数据进行处理，添加两列辅助列，分别输入公式：

`=IF(B2>AVERAGE($B$2:$B$11),B2,NA())=IF(B2<AVERAGE($B$2:$B$11),B2,NA())`


下拉填充。选中C列和D列数据，插入柱形图。

>[关于图表制作的常用技巧，看这一篇足够了！](https://mp.weixin.qq.com/s?__biz=MzA5NTI5NzUyNw==&mid=2666980487&idx=1&sn=657fe45edca5cf91b69c0a869575892a&chksm=8b43ce1fbc344709a5bff6e60d3868b4be8b310a2b25b4577509dd4ee416a424122603a0b649&mpshare=1&scene=1&srcid=#rd)

---

## 39、选择性粘贴实现行列转换

复制后，`Ctrl+Alt+v`打开选择性粘贴界面里面有 `转置` 选项


---

## 40、公司大事件时间轴 用Excel这么简单！


※ step1：添加辅助列

- C列全部输入0

- D输入正负交替的数字，数字大小要错开

※ step2：插入散点图

选取BC列插入 - 图表 - 散点图

※ step3：添加新系列

在图表上右键 - 选取数据 - 添加 ：X轴选年份B列，Y轴数据选D列

※ step4：添加误差线

选取图表 - 设计 - 添加图表元素 - 误差线 - 基于系列2 - 其他误差选项 ：

- 方向 - 负误差
- 误差量：100%
- 最后选取上面的横线按delete删除。

※ step5：添加文字

选取系列2 - 右键添加数据标签 - 分别选取标志（单独选中状态）逐个在编辑栏=引用B列的文字。（引用后数字变成对应的文字）

※ step6：美化图表

去掉图表上多余的部分（选取Y轴、网格钱按delete删除），对标签和Y轴进行美化

参考原文：[公司大事件时间轴 用Excel这么简单！](https://mp.weixin.qq.com/s?__biz=MjM5NDYyNzAzNQ==&mid=2652913811&idx=1&sn=16ee95118053cc37248c75475da868c1&chksm=bd500c278a278531f2b2234c4dc9d3cb5b2584c448c8844830b23a68fd33f172d2a8893e7525&mpshare=1&scene=1&srcid=1025SEmKrV6QjvgJyDhsZfpc#rd)

---

## 41、所有图片自动编号

按Ctrl+H 打开查找替换窗口，查找：^g，替换为：^&^p^c

代码说明：

^g  代表图片

^& 代表查找的内容

^p 代表换行符（添加的编号在图片下一行显示）

^c 代表剪切版的内容

总结：查找图片，替换为 原来的图片 + 换行符 + 剪切版中的域代码

---

## 42、带复选框的选择求和的例子

如果你下载过老外做的Excel表格或模板，会发现表格中有很多控件。其中，用的最多的是复选框 ☑。
在费用项目前的方框内打勾后：
该行填充色和字体都会变色
该行D列的金额会汇总到总成本内（D7单元格）


制作步骤：

step1： 插入复选框

开发工具 - 插入 - 点击复选框后在表中拖画出来 - 删除复选框旁的文字

step2： 设置复选框链接的单元格

点击 复选框右键菜单中的设置控件格式，在弹出的窗口中输入单元格链接 B3
用同样的方法，分别在4~6行插入复选框，并分别链接B4、B5、B6单元格。当点击复选框后，在对应的B
列会输入TRUE,去掉勾选则输入FALSE。

step3： 设置选中行变色

选中B:D列数据 - 条件格式 - 新建规则，在弹出的【新建格式规则】窗口中进行如下设置：

公式框中输入公式 `=$B3=TRUE` （注意$不可少）

点格式按钮，设置填充和字体颜色,本步设置完成后， B列方框画勾的行颜色发生了改变

step4： 隐藏B列的TRUE和FALSE

选取B3： B6 - 设置单元格格式  - 数字 - 自定义  - 在右侧代码框中输入 ;;; (3个分号)

step5： 设置总成本计算公式

在D7单元格中设置公式: `=SUMPRODUCT(B3:B6*D3:D6)`
完工！

原文参考：[口 内打 √，外企大公司都这么用.......](https://mp.weixin.qq.com/s?
__biz=MjM5NDYyNzAzNQ==&mid=2652913951&idx=1&sn=f99f7fccc5ccd7c9f8e01c5a0c85ad7c&chksm=bd50
0dab8a2784bd1e32d526866106a9be8d472b9c6900b23a74123befccd02aad9dae0e4ea2&mpshare=1&scene=1
&srcid=#rd)

---

## 43、Excel数据有效性

6个经典实例，带你重新认识Excel数据有效性

数据有效性（也叫数据验证）是我们使用频率最多的一个功能，比如下拉菜单的制作、限制性输入等，那你真的会用数据有效性吗？本期帮主通过6个经典案例与大家分享一下数据有效性的用法。

※ 下拉菜单的制作

下拉菜单是数据有效性最经典的用法，这里与大家分享一下相关的制作方法。

一级下拉菜单的制作：

选择区域，点击数据——数据验证——设置——验证条件——序列，之后选择来源区域即可。

注意：来源若是手动输入，要注意的是文本之间的分隔符是英文状态下的逗号。

二级下拉菜单的制作：

先选中区域，点击公式——定义名称——根据所选内容创建——勾选首行，之后建立一级菜单和二级菜单，做二级菜单时，来源写公式=INDIRECT(单元格地址)。

※ 在指定的区域输入数字

选中区域，打开验证对话框，在允许条件中选择整数，之后根据需要输入相应的区间。

※ 只允许输入数字

这时选择的条件是自定义，之后输入公式=ISNUMBER(B1)=TRUE。

※ 逐行输入内容

一样是选择自定义，在公式中输入=COUNTA(A$1:A13)=ROW(A1)

※ 输入唯一值

同理，选择自定义输入公式=COUNTIF(A:A,A1)=1

※ 输入当前时间

选中区域，之后按Ctrl+1打开设置单元格格式，然后选择自定义，输入数字格式H:MM:SS，点击确定。
这里需要在其他任意单元格输入公式=NOW()

完成以上操作之后，直接选中区域，打开数据验证，选择序列，来源设置=刚刚输入的公式的单元格。


>[参考原文：6个经典实例，带你重新认识Excel数据有效性](https://mp.weixin.qq.com/s?__biz=MzA5NTI5NzUyNw==&mid=2666980786&idx=1&sn=d1d6492757e5e74a73b52535fce2e304&chksm=8b43cf2abc34463c1b9ef200636f8b4f79638496db5d519d178c9161a104918d8201d2571bbd&mpshare=1&scene=1&srcid=1107GyG9QC8mjoy2a9OBqyfC#rd)

---