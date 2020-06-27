# CSS(Cascading Style Sheet)
---
层叠样式表,控制HTML布局和样式.  

## 使用方式 
---
三种使用方式  
- 内联样式: 在标签使用属性stype  
- 页内样式: 在`<head>`标签中使用`<style type="text/css"></style>`  
- 外部样式: 使用CSS文件,使用`<link rel="stylesheet" type="test/css" herf="mystyle.css">`  
优先级从高到低   


## 基本语法
`selector {property1: value1, ... , propertyN: valueN}`  
例如`a {color:red; text-decoration:line-through}`, 将链接标签文字颜色变成红色.  

## 颜色写法
---
给p标签加颜色
```js
p { color: #FF0000} //大小写都行
p { color: #f00}; //这个是上面的缩写 
p { color: rgb(255,0,0);}//三原色表示,0-255
```

## <font color=red>选择器***<font>
---
### 标签选择器  
---
`body {text-align: center}`  
上例直接使用HTML标签的选择器,就是标签选择器,元素选择器.  
注意,如果将标签改为* ,表示统配所有的html标签.  

### id选择器
id指的是HTML标签内的属性id,例如`<div id="menu">`;一般作为唯一标识    
```css
#menu {
    background-color: rgb(255.255,255);
    width: 100%;
    border-bottom: #FFF solid 1px;
    margin: 0px 0px 5px 0px;
}
```

### 类选择器
类,指的是标签中的class属性,例如`<div class='main center'>`;多个类似的为一个类class  
```css
.center {
    width: 80%;
    margin: auto;
}
```

### 选择器分组
分组的选择就可以使用同样的样式声明   
```css
h1,h2,h3,h4,h5{
    color: yellow;
}
```


### 层次选择器
#### 1 后代选择器
只要是div标签下面的li不管隔了几代都要使用这个选择器  
被覆盖的就是用覆盖的选择器   
```css
div li {
    display: inline
}
```

指定id为menu下面的li使用的
```css
div#menu li {
    display: inline;
}
```

#### 2 子选择器

指定ul标签下面的li标签使用的
```css
ul > li {
    color: red;
}
```

所有div标签下**直接的子元素**li标签  
```css
ul#menu > li {
    color: red;
}
```
#### 3 相邻兄弟选择器
```css
div.detail p+p{
    color:green;
}
```
class为了detail的div标签下任意层下面的相邻p标签下下一个p标签   
有两个p则下面的p变化,有三个p,下面的两个p变化   
---
### 伪类 pseudo-classes
伪类能增加样式,类似于class   
锚伪类, 链接标签a的四种状态   
```css
a:link {color: red} /*未访问的连接*/
a:visited {color: green} /*已访问的连接*/
a:hover {color: blue} /*鼠标移动到连接上*/
a:active {color: black} /*选定的连接*/
```
伪类可以和css类配合使用  
```js
a.red:visited {color: red}
a:hover {color:red }
a{
    color: chartreuse;
    text-decoration-line: none;
}
<a class="red" href="css_syntax.asp"> CSS Syntax </a>
```

注意, 伪类和前面部分中间不能有空格.  
### 伪元素 pseudo-element
伪元素能增加元素
```js
#homepage:after {
    content:url(http://www.magedu.com/kczx/image/why1.png);
}
a:befor {
    content:'这是链接~~~~~~';
}
```
### 属性选择器
|||
|:--|:----|
|E[attrj]{sRules}|具有某属性|
|E[attr=value]{sRules}|具有某属性且等于value|
|E[attr~=value]{sRules}|具有某属性且属性值中的一个是value|
|E[attr|=value]{sRules}|具有某属性值且属性只使用了-,且-之前的部分是value的才匹配  `*[class |= "main"]能和<div class='main-center'>`减号之前的部分匹配|

```js
连接具有href属性
a[href] {
    color: blue;
    text-decoration:line-through
}

图片alt属性为magedu_logo
img[alt=magedu_logo]{
    height: 20px;
}

*[class = "main center"] {
    color: black;
}

*[class != "center"]  [
    color:green;
]
```

