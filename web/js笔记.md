# js笔记

## 一.javascript 基础

### 1.1.js的组成

![1607427675816](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607427675816.png)

### 1.2.js的写法

##### 1.行内式js

```js
 <input type="button" value="我是谁" onclick="alert('你猜')">
```

可以将少量代码写在HTML标签的属性中如：onclick

js中推荐使用单引号

##### 2.内嵌式

```js
 <script>
        alert('hi~');
    </script>
```

##### 3.外部js   :适用于代码量较大的时候

```js
<script src="my.js"></script> 在body里面引入
```

### 1.3.js的基本

```js
 // 这是一个输入框

​    prompt('请输入年龄');

​    // alert弹出警示框，输出的，给用户展示的

​    alert('计算的结果是');

​    // console 控制台输出，给程序员测试用的

​    console.log('程序员能看到的')
```

```js
%f占位符  后面的值会占%f的位置
%s占位符
console.log('输入的值：%s',num);//%s是占位符
在alert里没有用
```



## 2.js的变量

### 2.1变量

变量是程序在内存中申请的一块用来储存数据的空间

变量的使用步骤（变量的初始化）：1.声明变量 2.赋值（var是js的关键字，variable变量的缩写，声明后，计算机会自动分配空间，不用管）

```js
var age;//声明一个叫做age的变量
```

```js
var myname = prompt('请输入一个名字');
    alert(myname);
```

```js
var myname = '嘻嘻',
      address = 'kaka村',
      age = 30;  声明多个变量用逗号隔开
```

### 2.2 声明变量特殊情况

|           情况            |          说明          |   结果    |
| :-----------------------: | :--------------------: | :-------: |
| var age;console.log(age); |     只声明 不赋值      | undefined |
|     console.log(age);     | 不声明 不赋值 直接使用 |   报错    |
|  age=10;console.log(age)  |     不声明 只赋值      |    10     |

### 2.3 变量的命名规范

●由字母(A-Za-z)、数字(O-9)、下划线(_)、美元符号($ )组成，如: usrAge,num01,_name

●严格区分大小写。var app;和var App;是两个变量

●不能以数字开头。18age是错误的

●不能是关键字、保留字。例如: var、for、while

●变量名必须有意义。MMD BBDnl→age

●遵守驼峰命名法。首字母小写，后面单词的首字母需要大写。myFirstName

## 3.数据类型

#### 3.1数据类型

1.js的变量只有在程序在运行过程中，根据等号右边的值来确定

2.js是动态语言 变量的数据类型是可以变化的

### 3.2 简单数据类型

| 简单数据类型 | 说明                                               |  默认值   |
| :----------: | -------------------------------------------------- | :-------: |
|    Number    | 数字型，包含整型值和浮点型值，如21,0.21            |     0     |
|   Boolean    | 布尔值类型，如true                                 |     0     |
|    String    | 字符串类型，如"张三" 注意咱们js里面,字符串都带引号 |   false   |
|  Undefined   | var a;声明了变量a但是没有给值，此时a=undefined     | undefined |
|     Null     | var a=null;声明了变量a为空值                       |   null    |

##### js中的最大值和最小值

alert(Number.MAX_VALUE);//1.7976931348623157e+308

alert(Number.MAX_VALUE);//5e-324

数字类型的范围：最大值，最小值，非数字

alert(Infinity);无穷大

alert(-Infinity);无穷小

alert(NaN);非数值

#### 3.2.1 数字型

##### 1.isNaN()

用来判断一个变量是否为非数字的类型，是返回ture,不是返回false

#### 3.2.2 字符串型 ：用单引号或者双引号括起来的都是字符串型。嵌套规则，外单内双或外双内单

##### 1.字符串转义符

![1607439842807](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607439842807.png)

##### 2.检测获取字符串的长度 length

```js
var a = 'sach a big surprise'
console.log(a.length);
```

##### 3.字符串的拼接：数值相加，字符相连

```js
console.log('沙漠' + '骆驼');//输出 沙漠骆驼
console.log(12 + 12);//输出24
```

##### 4.练习

```js
1.var age;
    age = prompt('请输入一个年龄');
    alert('您今年' + age + '岁啦');
 2.var age = prompt('请输入一个年龄');
    var str = '您今年' + age + '岁啦'
    alert(str);
```

##### 5.布尔型 Boolean

true值为1,false值为0

```js
console.log(true + 1); //2
    console.log(false + 1); //1
```

6.undefined

