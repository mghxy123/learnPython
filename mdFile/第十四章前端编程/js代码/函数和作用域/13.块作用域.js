// 块作用域
if(1){
    a = 100;
    var b = 200;
    let c = 300;
}
 console.log(a);
 console.log(b);//不可见
//  console.log(c);//不可见