## 继承
```js
body {
    text-align: center;
    color: red;
}
```
观察真个页面的文字颜色,几乎都变成了红色.  
页面中福元素中使用的样式,通用CSS继承,子孙元素将继承使用元素的属性,除非重新定义类该属性.  


## 常见样式
背景 background符合属性[http://www.w3school.com.cn/css/css_background.asp](http://www.w3school.com.cn/css/css_background.asp)  
字体font复合属性[http://www.w3school.com.cn/css/css_font.asp](http://www.w3school.com.cn/css/css_font.asp)
表格border
```js
table{
    border-collapse:collapse;
}
table,td{
    border: 1px soild black;
}
```
margin外边距和padding内边距  
```js
margin: top right bottom left
padding: top right bottom left

padding: 10px 5px 16px 20px  /*按顺序来该是多少是多少*/
padding: 10px 5px 15px /* 上10px 左右5px 下15px*/
padding: 10px 5px ; /*上下10px 左右5px*/ 
padding: 10px; /*4个方向全是10px*/
margin: auto; /*浏览器计算外边距*/
```
外边距都是顺时针设置4个方向,也可以单独设置.  


----
测试html
```html
<!--<!DOCTYPE html>-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" " http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>this for css exercise</title>
    <link rel="stylesheet" href="exercise.css" type="text/css">
</head>
<body>
    <div class="main center">
        <div id="menu">
            <ul>
                <li><a id="homepage">主页</a></li>
                <li><a>Linux</a></li>
                <li><a>Python</a></li>
            </ul>
        </div>
        <a href="http://www.magedu.com" target="_blank" title="abc">请点击</a><br><span>inline span</span>
        <p>
            <span>biggest title</span>
            <img src="http://www.magedu.com/wp-content/uploads/2017/09/logo.png" alt="magedu_logo">
        </p>

        <div id="detail" name="detail" class="detail">
            <p>title</p>
            <p>content</p>
        </div>

        <div>
            <form action="" method="POST">
                <table>
                    <tr>
                        <td>用户名 <input type="hidden" name="user" value="10001010"></td>
                        <td><input type="text" name="username" value="abc"></td>
                    </tr>
                    <tr>
                        <td>密码</td>
                        <td><input type="password" name="pwd"></td>
                    </tr>
                    <tr>
                        <td>性别</td>
                        <td>
                            <input type="radio" name="gender" checked value="M">男
                            <input type="radio" name="gender" checked value="F">女
                        </td>
                    </tr>
                    <tr>
                        <td>爱好</td>
                        <td>
                            <input type="checkbox" name="interest" checked value="music">音乐
                            <input type="checkbox" name="interest" checked value="movie">电影
                        </td>
                    </tr>
                    <tr>
                        <td>其他</td>
                        <td>
                            <textarea name="" id="" cols="30" rows="10">
                            line1
                            line2
                            </textarea>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2">
                            <input type="submit" name="submit" value="提交">
                            <input type="reset" value="重置">
                        </td>
                        <td></td>
                    </tr>
                </table>
            </form>
        </div>
    </div>
</body>
</html>


```

```css
#menu {
    color: blue;
    margin: auto;
    background-color: rgb(255,255,255);
    width: 90%;
    border-bottom: #000000 solid 1px;  /*1像素 实线 白色*/
    /*margin: 0px 1px 5px 0px;*/
}

.tclass {
    color: pink;
    margin: auto;
    border-bottom: #000000 solid 1px;  /*1像素 实线 白色*/
}


h1,h2,h3,h4,h5{
    color:green;
}

div li {
    display: inline;
}

div #menu li{
    /*display:inline-block;*/
    color:red;
    margin: 0 auto 0 auto;
}

ul > li{
    display: contents;
}

div #menu ul > li {
    border-bottom-color: black;
}

div.detail p+p {
    color: green;
}


```