```js
  var str = undefined;
    console.log(str + 1);//输出NaN
```

##### 7.typeof:检测变量类型 简单的数据类型，instanceof 复杂数据类型的判断

```js
var num = 'mi mi';
    console.log(typeof num);
```

#### 3.3数据类型转换

![1609293528769](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1609293528769.png)

##### 1.数字型转换为字符串型

![1607497462643](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607497462643.png)

![1607503083976](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607503083976.png)

##### 2.字符串型转换为数字型

 (1)parseInt(变量):将string类型转成整数数值型 会取整

```js
var age = prompt('请输入您的年龄');
 console.log(parseInt(age));
 console.log(parseInt('120px'));//120
```

（2）parseFloat(string)：将string类型转成浮点数数值型

```js
 console.log(parseFloat('120px'));//120
```

(3)Number()强制转换 为数字型 可以进行浮点数的运算

```js
var str = '123'
        console.log(Number(str));//变成数字型
```

##### (4)隐式转换(+ 不能隐式转换)（其他都可以）

```js
 console.log('12' - 0);
    console.log('123' - '120');

 var year = prompt('请输入您的出生年份');
    var age = 2020 - year;
    alert('您的年龄是' + age + '岁啦');
```

```js
  <script type="text/javascript">
        function jiecheng() {
            var n = parseInt(document.getElementById('number').value);
            var res = document.getElementById('result');
            var sub = 1;
            var i;
            for (i = n; i >= 1; i--) {
                sub = sub * i;


            } console.log(sub);
            res.value = sub;

        }

    </script>
</head>

<body>
    <div class="center">
        <input type="text" id="number"><br>
        <input type="button" value="阶乘" onclick="jiecheng()"><br>
        <input type="text" id="result">
    </div>
</body>
```

(5).转化为布尔型

![1607520562991](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607520562991.png)

上面的值会自动判断为false

#### 3.4标识符，关键字，保留字

标识符不能是关键字和保留字

![1607520886828](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607520886828.png)

![1607520900401](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607520900401.png)

## 4.运算符

```js
++age类似于age=age+1; 先加1后返回值
age++ //age=age+1;先返回原值后自加1；
console.log(age++ + 10);//20
```

![1607522985596](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607522985596.png)

![1607523379460](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607523379460.png)

![1607523411009](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607523411009.png)

![1607523490444](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607523490444.png)

![1607523982178](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607523982178.png)

![1607524211215](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607524211215.png)

#### 2.三元表达式：条件表达式 ？表达式1：表达式2

##### 如果条件表达式结果为真，则返回表达式1的值，如果结果表达式为假，则返回2的值。

```js
var num = 10;
    var result = num < 5 ? '是的' : '不是的';
    console.log(result);//不是的
```

## 5. 流程控制：标准流，分支流，循环流

### 1 switch分支流

```js
switch(表达式){
    case value1:
        执行语句;
        break;
    case value2:
        执行语句;
        break;
    default:
        执行最后语句;
}
//实例：
    switch(inp.value){
					case '诗仙':
					console.log('李白');
					break;
					case '诗圣':
					console.log('杜甫');
					break;
					default:
					alert('查无此人！');
				}    	
```



##### 注：固定值选择switch,常用语判断大于或小于某个范围用else if.

##### switch效率会更高一些，分支较少，用else if效率高一些

### 5.2 循环流

#### 5.2.2 for循环

```js
for(初始化变量;条件表达式;操作表达式){
    //循环体;
}

var result = '';
			var num = 0;
			for (var i = 1; i < 1024; i++) {
				if (i % 7 == 0) {//能被7整除的数
					// console.log(i);
					num++; //每次有符合条件的一个数时，sum就加一，就可以统计有多少个可以符合条件的数
					result = result + i + ' '; //可以在一行内显示

				}
			}
			console.log(num);
			console.log(result);
		</script>
```

#### 5.2.3双重for循环

外层循环一次，里层循环全部；

#### 5.2.4 while循环

```js
while(条件表达式){
    循环体
}
//实例：
 var num = 1;
    while (num <= 100) {
        console.log('你好');
        num++;
    }

```

#### 5.2 do while循环

```js
do {
    循环体；
}while(条件表达式)//先执行代码，在判断条件
    //实例：
     var i = 1;
    do {
        console.log('你好吗');
        i++;
    } while (i <= 10)
```



#### 5.3continue关键字

跳出本次循环，继续下一次循环。

