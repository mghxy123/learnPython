console.log(add(4,6));
//匿名函数
function add(x,y) { //声明提升
    return x+y;
 }


//  console.log(sub(5,3)); //sub未定义
//  有名字的函数表达式
const sub = function (x,y) { 
    return x-y;
 }


 console.log(sub(3,5));
