<!--
 * @Author: 崩布猪
 * @Date: 2024-06-05 08:58:25
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-06-05 13:37:05
 * @FilePath: \CS\web\HTML.md
 * @Description: 
 * 
-->
```html
<!DOCTYPE html> // 说明文档类型为html     

<!--

 * @Author: 崩布猪

 * @Date: 2024-07-18 14:51:53

 * @LastEditors: 崩布猪

 * @LastEditTime: 2024-07-18 15:05:57

 * @FilePath: \web\内容演示\index.html

 * @Description:

 *

-->

<!DOCTYPE html>

<html lang="en">

  

<head>

    <meta charset="UTF-8">

    <!-- 元素表示那些不能由其他 HTML 元相关（meta-related）元素表示的元数据信息。 本文中是定义网页编码格式 -->

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- 元素定义视口（viewport）的宽度和缩放比例。 这可以使得网页在不同设备上显示的效果更加一致。 -->

    <title>My Webpage</title>

  

    <style>

        h1,

        h2 {

            color: blue;

            text-align: center;

        }

    </style>

    <link rel="stylesheet" href="styles.css">

</head>

  
  
  

<body>

    <header>

        <!-- 导航 用于展示介绍性内容，通常包含一组介绍性的或是辅助导航的实用元素用于展示介绍性内容，通常包含一组介绍性的或是辅助导航的实用元素 但也可能包含其他元素，比如 Logo、搜索框、作者名称，等等。-->

        <img id="logo" alt="freeCodeCamp" src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg">

        <h1>HTML/CSS Quiz</h1>

        <nav>

            <!-- 其目的是在当前文档或其他文档中提供导航链接。导航部分的常见示例是菜单，目录和索引。 -->

            <ul>

                <li><a href="#student-info">INFO</a></li>

                <li><a href="#html-questions">HTML</a></li>

                <li><a href="#css-questions">CSS</a></li>

            </ul>

        </nav>

    </header>

    <main>

        <!-- body或者应用主体部分，主题部分与文档直接相关或者扩展于文档的中心主题、一应用的主要功能部分的内容组成-->

        <h1>Welcome to my webpage</h1>

        <p>This is a paragraph.</p>

        <section>

            <!-- <section> 元素表示 HTML 文档中一个通用独立章节，它没有更具体的语义元素来表示。一般来说会包含一个标题。 -->

            <h2>Cat Photos</h2>

            <p>See more <a target="_blank" href="https://freecatphotoapp.com">cat photos</a> in our gallery.</p>

            <a href="https://freecatphotoapp.com"><img

                    src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"

                    alt="A cute orange cat lying on its back."></a>

  

            <figure>

                <!-- <figure> 元素代表一段独立的内容，可能包含 <figcaption> 元素定义的说明元素。该插图、标题和其中的内容通常作为一个独立的引用单元。 -->

                <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg"

                    alt="A slice of lasagna on a plate.">

                <figcaption>Cats <em>love</em> lasagna.</figcaption>

                <!-- <figcaption> HTML 元素是用来描述其父节点 <figure> 元素里的其余内容的标题或说明。为 <figure> 提供一个无障碍描述。 -->

            </figure>

            <article class="item">

                <!-- <article> 元素表示文档、页面、应用或网站中的独立结构，其意在成为可独立分配的或可复用的结构，如在发布中，它可能是论坛帖子、杂志或新闻文章、博客、用户提交的评论、交互式组件，或者其他独立的内容项目。 -->

                <p class="flavor">French Vanilla</p><p class="price">3.00</p>

            </article>

        </section>

  

        <h2>表单部分</h2>

        <form action="submit.php" method="get" id="survey-form">

            <fieldset class="base-info">

                <label for="name" id="name-label">姓名：

                    <input type="text" id="name" name="name" placeholder="请输入" required>

                </label>

                <label for="email" id="email-label">邮箱：

                    <input type="email" id="email" name="email" placeholder="请输入" required>

                </label>

                <label for="number" id="number-label">年龄：

                    <input type="number" id="number" name="age" min="0" max="120" placeholder="请输入" required>

                </label>

            </fieldset>

            <fieldset>

                <label for="dropdown" id="dropdown-label">知道此网站多长时间了</label>

                <select id="dropdown" name="time" required>

                    <option value="">--请选择--</option>

                    <option value="1">1年以下</option>

                    <option value="2">1-3年</option>

                    <option value="3">3-5年</option>

                    <option value="3">5年以上</option>

                </select>

                <label for="radio">你对此网站的印象<br>

                    <input type="radio" id="radio1" name="gender" value="male" required>好<br>

                    <input type="radio" id="radio2" name="gender" value="normal">还可以<br>

                    <input type="radio" id="radio2" name="gender" value="female">不好<br>

                </label>

                <label for="checkbox">你希望了解的网站增加什么功能<br>

                    <input type="checkbox" id="checkbox1" name="function" value="1">新闻资讯<br>

                    <input type="checkbox" id="checkbox2" name="function" value="2">购物<br>

                    <input type="checkbox" id="checkbox3" name="function" value="3">体育<br>

                </label>

                <Label for="textarea">你对此网站的意见或建议<br>

                    <textarea id="textarea" name="message" rows="4" cols="50"></textarea>

                </Label>

            </fieldset>

            <input type="submit" id="submit" value="提交问卷">

        </form>

  

    </main>

  

</body>

  

</html>
```

## 标签
HTML 开始文档
**head 头部**
		meta 
		title
		style
		link rel href
body 身体
	main
		h1-h6
		p
		section 章节
		div 块
		figure # 附标题内容元素
			# figcaption 描述其父节点 [`<figure>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/figure) 元素里的其余内容的标题或说明
		fieldset 对表单中的控制元素进行分组
			legend 父元素 [`<fieldset>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/fieldset) 内容的标题。
		label 表示用户界面中某个元素的说明  for 连接表单
		article 示文档、页面、应用或网站中的独立结构，其意在成为可独立分配的或可复用的结构
		form 表单
			input  ：requires属性 必须写内容
					type：text email number  radio  checkbox submit
				placeholder input框输入提示文字
			select  下拉菜单
				option
			textarea  rows 行 clos 列
			 