```js
for (var i = 7; i <= 30; i++) {
				/* if (i % 11 != 0) {
					console.log(i);
				} */
				if(i%11==0){
					continue;
				}
				else{
					console.log(i);
				}
			}
```



#### 5.3.1 break 退出整个循环

```js
for(var i=34;i<=125;i++){
				if(i%23==0){
					console.log('第一个被23整除的数字是：%f',i)
					break;
				}
			}
```



#### 5.4断点调试

source->点要调试的行数->刷新->开始调试->右边栏w,点+输入变量

![1607571720627](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607571720627.png)

![1607571939565](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607571939565.png)

## 6.数组

#### 6.1一组数据的集合，数组中一个变量可以存多个值

数组可以把一组数据的集合存放在一个变量中

#### 6.2创建数组的两种方式

1.new关键字

```js
var arr = new Array();
```

2.数组字面量

```js
var arr = [];//任何类型都可以
```

#### 6.3数组的索引

#####  用来访问（获取）数组元素的序号；注：数字（索引）下标从0开始的    数组名[索引]

```js
var arr1 = [5, 6, 'pink', true];
    console.log(arr1);//输出所有元素
    console.log(arr1[3]);//输出其中一个元素
```

```css
//对象数组
			var team=[
				{name:'黄磊',age:48},
				{name:'黄渤',age:42},
				{name:'张艺兴',age:28},
			]
```

#### 6.4 数组的遍历

##### 数组的长度=数组名.length

```js
 var arr1 = [2, 6, 1, 7, 4];
    var sum = 0;
    var ave = 0;
    for (var i = 0; i < arr1.length; i++) {
        sum = sum + arr1[i];
    } ave = sum / arr1.length;
    console.log(sum);
    console.log(ave);//i是计数器，当索引号使用 arr1[i]是数组的元素
```

#### 6.5数组中新增元素

1.通过修改length长度新增数组元素（length属性是可读的）

```js
 var arr1 = ['red', 'green', 'blue', 'pink'];
    console.log(arr1.length);
    arr1.length = 5;
    console.log(arr1);
    console.log(arr1[4]);

```

2.新增数组元素，修改索引号，增加数组元素

```js
  var arr1 = ['red', 'green', 'blue', 'pink'];
    arr1[4] = 'tian';//追加数组元素
    console.log(arr1);
    arr1[0] = 'yellow';//替换数组元素
    console.log(arr1);
```

3.向数组中追加元素

```js
var arr = [];
    for (var i = 0; i < 10; i++) {
        arr[i] = i + 1;
    }
    console.log(arr);
```

#### 6.6冒泡排序

重复走访要排列的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来

```js
 var arr = [2, 5, 3, 8, 9, 4, 6]
    for (var i = 0; i < arr.length - 1; i++) {
        for (var j = 0; j < arr.length - i - 1; j++) {//4,3,2,1 数组索引从0开始 找规律
            if (arr[j] > arr[j + 1]) {
                var temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    } console.log(arr);
```

## 7.函数

#### 7.1.函数就是封装了一段可以被重复执行调用的代码块(封装：把一个或多个功能通过函数的方式封装起来，对外只提供一个简单的函数接口)

目的：就是让大量代码重复使用

#### 7.2.函数的使用

（1.）声明函数（2）调用函数:函数不调用，自己不执行

```js
1.function 函数名（）{
    函数体；
}               //函数名一般是动词,例： "sayhi"
函数名（）;
 function sayhi() {
        console.log('hi~');
    }
    sayhi();

```

2.函数声明的第二种表达方式：匿名函数表达式

```js

var fun = function () {
        console.log('pink');
    }
    fun();//函数的另一种声明方式，变量里存的是函数，函数表达式也可以传递参数

 var fun = function (str) {
        console.log('pink');
        console.log(str);
    }
    fun('red');
```

#### 7.3形参和实参：可以有0-无限个

参数的作用：在函数内部，某些值不能固定，可以通过参数在调用函数时传递不同的值进去

形参：函数在声明时的变量，用来接收实参

实参：函数调用时传递的参数，实际参数，传递给形参

![1607668637684](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607668637684.png)

![1607669376082](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607669376082.png)

#### 7.4 函数返回值 return

1.函数只是实现某种功能，最终的结果需要返回给函数的调用者函数名（）通过return实现的

2.只要函数遇到return就把后面的结果返回给函数的调用者 函数名=return后面的结果

##### 3.返回函数时return 函数名;不加括号，调用的时候才加括号

![1609395750113](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1609395750113.png)

