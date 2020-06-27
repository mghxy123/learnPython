
```flow

st=>start: index.html
e=>end: 结束
op=>operation: 我的操作
cond=>condition: 确认？

st->op->cond
cond(yes)->e
cond(no)->op
```

index.html --index.js通過id(document.getElementById('root'))找到html--> --index.html的路由通過uri去找到对应的主键(Router->to path --> Route->path -component主键)--> 主键找到主键目录下面的对应注入的主键文件