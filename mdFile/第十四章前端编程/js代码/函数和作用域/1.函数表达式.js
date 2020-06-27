//匿名函数
const add = function (x,y) { 
    return x+y;
 }
 console.log(add(4,6));

 // 有名字的函数表达式
 const sub = function fn(x,y){
     return x-y;
 };

 console.log(sub(3,6));
//  console.log(fn(3,5)); //fn 只能函数内部使用


// 有名字的函数表达式
const sum = function _sum(n){
    if (n==1) return n;
    return n + _sum(--n) //_sum 只能内部使用
}

console.log(sum(5))