```js
function 函数名（）{
    return 需要返回的结果;
}

 function cook(str) {
        return str;
    }
    console.log(cook('大猪蹄子'));

function getResult() {
        return 789;
    }

    console.log(getResult());
```

3.用函数返回两个数的最大值

```js
function getMax(n1, n2) {
       
        return n1 > n2 ? n1 : n2;
    } console.log(getMax(8, 9));
```

4.求数组中的最大值

```js
function getMax(arr) {
        var max = arr[0];
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i]
            }
        } return max;
    } var a = getMax([5, 2, 99, 101, 67, 77]);
    console.log(a);
```

注：return后面的代码不会被执行，return只返回一个值，返回结果最后一个值

![1607672760284](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607672760284.png)

#### 7.5 arguments

是函数的一个内置对象，arguments对象存储了传递的所有实参

只有函数才有arguments对象，而且是每个函数都内置好了这个arguments对象。伪数组，并不是正真意义上的数组，具有length属性，按照索引方式进行存储的，没有正真数组的一些方法，pop()

push()等等；

```js
 function ab() {
        console.log(arguments);
        console.log(arguments.length);
        console.log(arguments[0]);
        for (var i = 0; i < arguments.length; i++) {
            console.log(arguments[i]);
        }
    }
    ab(1, 2, 3);
    ab(9, 6, 3, 7, 2, 0, 3)
```

用arguments求任意一组数的最大值

```js
  function getMax() {
        var max = arguments[0];
        for (var i = 0; i < arguments.length; i++) {
            if (arguments[i] > max) {
                max = arguments[i];
            }
        } return max;
    }

  console.log(getMax(10, 4, 5, 7, 8, 6, 5));
```

#### 7.6先执行函数调用，在执行函数

![1607695252523](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607695252523.png)

## 8.js作用域

#### 8.1 js作用域

1.作用域就是代码名字（变量）在某个范围内起作用和效果，目的是为了提高程序的可靠性更重要的是减少命名冲突

2.js的作用域：（es6）之前：全局作用域和局部作用域

3.全局作用域：整个js标签，或者是单独的js文件

4.局部作用域（函数作用域）：在函数内部就是局部作用域，这个代码的名字只在函数内部起效果和作用

#### 8.2变量的作用域

1.全局变量：全局作用下的变量，在全局下都可以使用的变量

##### 注：在局部作用域中只赋值不声明的变量也属于全局变量

浏览器关闭时，全局变量才会被销毁，比较占内存

2.局部变量：在局部作用域（函数），只能在函数内部使用 

##### 注：函数的形参也是局部变量

只在函数内部使用，当其所在的代码块被执行时，会被初始化；当代码块运行结束后，就会被销毁，比较节省空间

3.作用域链：内部函数访问外部函数的变量，采取的是链式查找的方式来决定取那个值，这种结构我们称作作用域链

```js
  var num = 20;
    function fun() {
        var num = 10;
        function fn() {
            console.log(num);
        }
        fn();
    }
    fun();//10
```

#### 作用域/闭包

![1609385843080](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1609385843080.png)

```js
(1)function foo(x){
				var num=3;
				return function(y){
					alert(x+y+(++num));
				}
			}
			var bar=foo(5);
			bar(20);//输出29
(2)function fun(n,o){
				console.log(o);
				return{
					fun:function(m){
						return fun(m,n);
					}
				};
			}
			var a=fun(0);//undefined
			a.fun(1);//0
			a.fun(2);//0
			a.fun(3);//0
```

![1609679127907](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1609679127907.png)

```js
var sum = function (x, y) {
            if (y !== undefined)
                return x + y;

            return function (a) {
                return x + a;
            }

        }
        console.log(sum(2, 3));//5
        console.log(sum(2)(3));//5
```



#### 8.3 预解析

1.js引擎运行js分为两步：预解析 代码执行

（1）.预解析，js引擎会把js里的所有var和function提升到当前作用域的最前面

（2）代码执行 按照代码执行的顺序从上往下执行

2.预解析分为变量解析（变量提升）和函数预解析（函数提升）

（1）变量提升 就是把所有的变量声明提升到当前作用域的最前面 不提升赋值操作

（2）函数提升 就是把所用的函数声明提升到当前作用域的最前面 不调用函数

![1609398530989](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1609398530989.png)

