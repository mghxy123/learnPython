// 函数中变量的作用域
function test() { 
    a = 100;
    var b = 200;
    let c = 300;
 }

 // 先要运行test函数

 test()
 console.log(a);
//  console.log(b);//不可见
//  console.log(c);//不可见