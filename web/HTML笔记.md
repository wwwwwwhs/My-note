#              HTML

思途管理系统121.42.236.205

## 1.常用标签

搜索引擎格式


html ： 决定了网页的内容

css:  决定了网页表现|样式

javascript: 决定了网页的行为(与用户的交互效果)



####  1.1目前需要掌握的几个html标签

##### 有语义的标签

| 标签名      | 作用                                 | 使用时的注意事项                                             |
| ----------- | ------------------------------------ | :----------------------------------------------------------- |
| h (h1 – h6) | 表示的是网页中的标题                 | 一个网页最多出现一次h1                                       |
| p           | 表示的是网页中的段落                 | 不常用                                                       |
| img         | 在网页中显示图片                     | 这个标签一定要给src属性和alt属性img总是默认按图片原始的宽高进行显示！ |
| a           | 超链接，可以当前网页中激活另一个网页 | a标签，一定要给href属性值，指明要打开的目标页面是哪个        |
| ol          | 有序列表                             | ul和ol的儿子只能是li, 反之li的父亲只能是ul或ol               |
| ul          | 无序列表                             | ul里只能放li标签，不能放其他标签                             |
| li          |                                      |                                                              |
| dl          | 自定义列表                           | 只能包含dt或dd                                               |
| dt          | 自定义列表表头                       | dd 包含于dl中                                                |

#### ctrl+回车 强制换行

##### br  不要经常用  常用在段落里 换行常用p标签 包在里面

##### 没有语义标档签

##### div  大块 用来布局，一行只能放一个div,大盒子

##### span 小块 一行可以有多个span标签 小盒子


### 1.2 文字

| 语义   |            标签            |
| ------ | :------------------------: |
| 加粗   | <strong></strong>或<b></b> |
| 倾斜   |     <em></em>或<i></i>     |
| 删除线 |    <del></del>或<s></s>    |
| 下划线 |    <ins></ins>或<u></u>    |

### 1.3 div和span标签

div和span是没有语义的，他们就是一个盒子，用来装内容的。 


```html
<div class="box">
		</div>
<div class="clear"> <!--清除浮动 -->
			</div>
```

```css
.box {
	width: 200px;
	height: 200px;
	background-color: red;
	float: left;//向左向右浮动水平排列，默认垂直排列
    margin: auto;/*水平居中*/
}
.clear {
	clear: both; /*清除浮动*/
}
```

### 1.4 图像标签

图像标签的其他属性

| 属性   | 属性值   | 说明                               |
| ------ | -------- | ---------------------------------- |
| src    | 图片路径 | 必须属性                           |
| alt    | 文本     | 替换文本，图像不能显示的文字       |
| title  | 文本     | 提示文本，鼠标放到图像上显示的文字 |
| width  | 像素     | 设置图像的宽度                     |
| height | 像素     | 设置图像的高度                     |
| border | 像素     | 设置图像的边框组纽                 |

原图像只设置宽度，不设高度，它就会等比例缩放

### 1.5 超链接标签

连接里面不能再套连接

绝对路径 跳转外部文件

```html
<a href="跳转目标" target="目标窗口的弹出方式">文本或图像</a>
<a href="xxx.html/css" target=""></a>内部链接
herf="#"空连接
herf="xxx.zip/exe"下载链接
<a href="http://www.baidu.com"><img src="x.jpg" /></a>网页链接
相对路径 跳转本地文件  不加./ 浏览器会自动补全
当前目录查找 ： ./
<a herf="./2-标签.html">标签</a>
查找上一级目录
<a href="../index.html">返回上一个页面</a>
```

| 属性   | 作用                                                         |
| ------ | ------------------------------------------------------------ |
| href   | 用于指定链接的url地址（必须属性）具有超链接功能              |
| target | 用于指定链接的打开方式，其中_self为默认值，_blank为在新窗口中打开方式 |

![1606828447685](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1606828447685.png)

### 1.6 表格标签

```js
表格
<table border="1px"  width="800px" bordercolor="skyblue" cellpadding="20px" cellspacing=0>
			<thead>
				<tr>
					<th>#</th>
					<th>书名</th>
					<th>作者</th>
					<th>价格</th>
					<th>数量</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>1</td>
					<td>西游记</td>
					<td>吴承恩</td>
					<td>40</td>
					<td>2</td>
				</tr>
			</tbody>
		</table>
```

#### 1.合并单元格

```js
<td colspan="2">Data1</td> //跨2列合并
<td rowspan="2">Data1</td> //跨2行合并
```