```js
  1.console.log(num);
    var num = 10;//  undefined
   
    相当于执行了
    var num;
    console.log(num);
    num = 10;//只声明不赋值就输出


   2. fn();
    var fn = function fun() {
        console.log(2);
    }  //报错
  
    相当于执行了
    var fn;
    fn();//调用之前没有这个函数，
    fn = function fun() {
        console.log(2);
    } //上面的代码没有这个函数，肯定会报错
3.  var num = 10;
    fun();
    function fun() {
        console.log(num);
        var num = 20;
    } //  undefined

    相当于执行了
    var num;
    function fun() {
        var num;
        console.log(num);
        num = 20;
    }
    fun();
```

```js
 f1();
    console.log(c);
    console.log(b);
    console.log(a);
    function f1() {
        var a = b = c = 9;
        console.log(a);
        console.log(b);
        console.log(c);
    }

    相当于执行了
    function f1() {
        var a = 9;
        b = 9; //b,c为全局变量 都可以调用
        c = 9;
        console.log(a);
        console.log(b);
        console.log(c);
    }
    f1();
    console.log(c);
    console.log(b);
    console.log(a);//全局作用域没有声明a 故报错 结果为 99999报错
```

## 9.对象：特质具体事物

### 9.1创建对象的三种方法

##### 1.利用字面量创建对象

var 对象={}

（1）里面的属性或者方法我们采取键值对的形式 键 属性名 ：值 属性值

（2）多个属性或者方法中间用逗号隔开

（3）方法后面跟的是一个匿名函数

##### 使用 对象  （1）名.属性名 可以理解为  的（2）对象名['属性名']

```js
 var dog = {
        hname: '可可',
        type: '阿拉斯加犬',
        age: '5岁',
        color: '棕红色',
        skill: function () {
            console.log('汪汪汪' + '\t' + '演电影');
        }
    }
    console.log(dog.hname);
    console.log(dog.type, dog.color);
    dog.skill();
    console.log(dog['age']);

可以用delete 删除属性
delete person.boyFriend;
```

##### #变量，属性，函数，方法的区别：

1.变量和属性的 相同点：它们都是用来存储数据的

不同点  变量：单独声明并赋值，使用的时候直接写变量名

​             属性：在对象里面的不需要声明的，使用的时候必须是 对象.属性   

2.函数和方法的相同点  都是实现某种功能 做某件事

函数：单独声明，并且调用的函数名（）单独存在的

方法：在对象里面 调用的时候  对象.方法()

##### 2.利用 new object创建对象

```js
 var dog = new Object();
    dog.sname = '可可';
    dog.age = 13;
    dog.sex = '男';
    dog.sayhi = function () {
        console.log('hi~');
    }
    console.log(dog.sname);
    console.log(dog['sex']);
    dog.sayhi();
```



##### 3.利用构造函数创建对象

原因：创建对象的方式一次只能创建一个对象

构造函数就是把对象里面一些相同的属性和方法抽取出来封装到函数里面

```js
 function 构造函数名() {
        this.属性 = 值;
        this.方法 = function () { }

    }
    new 构造函数名();
```

构造函数名首字母要大写，不需要return就可以返回结果

调用构造函数必须使用new

我们只要new Actor（）调用函数就创建了一个对象 yyqx {}

```js
  function Actor(uname, age, sex) {
        this.name = uname;
        this.age = age;
        this.sex = sex;
        this.skill = function (move) {
            console.log(move);
        }
    }
    var yyqx = new Actor('易烊千玺', '20岁', '男');
    console.log(yyqx.name);
    console.log(yyqx['sex']);
    yyqx.skill('少年的你');
    var wjk = new Actor('王俊凯', 21, '男');
    console.log(wjk.name);
    console.log(wjk['age']);
```

![1607770209692](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607770209692.png)

![1607770519298](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607770519298.png)

### 9.2遍历对象属性

##### 1.for in:建议对对象进行遍历

```js
var dog = {
            uname: '点点',
            age: 8,
            sex: '女',
            skill: function () {
                console.log('汪汪');
            }
        }
        for (var k in dog) {
            console.log(k);//得到属性名
            console.log(dog[k]);//得到属性值

        }//一般是k或key,很少遍历方法
```

##### 2.forEach循环遍历

forEach方法中的function回调有三个参数：item参数是遍历的数组元素，index参数是对应的数组索引，array参数是数组本身

```js
for (var i = 0; i < arr.length; i++) {
				sum += arr[i];
			}
			//等价于
			var arr = [1, 2, 3, 4];
			var sum = 0;
			arr.forEach(function(item, index, array) {//item为元素，index为索引号 
				array[index] == item; //结果为true
				sum += item;
			});
			console.log(sum);
```

