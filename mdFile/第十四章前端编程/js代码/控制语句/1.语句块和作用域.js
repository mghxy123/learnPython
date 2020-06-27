function hello(){
    let a = 1;
    let b = 2;
    c = 3;
}
//let d = 100

if(1){
    let d = 4;
    var e = 5;
    f = 6;
    if(true){
        console.log(d);
        console.log(e);
        console.log(f);
        console.log('~~~~~~~~~~~~~~~~~~~~~~');
        g = 10;
        var h = 11;
    }
}

//console.log(a) //不可见
//console.log(b) //不可见
//console.log(c) //不可见?

//console.log(d) //块作用域使用let,不可见;但是块外的d是可见的
console.log(e)  //块作用域使用var,可见
console.log(f) //块作用域隐式声明,可见
console.log(g) //可见
console.log(g) //可见