// const arr = [1,2,3,4];
// arr.push(100)
// console.log(arr)
// 不是说const定义的变量不能被改变吗?这里为什么可以增加数据?
// const a = 20;
// a = 2000;
// console.log(a)

//  这里的a 为什么又报错了?


/*那是因为arr是一个容器,我们只是增加了容器里面的内容,但是并没有修改指向arr的地址,他,这并不算是把变量改变了,

而a的两次赋值就是改变了a,所以会报错
*/
const arr = [100,200,300];
let [x,y,z] = arr;
console.log(1,x,y,z)

//丢弃
const [,b,] = arr;
console.log(2,b);
// b = 5 // 异常,b声明为const,不可修改

//少于数组元素
const [d,e] = arr;
console.log(3,d,e);

//多与数组元素  多出来没有的就是undefined
const [m,n,o,p] = arr;
console.log(m,n,o,p);

// 可变量
const [ f,...args] = arr;
console.log(5,f,args);

// 支持默认值 300被丢弃了
const [j=1,k,,,,l=20] = arr;
console.log(j,k,l);