```js
var students = [
				{ name: "黄小米", code: "3018", age: 16, score: 584 },
				{ name: "黄渤", code: "3019", age: 19, score: 599 },
				{ name: "黄磊", code: "3020", age: 18, score: 650 },
				{ name: "黄晓明", code: "3021", age: 17, score: 530 },
			];
			//for循环
			var sum = 0;
			for (var i = 0; i < students.length; i++) {
				sum += students[i].age;
			}
			var average = sum / students.length;
			console.log(sum);
			console.log('平均年龄：%f', average);

				//forEach 循环
			var aveScore = 0;
			var sumScore = 0;
			students.forEach(function(item, index) {
				sumScore += item.score;

			});
			aveScore = sumScore / students.length;
			console.log(aveScore);
			console.log(sumScore);
```



### 9.3内置对象

#### 9.3.1 内置对象

1.js中的对象分为3种：自定义对象，内置对象，浏览器对象

前两种属于ECMAScript，第三种属于js独有的

2.内置对象就是js语言自带得一些对象，帮助开发者快速开发

3.js提供了多个内置对象：Math,Data,Array,Sring等

#### 9.3.2Math对象

```js
  console.log(Math.abs(-2));//绝对值
        console.log(Math.abs('-1'));//隐式转换
        console.log(Math.floor(1.9));//往下取整
        console.log(Math.ceil(1.1));//往上取整
        console.log(Math.round(1.5));//四舍五入
        console.log(Math.round(1.4));
        console.log(Math.round(-1.5));//这里5特殊，往大了取

```

##### （2）Math.random()随机数

```js
得到两个数之间的任意整数
 function getRandom(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;//牢记公式
        }
        console.log(getRandom(1, 100));

随机输出名字
  function getRandom(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        console.log(getRandom(1, 100));
        var arr = ['小高', '小李', '小王', '小张', '小韩', '小刘', '刘蓓蓓', '高静文', '高海翔'];
         console.log(arr[getRandom(0, arr.length - 1)]);
        alert(arr[getRandom(0, arr.length - 1)]);
猜数字游戏
   function getRandom(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        var random = getRandom(1, 10);
        while (true) {
            var num = prompt('请输入一个数')
            if (num > random) {
                alert('数字大了，继续猜');
            }
            else if (num < random) {
                alert('数字小了，继续猜');
            }
            else {
                alert('猜对了');
                break;//退出整个循环
            }
        }
```

#### 9.3.3 Data日期对象

是一个构造函数，需要实例化后使用 Date实例用来处理日期和时间

```js
 var date = new Date();
        console.log(date);//输出现在的时间
        var date1 = new Date(2020, 9, 1);
        console.log(date1);
        var date2 = new Date('2020-12-24');
        console.log(date2);
```

##### 1.日期格式化

![1607829835571](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607829835571.png)

```js
 var year = new Date();
        console.log(year.getFullYear());//返回当前年份
        console.log(year.getMonth());//0-11，返回月份小一个月
        console.log(year.getDate());//返回当前几号
        console.log(year.getDay());//返回0-6 周天代表0
        //输出今天是xx年xx月xx日星期x
        var years = year.getFullYear();
        var month = year.getMonth() + 1;
        var day = year.getDate();
        var xq = year.getDay();//星期
        var arr = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
        console.log('今天是：' + years + '年' + month + '月' + day + '日' + arr[xq]);
```

```js
时分秒 

var day = new Date();
        console.log(day.getHours());
        console.log(day.getMinutes());
        console.log(day.getSeconds());
        function getTime() {
            var h = day.getHours();
            var m = day.getMinutes();
            var s = day.getSeconds();
            //console.log(h + ':' + m + ':' + s);
            return h + ':' + m + ':' + s
        }
        // getTime();
        console.log(getTime());
```

```js
毫秒数
var date = new Date();
        console.log(date.valueOf());
        console.log(date.getTime());
        //2.简单的写法 最管用的写法
        var date1 = +new Date();
        console.log(date1); //距离1970年1月1号过了多少毫秒数
        //3.h5新增的
        console.log(Date.now());
```

##### 2.倒计时案例

![1607851262062](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607851262062.png)