<thead>标签，表格的头部区域 <tbody>标签，表格的主体区域，

可以更好的分清表格的结构

<th>表头单元格，加粗并且居中

name相同，同一个组里面的radio可以实现互斥

提交：name=value

#### 2.嵌套页面：用得不多

```js
<p>
			<iframe src="http://www.baidu.com" width="100%" height="400px" frameborder="0"></iframe>
		</p>
		<p>
			<iframe src="index.html" width="100%" height="400px" frameborder="0"></iframe>
		</p>
```



### 1.7 特殊字符

普通的空格在html中如果连续出现多个会被当成一个空格

如果想显示多个连续的空格就要使用特殊的字符

在HTML 中，某些字符是预留的。在 HTNL 中不能使用小于号(<）和大于号(>)，这是因为浏览器会误认为它们是标签。如果希望正确地显示预留字符，必须在 HTML 源代码中使用字符实体(character entities）。实体名称对大小写敏感!字符实体类似这样:

```html
&lt;等同于<;less than
&gt;等同于>;greater than
&nbsp;等同于空格
```

![1606828934958](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1606828934958.png)

### 1.8 表单域

```html
<form action="">//form用于定义表单域 ，它会把它范围内的表单元素提交给服务器
			<p>
				<label>账户：</label>
				<!--内联元素 -->
				<input type="text">
			</p>
			<p>
				<label>手机：</label>
				<input type="text">
			</p>
			<p>
				<label>密码：</label>
				<input type="password">
			</p>
			<p>
				<label>性别：</label>
				<label>
					<input type="radio" name="sex" id="" value="" checked />男
				</label>
				<label>
					<input type="radio" name="sex" id="" value="" />女
				</label>
			</p>
			<p>
				<label for="">爱好：</label>
				<lable>
					<input type="checkbox" name="" id="" value="" checked />摄影
				</lable>
				<lable>
					<input type="checkbox" name="" id="" value="" />绘画
				</lable>
				<lable>
					<input type="checkbox" name="" id="" value="" />唱歌
				</lable>
				<lable>
					<input type="checkbox" name="" id="" value="" />旅行
				</lable>
			</p>
			<p>
				<label for="">学历：</label>
				<select name="" id="">
					<option value="">高中</option>
					<option value="">大专</option>
					<option value="">本科</option>
					<option value="">研究生</option>
					<option value="">博士</option>
				</select>
			</p>
			<p>
				<label for="">简介：</label>
				<textarea name="" id="" cols="30" rows="10"></textarea>
				<!-- <textarea rows="" cols="">
						
					</textarea> -->
				<!-- 不要带空行 会有空格产生 -->
			</p>
			<p>
				<!-- 按钮写法1 -->
				<input type="button" name="" id="" value="确定" />
				<!-- 按钮写法2 更灵活 里面可以放文字图片等-->
				<button type="button">取消</button>
				<!-- 提交按钮  自动触发form的提交行为-->
				<button type="submit">提交</button>
				<!-- 重置按钮 将表单还原为初始值 -->
				<button type="reset">重置按钮</button>
				<!-- 如果不写type 默认为submit按钮 -->
			</p>
		</form>
```



#### 1.8.1 表单标签

##### 1.input输入表单元素



##### 忘记密码的时候打开f12 将password改为text就可以看了

##### placeholder 属性提供可描述输入字段预期值的提示信息（hint）。

```js
 <input type="text" placeholder="请输入快递单号" class="jd">
```

该提示会在输入字段为空时显示，并会在字段获得焦点时消失。

**注释：**placeholder 属性适用于以下的 <input> 类型：text, search, url, telephone, email 以及 password。

##### 2.文件域：上传文件使用的

```html
<input type="file">
```



##### label是内联元素  包住单选按钮时 点字就可以选中

#### 1.8.2.select下拉表单元素

select至少包含一对option ，在里面定义selected时，即为默认选中项

```html
<select name="" id="">
					<option value="">高中</option>
					<option value="">大专</option>
					<option value="">本科</option>
					<option value="">研究生</option>
					<option value="">博士</option>
				</select>
```

#### 1.8.3.textarea文本域元素：用于定义多行文本输入的控制（留言板，评论）

```html
<textarea row="3" cols="20"></textarea>
```

cols="每行中的字符数"，rows="显示的行数"，我们在实际开发中不会使用，都是用css来改变大小

```html
<!-- <textarea rows="" cols="">
						
					</textarea> -->
				<!-- 不要带空行 会有空格产生 -->
```




可放大或缩小