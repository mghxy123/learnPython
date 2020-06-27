var a //只是声明, a为了undefined
let b
console.log(1,a,b)
// const c //可以吗? 不能.因为这是常亮
const c= 100 //常亮必须声明是赋值,之后不能在修改
console.log(c)

// c = 200 //常亮不能修改



function hello() {
    var a //只是声明,a为undefined, 作用域在函数中
    a =100
}

console.log(a) //未声明变量a,异常

//a = 200 //不能声明提升
// let a=200 //不能声明提升
// var a = 200 ;hello(); //var声明提升hoisting