```js
function countDown(time) {
            var nowTime = +new Date();//返回的是当前时间总的毫秒数
            var inputTime = +new Date(time);//返回的是当前时间总的毫秒数
            var times = (inputTime - nowTime) / 1000;//times是剩余时间总的毫秒数
            var d = parseInt(times / 60 / 60 / 24);
            d = d < 10 ? '0' + d : d;
            var h = parseInt(times / 60 / 60 % 24);
            h = h < 10 ? '0' + h : h;
            var m = parseInt(times / 60 % 60);
            m = m < 10 ? '0' + m : m;
            var s = parseInt(times % 60);
            s = s < 10 ? '0' + s : s;
            return d + '天' + h + '时' + m + '分' + s + '秒';

        }
        console.log(countDown('2020-12-13 18:00:00'));
```

#### 9.3.4  数组对象

```js
var arr = new Array(2);//创建了一个空的数组，长度为2
        var arr = new Array(2, 3);//等价于[2,3] 表示数组中有两个元素2和3
        console.log(arr);
```

##### 1.反转数组

```js
function reverse(arr) {
            var newArray = [];
            for (var i = arr.length - 1; i >= 0; i--) {
                newArray[newArray.length] = arr[i];
            }
            return newArray;
        }
        console.log(reverse([1, 2, 3, 4, 5, 6, 7]));
```

##### 2.检测是否为数组

```js
  //(1)instanceof 检测是否为数组
        var arr = [];
        var arr1 = {};
        console.log(arr instanceof Array);
        console.log(arr1 instanceof Array);
        //(2)Array.isArray IE9以上版本使用，H5新增的检测是否为数组
        console.log(Array.isArray(arr));
        console.log(Array.isArray(arr1));

```

##### 3.添加删除数组的方法

![1607858684675](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607858684675.png)



```js
  //push可以给数组增加新的元素，括号里直接写新数组的元素
        var arr = [1, 2, 3];
        // arr.push(4, 5, 6);
        // console.log(arr);
        //push完毕后 会返回新数组的长度
        console.log(arr.push(4, 5, 6));//返回数组长度
        //unshift 在数组开头添加一个或多个元素
        arr.unshift('blue');
        console.log(arr);
        console.log(arr.unshift('blue'));//返回新数组的长度
```

```js
 arr.pop(); //删除数组的最后一个元素 一次只能删一个
        console.log(arr.pop());//返回删除的元素
        console.log(arr);
        arr.shift();//删除第一个元素
        console.log(arr);
        console.log(arr.shift());//返回删除元素
```

```js
//删除小于2000的数并存到新数组中
        var arr = [1500, 1200, 2000, 2100, 1800];
        var newArr = [];
        for (var i = 0; i < arr.length; i++) {
            if (arr[i] < 2000) {
                //  newArr[newArr.length] = arr[i];
                newArr.push(arr[i]);
            }
        }
        console.log(newArr);
```

##### 4.反转数组 reverse()  以及排序sort()

```js
   var arr = ['pink', 'blue', 'black'];
        arr.reverse();//反转数组
        console.log(arr);
        var arr1 = [9, 41, 6, 8, 17, 0, 25, 5]
        arr1.sort(function (a, b) {
            //return a - b;//升序
            return b - a;//降序

        });//sort对个位数有用 对十位数及以上要用这个函数
        console.log(arr1);//冒泡排序
```

##### 5.返回数组的索引号 indexOf（）

```js
 var arr = ['多', '少', '大', '小'];
        console.log(arr.indexOf('少'));//返回元素的索引号 没有则返回-1，从前面开始查找 有重复的只返回第一个元素索引号
        console.log(arr.lastIndexOf('小'));//也返回索引号，不过是倒着查找 没有返回-1
```

##### 6.数组去重

```js
   //有一个数组['c','a','z','a','x','a','x','c','b'],要去去除数组中重复的元素
        function del(arr) {
            var newArr = [];
            for (var i = 0; i < arr.length; i++) {
                if (newArr.indexOf(arr[i]) === -1) {
//                   
                    newArr.push(arr[i]);
                }
            } return newArr;

        }
        var num = del(['c', 'a', 'z', 'a', 'x', 'a', 'x', 'c', 'b'])
        console.log(num);
```

7. ##### splice(删除的index,删除的个数，增加的元素...)

```js
 arr.splice(1, 2, 7, 8, 9);
```

##### 8.数组转换为字符串 toString() , join()

##### 9.toFixed()     把数字转换为字符串，结果的小数点后有指定位数的数字。

```js
 oTotal.innerText = mul.toFixed(2);//把数字转换为字符串，结果的小数点后有指定位数的数字：
```

