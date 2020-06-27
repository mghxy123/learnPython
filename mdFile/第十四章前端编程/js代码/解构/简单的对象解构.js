const obj = {
    a:100,
    b:200,
    c:300
}

let {a,b,c} = obj;
console.log(a,b,c)

let {x,y,z} = obj;
console.log(x,y,z);

// let {a,b,c} = obj; //这里会报错,那是因为abc变量已经声明过了,这里不会覆盖变量,而是抛异常,正确的做法事,取别名,即重命名
// console.log(a,b,c)

// 重命名
let {a:n,b:m, c:h} = obj;
console.log(n,m,h)


// 缺省值
let {a:M, c:N, d:D='hello'} = obj;
console.log(M,N,D);