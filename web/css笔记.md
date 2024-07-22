# css

Cascading Style Sheets

# 1.选择器分类

##### 选择器分为**基础选择器**和**复合选择器**

1.基础选择器由单个选择器组成的

2.基础选择器又包括:**标签选择器,类选择器,id选择器和通配符选择器**
#### 标签名选择器
h1{

}

#### 类选择器
.class{

}
####  id选择器
\#id{

}

####  通配符选择器

\*{

}
#### 属性选择器
ul\[class]{

}
#### 子字符串选择器
li\[class^="box-"]{

}
#### [伪类选择器](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Selectors/Pseudo-classes_and_pseudo-elements#%E4%BC%AA%E7%B1%BB)
| 选择器                                                                                          | 描述                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`:active`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:active)                        | 在用户激活（例如点击）元素的时候匹配。                                                                                                                                                                      |
| [`:any-link`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:any-link)                    | 匹配一个链接的`:link`和`:visited`状态。                                                                                                                                                             |
| [`:blank`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:blank)                          | 匹配空输入值的[`<input>`元素](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input)。                                                                                                   |
| [`:checked`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:checked)                      | 匹配处于选中状态的单选或者复选框。                                                                                                                                                                        |
| [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/:current "此页面目前仅提供英文版本")       | 匹配正在展示的元素，或者其上级元素。                                                                                                                                                                       |
| [`:default`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:default)                      | 匹配一组相似的元素中默认的一个或者更多的 UI 元素。                                                                                                                                                              |
| [`:dir`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:dir)                              | 基于其方向性（HTML[`dir`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes/dir)属性或者 CSS[`direction`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/direction)属性的值）匹配一个元素。 |
| [`:disabled`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:disabled)                    | 匹配处于关闭状态的用户界面元素                                                                                                                                                                          |
| [`:empty`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:empty)                          | 匹配除了可能存在的空格外，没有子元素的元素。                                                                                                                                                                   |
| [`:enabled`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:enabled)                      | 匹配处于开启状态的用户界面元素。                                                                                                                                                                         |
| [`:first`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:first)                          | 匹配[分页媒体](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_paged_media)的第一页。                                                                                                          |
| [`:first-child`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:first-child)              | 匹配兄弟元素中的第一个元素。                                                                                                                                                                           |
| [`:first-of-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:first-of-type)          | 匹配兄弟元素中第一个某种类型的元素。                                                                                                                                                                       |
| [`:focus`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:focus)                          | 当一个元素有焦点的时候匹配。                                                                                                                                                                           |
| [`:focus-visible`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:focus-visible)          | 当元素有焦点，且焦点对用户可见的时候匹配。                                                                                                                                                                    |
| [`:focus-within`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:focus-within)            | 匹配有焦点的元素，以及子代元素有焦点的元素。                                                                                                                                                                   |
| [`:future`](https://developer.mozilla.org/en-US/docs/Web/CSS/:future "此页面目前仅提供英文版本")         | 匹配当前元素之后的元素。                                                                                                                                                                             |
| [`:hover`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:hover)                          | 当用户悬浮到一个元素之上的时候匹配。                                                                                                                                                                       |
| [`:indeterminate`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:indeterminate)          | 匹配未定态值的 UI 元素，通常为[复选框](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/checkbox)。                                                                                        |
| [`:in-range`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:in-range)                    | 用一个区间匹配元素，当值处于区间之内时匹配。                                                                                                                                                                   |
| [`:invalid`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:invalid)                      | 匹配诸如`<input>`的位于不可用状态的元素。                                                                                                                                                                |
| [`:lang`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:lang)                            | 基于语言（HTML[lang](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes/lang)属性的值）匹配元素。                                                                                      |
| [`:last-child`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:last-child)                | 匹配兄弟元素中最末的那个元素。                                                                                                                                                                          |
| [`:last-of-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:last-of-type)            | 匹配兄弟元素中最后一个某种类型的元素。                                                                                                                                                                      |
| [`:left`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:left)                            | 在[分页媒体](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_paged_media)中，匹配左手边的页。                                                                                                      |
| [`:link`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:link)                            | 匹配未曾访问的链接。                                                                                                                                                                               |
| [`:local-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/:local-link "此页面目前仅提供英文版本") | 匹配指向和当前文档同一网站页面的链接。                                                                                                                                                                      |
| [`:is()`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:is)                              | 匹配传入的选择器列表中的任何选择器。                                                                                                                                                                       |
| [`:not`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:not)                              | 匹配作为值传入自身的选择器未匹配的物件。                                                                                                                                                                     |
| [`:nth-child`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-child)                  | 匹配一列兄弟元素中的元素——兄弟元素按照_an+b_形式的式子进行匹配（比如 2n+1 匹配元素 1、3、5、7 等。即所有的奇数个）。                                                                                                                     |
| [`:nth-of-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-of-type)              | 匹配某种类型的一列兄弟元素（比如，`<p>`元素）——兄弟元素按照_an+b_形式的式子进行匹配（比如 2n+1 匹配元素 1、3、5、7 等。即所有的奇数个）。                                                                                                        |
| [`:nth-last-child`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-last-child)        | 匹配一列兄弟元素，从后往前倒数。兄弟元素按照_an+b_形式的式子进行匹配（比如 2n+1 匹配按照顺序来的最后一个元素，然后往前两个，再往前两个，诸如此类。从后往前数的所有奇数个）。                                                                                             |
| [`:nth-last-of-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-last-of-type)    | 匹配某种类型的一列兄弟元素（比如，`<p>`元素），从后往前倒数。兄弟元素按照_an+b_形式的式子进行匹配（比如 2n+1 匹配按照顺序来的最后一个元素，然后往前两个，再往前两个，诸如此类。从后往前数的所有奇数个）。                                                                            |
| [`:only-child`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:only-child)                | 匹配没有兄弟元素的元素。                                                                                                                                                                             |
| [`:only-of-type`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:only-of-type)            | 匹配兄弟元素中某类型仅有的元素。                                                                                                                                                                         |
| [`:optional`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:optional)                    | 匹配不是必填的 form 元素。                                                                                                                                                                         |
| [`:out-of-range`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:out-of-range)            | 按区间匹配元素，当值不在区间内的时候匹配。                                                                                                                                                                    |
| [`:past`](https://developer.mozilla.org/en-US/docs/Web/CSS/:past "此页面目前仅提供英文版本")             | 匹配当前元素之前的元素。                                                                                                                                                                             |
| [`:placeholder-shown`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:placeholder-shown)  | 匹配显示占位文字的 input 元素。                                                                                                                                                                      |
| [`:playing`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:playing)                      | 匹配代表音频、视频或者相似的能“播放”或者“暂停”的资源的，且正在“播放”的元素。                                                                                                                                                |
| [`:paused`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:paused)                        | 匹配代表音频、视频或者相似的能“播放”或者“暂停”的资源的，且正在“暂停”的元素。                                                                                                                                                |
| [`:read-only`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:read-only)                  | 匹配用户不可更改的元素。                                                                                                                                                                             |
| [`:read-write`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:read-write)                | 匹配用户可更改的元素。                                                                                                                                                                              |
| [`:required`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:required)                    | 匹配必填的 form 元素。                                                                                                                                                                           |
| [`:right`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:right)                          | 在[分页媒体](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_paged_media)中，匹配右手边的页。                                                                                                      |
| [`:root`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:root)                            | 匹配文档的根元素。                                                                                                                                                                                |
| [`:scope`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:scope)                          | 匹配任何为参考点元素的元素。                                                                                                                                                                           |
| [`:valid`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:valid)                          | 匹配诸如`<input>`元素的处于可用状态的元素。                                                                                                                                                               |
| [`:target`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:target)                        | 匹配当前 URL 目标的元素（例如如果它有一个匹配当前[URL 分段](https://en.wikipedia.org/wiki/Fragment_identifier)的元素）。                                                                                              |
| [`:visited`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:visited)                      | 匹配已访问链接。                                                                                                                                                                                 |

#### [伪元素](https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Building_blocks/Selectors/Pseudo-classes_and_pseudo-elements#%E4%BC%AA%E5%85%83%E7%B4%A0)

| 选择器                                                                                     | 描述                         |
| --------------------------------------------------------------------------------------- | -------------------------- |
| [`::after`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::after)                   | 匹配出现在原有元素的实际内容之后的一个可样式化元素。 |
| [`::before`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::before)                 | 匹配出现在原有元素的实际内容之前的一个可样式化元素。 |
| [`::first-letter`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::first-letter)     | 匹配元素的第一个字母。                |
| [`::first-line`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::first-line)         | 匹配包含此伪元素的元素的第一行。           |
| [`::grammar-error`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::grammar-error)   | 匹配文档中包含了浏览器标记的语法错误的那部分。    |
| [`::selection`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::selection)           | 匹配文档中被选择的那部分。              |
| [`::spelling-error`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/::spelling-error) | 匹配文档中包含了浏览器标记的拼写错误的那部分     |
|                                                                                         |                            |

### 关系选择器

#### 后代选择器

ul li{

}

#### 子代关系选择器
ul > li{

}

#### 邻接兄弟选择器

img + p{

}

#### 通用兄弟
img ~ a{

}

# 层叠层
有三种[层叠来源类型](https://developer.mozilla.org/zh-CN/docs/Web/CSS/Cascade#origin_types)：用户代理样式表、用户样式表和作者样式表。
优先级由低到高
1. 用户代理普通样式
2. 用户普通样式
3. 作者普通样式
4. 正在动画的样式
5. 作者重要样式
6. 用户重要样式
7. 用户代理重要样式
8. 正在过渡的样式
### 2.display有三个取值：

(1),block 块级元素：独占一行; 在没有设置宽度的情况下，水平方向占满父元素（流体特性）; 设置宽width或高height有效;

##### 常见标签： div、h、p、ul、ol、li等

(2),inline 行级元素（内联）（字体修饰/表单）：非独占一行; 在没有设置宽度的情况下，水平方向紧紧的包住自己的内容（包裹性）; 设置宽width或高height无效;

##### 常见标签:  a、span、strong、b、em、i、del、s、ins、u

![1607081080844](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607081080844.png)

![1607081560279](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607081560279.png)

(3),inline-block 行级元素（内联块级/行块）：非独占一行; 在没有设置宽度的情况下，水平方向紧紧的包住自己的内容（包裹性）; 设置宽width或高height有效;

![1607347507464](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607347507464.png)

##### 常见标签：表单、img、input、td、

border盒子的边框： 略

padding盒子的内填充(内边距)： 盒子的内容content与盒子的边框border之间的距离我们叫内边距padding!

margin盒子的外填充(外边距): 盒子的边框与其相临盒子或其父盒子的边框之间的距离(两个值：上下，左右。三个值：上，左右，下。四个值：上，右，下，左)

margin；块级元素水平居中。行内元素或者行内块元素水平居中给其父元素添加text-align:center;即可

四个盒子三个缝每个设置margin-ringht,最后一个盒子不需要边距会挤下来，所以给最后一个盒子单独设置一个类，并且设置右边距为0，若还没有上来，就看权重的问题。

#### box-sizing决定了盒子的盒模型，有两个取值：

标准盒模型content-box: 这是默认值     盒子的width =content

IE盒模型（怪异盒模型）border-box:	 盒子的width = border + padding + content

总结： box-sizing的取值直接决定了盒子width的分配方案

总结注意：行级元素默认是放在一行的基线（baseline）上的，不是底线！

#### 以后使用display将块级变行级，一定要记得设置font-size:0;来清除水平和垂直之间的缝隙！

#### 设置padding时；会挤出来，就要在设置border盒模型才能对齐

#如果盒子没有指定width/height属性，则此时padding不会撑开盒子大小

```css
padding: 15px 0;
	box-sizing: border-box;
```

盒模型

![1606897557129](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1606897557129.png)

*{ padding: 0; margin: 0; }/*清空默认样式*/
ul { list-style: none; } //除去ul的小圆点
a { text-decoration: none; }/*去掉下划线*/

##### 行高=盒子的高度可以使文字垂直居中

![1607347057502](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607347057502.png)

注上内边距：设置padding

### 3.css字体属性

```css
font-family:"字体"；字体样式
font-size:20px;字体大小/px表示像素/(标题标签需要单独指定文字大小)
font-weight: boid/700;字体加粗
h2 {
    font-weight:400/normal;
}
font-style:normal/italic斜体;字体样式
font复合属性写法
font: font-style font-weight font-size/line-height font-family;
font: italic 700 16px 'Microsoft yahei';
必须保留font-size和font-family属性，否则不起作用
```

bootstrap

### 4.css文本属性

##### 1.alt+鼠标左键 可以打开拾色器

##### 2. text-align:center; 文本，图片等内联元素水平居中对齐

##### 3.line-height: 20px; 行间距

##### 4.text-decoration: underline/none line-throng; 装饰文本，有/无下划线 删除线

##### 5.text-indent: 12px/em(1em=一个文字的大小像素); 段落的首行缩进

##### 6.在input标签里  border: 0;   /* //去掉显示的input边框 */

#####             outline: none;  /* //去掉点击时input边框 */

##### 7.vertical-align:middle/top/bottom设置内联元素的垂直居中

![1607053839465](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607053839465.png)

![1607061015555](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607061015555.png)

### 5.Emmet语法

#### 5.1 快速生成HTML结构语法

.demo$*5

div{我是谁}*5

HB中ctrl+k 格式化文件，vscode中shift+alt+f格式化文件

### 6.css的复合选择器

##### 一.复合选择器有两个或多个基础选择器通过不同的方式组合而成

##### 二.常用的复合选择器有：后代选择器，子选择器，并集选择器，伪类选择器...

#### 6.1 后代选择器

不加点，用空格隔开

```css
ul li {
    color:pink;
}
ul li a {}
```

元素2/3可以是儿子或孙子,元素1/2可以是任意基础选择器

#### 6.2子选择器

![1607070396560](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607070396560.png)

#### 6.3并集选择器

用英文逗号隔开，表示和的意思，通常用于集体声明

```css
p,a {
    color:pink;
}
```

#### 6.4伪类选择器

![1607072119812](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607072119812.png)

![1607072166558](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607072166558.png)

链接伪类按顺序写：lvha

:hover 任何标签都可以使用

![1607072420210](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607072420210.png)

```css
a:hover {
    color: red;
}
```

#### 伪类选择器中实际开发的写法

![1607072714395](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607072714395.png)

##### :first-child  选择器匹配任意元素的第一个子元素（IE>7）

##### :last-child  选择器匹配任意元素的最后一个子元素（IE>9)

#### 6.4.2 伪元素：多用于清除浮动

::before  content:''; 必要属性  在每个元素之前插入内容

::after content:''; 必要属性  在每个元素之后插入内容 可以插字符或者图片

### 6.5:focus 伪类选择器

用于选取获得焦点的表单元素

焦点就是光环，一般情况<input>类表单元素才能获取，因此这个选择器也主要针对表单元素来说

### 7.背景图片

```css
<div>
background-img: url(img/XX.jpg);
</div>
```

#### 7.1.背景平铺

平铺，不平铺，沿x轴平铺，沿y轴平铺

```css
 background-repeat: repeat|no-repeat|repeat-x|repeat-y;
```

背景图片方位：与顺序无关(可以混合，但一定是x,y)

```css
background-position: left center;/*方位名词*/
```

![1608616985358](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1608616985358.png)

![1607092892744](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607092892744.png)

#### 7.2背景图像固定

滚动或固定

```css
background-attachment:scroll | fixed
```

```css
background: url(../img/huiyuan（1）.jpg) no-repeat center center;
```

![1607336386488](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607336386488.png)

![1608619243342](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1608619243342.png)

```css
body {
    background: url('./images/xianxian.jpg');
    background-attachment: fixed;
}//固定在body里，不随着滚动条而滚动
```



### 8.定位

定位=定位模式+边偏移

定位通过 上下左右四个属性设置的

2.边偏移

![1608349517842](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1608349517842.png)

#### 8.1.相对定位：relative

参照物：自己本应该出现的位置。

元素自身相对于当前位置发生的偏移；原来在标准流的位置继续占有，后面的元素任然以标准流的方式对待它，不脱标，继续保留原来的位置 

#### 占有位置

#### 8.2.固定定位：fixed

参照物：浏览器可视窗口为参照点移动元素

做广告，页面的导航菜单，漂浮广告，返回顶部时使用；不会随浏览器滚动条滚动而被卷起的元素都应该用固定定位。

固定定位也是脱标的，其固定定位也可以看作是一个特殊的绝对定位 不占位置

##### 定位的时候不要用margin

#### 8.3绝对定位:absolute

参照物：离它最近的，opsition值为relative\fixed\absolute之一的祖先元素；如果没找到这样的祖先元素，则绝对定位的参照物是"整个页面文档的左上角"（不是html和body）{平时能不用就不用}

##### 父元素或祖先元素必须定位 否则以整个浏览器为参照物，绝对定位不再占有原先的位置（脱标）

#### 不占有位置

8.4粘性定位

```css
选择器{position:sticky;top:10px;}
```

特点：

1.以浏览器的可视窗口为参照点移动元素（固定定位特点）

2.粘性定位占有原先的位置（相对定位特点）

2.设置方位属性才有效  兼容性较差，IE不支持

注：消除div和图片的缝，在包图片的div中设置：font-size:0;

### ！子绝父相：子级用绝对定位，父级要用相对定位 （大多数情况下）

##### #完全作为一个后代的参照物时祖先/父元素用relative,违反常规定位时选择绝对定位自己用absolute

```css
.nav {
	font-size: 0;消除图片和div之间的缝
	position: relative;
}
.nav ul {
	position: absolute;
	top: 0;
	left: 0;
}
```
### 8.4 给盒子使用相同的定位 就会出现盒子重叠的情况，这时要使用z-index来控制定位的叠放次序(z轴)

#### 语法：选择器{z-index:1;}

1.数值可以是正整数，负整数或0，默认是auto,数值越大，盒子越靠上

2.如果属性值相同，则按照后来者居上

3.数字后面不能加单位

4.只有定位的盒子才有z-index属性

### 8.5 定位的拓展

1. #### 用定位算法使盒子居中

```js
.father {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 200px;
            height: 200px;
            background-color: orchid;
            margin-left: -100px;
            /* //  用定位算法使盒子居中 */
            margin-top: -100px;
        }
```

![1608865991706](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1608865991706.png)

#### 2.绝对定位和固定定位也和浮动类似

行内元素添加绝对或者固定定位，可以直接设置宽高

块级元素添加绝对或者固定的定位，如果不给宽高，默认大小是内容的大

浮动元素，绝对定位（固定定位）元素都不会触发外边距合并的问题

#### 3.绝对定位(固定定位)会完全压住盒子

浮动元素不同，只会压住他下面的标准流盒子，但是不会压住下面标准流盒子里面的文字（图片），但是绝对定位（固定定位）会压住标准流所有的内容

浮动之所以不会压住文字，因为浮动产生的最初的目的是为了做文字环绕效果的，文字会围绕浮动元素

![1607322694867](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607322694867.png)

设置弹性高度的优点，不会随着总高度的改变而改变

```css
.nav li {
	height: 10%;
}
```

行级元素的属性：中线对齐

```css
vertical-align: middle;/*仅对行级元素有效*/
```

```css
.nav ul {
	position: absolute;
	top: 0;
	left: 0;
	width: 250px;
	height: 100%;
	padding: 15px 0;
	box-sizing: border-box;
	background-color: rgba(0,0,0,0.3);
	
}
.nav li {
	height: 10%;
	padding: 0 20px;
	cursor: pointer;/*指针变为手*/
}
```

#### text-align: left/right/center;只对行级元素有效

```css
body {
    font:12px/1.5 //表示字体大小/行高是当前字体大小的1.5倍
}
```

### css的三大特性：层叠性，继承性和优先级

#### 1.层叠样式遵循就近原则：离代码近的生效

#### 重置样式表必须放在第一位

#### 2.继承性：凡是文字修饰的 都可以继承 color,font-family,font-size,line-height

##### ,list-style,text-align,font-weight,text-indent

#### 3.优先级

![1607338152609](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607338152609.png)

#### 256进制

![1607338647147](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607338647147.png)

![1607339434171](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607339434171.png)

```css
border-style:dotted;点线边框
```

![1607340886346](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607340886346.png)

```css
border-collapes:collapse;//表示相邻边框合并在一起
```

#### 9.圆角边框

```css
border-radius:20px; 设置高度为一半就可以变为圆（正方形写50%也可以）可以跟2,3,4个数值
```

![1607351005993](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607351005993.png)

#### 10.盒子阴影

```css
  box-shadow: 10px 10px 10px 10px rgba(0, 0, 0, 0.3);
```

![1607351889407](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607351889407.png)

文字阴影

![1607352255923](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607352255923.png)

### 11.浮动

![1607353554796](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607353554796.png)

![1606889191947](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1606889191947.png)

![1607397633962](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607397633962.png)

![1607398558156](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607398558156.png)



![1607398797637](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607398797637.png)

![1607399067050](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607399067050.png)

##### 给浮动元素父级添加 class='clearfix'

```js
.clearfix::after{
				content: '';
				display: block;
				clear: both;
			}
```



代表：百度 淘宝 网易

![1607399237417](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607399237417.png)

父元素调用类名   "class=clearfix"    代表：小米 腾讯

#### 清除浮动需要注意的点

##### 1.浮动和清除浮动成对出现,

##### 2.清除浮动一般放在最靠近浮动元素的尾部，清除浮动只对同级元素有效。

##### 3.检查是否正确清除浮动，看父级元素的高度，如果高度==0，浮动没清除



## 12 元素的显示与隐藏

### 12.1 display属性

display属性用于设置一个元素应如何显示

##### ●display:none;隐藏对象(第一种隐藏方式)

●display:block;除了转换为块级元素之外，同时还有现实元素的意思

display隐藏元素后，不在占有原来的位置

```js
例子：给图片加遮罩 要使用定位 隐藏元素 鼠标滑过在显示元素
```



### 12.2 visibility可见性

##### visibility:visible;元素可视

##### visibility:hidden;元素隐藏（第二种隐藏方式）

visibility隐藏元素后，继续占有原来的位置

如果隐藏元素想要原来的位置，就用visibility:hidden

如果隐藏元素不想要原来位置，就用display:none(用处更多 重点)

### 12.3 overflow

| 属性值  | 描述                                       |
| ------- | ------------------------------------------ |
| visible | 不剪切内容也不添加滚动条                   |
| hidden  | 不显示超过对象尺寸的内容，超过的部分隐藏掉 |
| scroll  | 不管超出内容否，总是显示滚动条             |
| auto    | 超出自动显示滚动条，不超出不显示滚动条     |

一般情况下，我们都不想让溢出的内容显示出来，因为溢出的部分会影响布局

但是如果有定位的盒子，请慎用overflow:hidden因为它会隐藏多余的部分

类似网站广告，当我们点击关闭就不见了，但是我们重新刷新页面，会重新出现

本质：让一个元素在页面中隐藏或者显示出来

### 12.4 opacity(第三种隐藏方式)

```css
opacity: 0.7; /* 设置透明度隐藏取值范围为[0,1],会将里面所有元素都透明 设置0时可以隐藏元素 */
```
## 13.居中的方式

#### 1.水平居中：

##### 内联元素：text-aligen:center;

##### 块级元素：margin:0 auto;

#### 2.垂直居中:

##### 内联元素：vertical-aligen:middle;

##### 块级元素：绝对定位 margin负距（整体居中）前提是宽高固定

#### 3.上下左右居中

1.尺寸不固定

用padding 

2.尺寸固定

```js
(1).father {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 200px;
            height: 200px;
            background-color: orchid;
            margin-left: -100px;
            /* //  用定位算法使盒子居中 */
            margin-top: -100px;
        }
```

(2)

![1608865991706](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1608865991706.png)