##### 10.split('分隔符')；

```js

		var stri = "How are you doing today?";
		var n = stri.split(' '); //转化为数组 并且从那个分隔符开始分割为每一个数组元素
		console.log(n);

```

##### 11.其他的数组对象方法

![1607863302195](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607863302195.png)

```js
 var arr = [2, 5, 3, 6, 8];
        console.log(arr.toString());//数组转换为字符串
        //join(分隔符)
        var arr1 = ['pink', 'blue', 'purple'];
        console.log(arr1.join('-'));
```

#### 9.3.5 字符串对象

![1607865599853](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607865599853.png)

##### 1.基本包装类型

为了方便操作基本数据类型，js还提供了三个特殊的引用类型：String,Number和Boolean

基本包装类型就是把简单数据类型包装成复杂数据类型，这样基本数据类型就有了属性和方法

![1607865930192](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607865930192.png)

![1607865956073](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607865956073.png)

##### 2.字符串不可变

指的是里面的值不可变，虽然看上去可以改变内容，但其实是地址变了，内存中心开辟了一个内存空间

字符串不可变所以不要大量拼接字符串

##### 3.根据字符返回位置

##### 检索字符串: indexOf()



```js
 var str = '改革春风吹满地，春天来了';
        console.log(str.indexOf('春'));//返回索引号
        console.log(str.indexOf('春', 3));//从第三个开始查找
```

![1607868490458](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607868490458.png)

```js
查找字符串出现的位置及次数（重点案例）
var str = 'oabcoefoxyozzopp';
        var index = str.indexOf('o');
        var num = 0;
        while (index !== -1) {
            console.log(index);
            num++;
            index = str.indexOf('o', index + 1);

        }
        console.log('o出现的次数是' + num);

```

##### 4.根据位置返回字符串（重点）

![1607869078748](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607869078748.png)

```js
//1.charAt(index) 根据位置返回字符
        var str = 'purplea';
        console.log(str.charAt(3));
        for (var i = 0; i < str.length; i++) {
            console.log(str.charAt(i));//console.log(str[i]);//结果等价于
        }
        //2.chartCodeAt(index)返回索引号对应元素的ASCII值
        console.log(str.charCodeAt(6));//97
        //str[index] H5新增的 根据位置返回字符
        console.log(str[1]);


```

```js
     //判断一个字符串中出现最多次的字符，并统计其字数
        var str = 'abcoefoxyozzopp';
        var o = {};
        for (var i = 0; i < str.length; i++) {
            var chars = str.charAt(i);
            if (o[chars]) {//得到的是属性值
                o[chars]++;
            }
            else {
                o[chars] = 1;
            }

        }
        console.log(o);//输出字符出现的次数
        var max = 0;
        var cha = '';
        for (var k in o) {
            if (o[k] > max) {
                max = o[k];
                cha = k;
            }
        }
        console.log('出现最多的次数是：' + max);
        console.log('出现次数最多的字符是：' + cha);

```

![1607929531145](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607929531145.png)

替换字符串: replace() .
提取字符串片段:slice()/substr()/substring()·

slice(start,end)比substring(start,length)灵活

```js
  //1.字符串拼接 concat
        var str = 'blue';
        console.log(str.concat('pink'));
        //2.查找字符 substr()
        var str1 = '改革春风吹满地';
        console.log(str1.substr(2, 5));//第一个为字符索引号，第二个是要查几个字符
        console.log(str.replace('e', 'c'));// 输出bluc 

        //3.替换字符串中的字符 replace()
        var abc = 'abcoefoxyozzopp';
        while (abc.indexOf('o') !== -1) {
            abc = abc.replace('o', '*');
        }
        console.log(abc);
        //4.字符转换为数组 split('分隔符') join把数组转换为字符串
        var str2 = 'pink,red,blue';
        console.log(str2.split(','));
        var str3 = 'pink&red&blue';
        console.log(str3.split('&'));//分隔符是什么，括号里就写什么
```

![1607931843354](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607931843354.png)

### 10.简单数据类型 和复杂数据类型

![1607934434454](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607934434454.png)

1.简单数据类型存放在栈里面，里面直接开辟一个空间存放的是值

2.复杂数据类型 首先在栈里面存放十六进制的地址，然后这个地址指向堆里面的数据

![1607934696318](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607934696318.png)

![1607935009179](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607935009179.png)

![1607935884046](C:\Users\ASUS\AppData\Roaming\Typora\typora-user-images\1607935884046.png)



