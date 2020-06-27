# Promise

## 概念
Promise对象用于一个异步操作的最终完成(包括成功或失败)及结果值的表示.  
简单说,就是处理异步请求的.   
之所以叫做Promise,就是我承诺,如果处理成功了我就做什么;还是失败了又该怎么去做(;有点类似if else)  

```js
// 语法
new Promise{
    /*executor*/
    function(resolve,reject) { ... }
}
```

#### executor(执行者)
- executor 是一个带有resolve和reject**两个参数的函数**.  
- executor 函数在Promise构造函数执行时同步执行, 被传递resolve和reject函数(executor函数在Promise构造函数返回新建对象前被调用).  
- executor 内部通常会执行一些一步操作,一旦完成,就可以调用resolve函数来将promise状态改成fulfilled即完成,或者在发生错误时将它的状态改为rejected即失败.  
- 如果在executor函数中抛出一个异常错误,name给promise状态为rejected,executor函数的返回值被忽略   
- executor中,resolve或reject只能执行其中一个函数.  


#### Promise的状态
- pending: 初始状态,不是成功或者失败的状态.
- fulfilled: 意味着操作成功完成.  
- rejected: 意味着操作失败.  

#### Promise.then(onFufilled,onRejected)
参数是两个函数,根据Promise的状态来调用不同的函数,fulfilled走onFulfilled,rejected走onRejected函数.   
then的返回值是一个新的额Promise对象;调用任何一个参数后,其返回值会被新的Pormise对象来resolve,向后传递.   
[简单使用](js代码/promise/1.简单使用.js)
```js
// 简单使用
var myPromise = new Promise((resolve, reject) => {
    resolve('say hi');//执行,置状态位fulfilled
    console.log('~~~~~~~~~~~~~~~~');
    reject('say bye'); //永远执行步不到
})

console.log(myPromise);

myPromise.then(
    //如果陈宫则显示结果,
    (value) => console.log(1,myPromise,'+++++++',value),
    //如果失败则显示原因,
    (reason) => console.log(2,myPromise,'------',reason)
);
```
输出结果为: 
```js
~~~~~~~~~~~~~~~~
Promise { 'say hi' }
1 Promise { 'say hi' } '+++++++' 'say hi'
```

#### catch(onRejected)
为当前Promise对象添加一个拒绝回调,返回一个新的Promise对象. onRejected函数调用其返回值会被新的Promise对象来用resolve.  
[异常捕获catch](js代码/promise/2.异常捕获catch.js)
```js
var myPromise = new Promise((resolve, reject) =>{
    // resolve('hello'); //执行,置状态位fulfilled
    console.log('~~~~~~~~~~~')
    reject('say bye');

});

//链式处理
myPromise.then(
    //如果成功则显示结果
    (value) => console.log(1,myPromise,value),
    // 如果失败则显示原因
    (reason) => console.log(2,myPromise,reason)
).then(
    function (v){
        console.log(2.5,v);
        return Promise.reject(v+'*****');
    
    },
    (r) => {return '没有原因'}
).catch( reason => {
        console.log(3,reason);
        return Promise.resolve(reason);
});
```
输出结果为: 

```js
~~~~~~~~~~~
2 Promise { <rejected> 'say bye' } 'say bye'
2.5 undefined
3 'undefined*****'
```
这里为什么会返回undefined,那是因为我们在第myPromise.then的时候没有返回,导致后面的后没有返回值传递,所以都是undefined

## 异步实例
[异步实例](js代码/promise/3.异步实例.js)

```js
function runAsync(){
    return new Promise(function(resolve,reject){
        //异步调用,
        setTimeout(function(){
            console.log('do something');
            resolve("I'm ok");

        },3000); //单位是毫秒, 3000就是3秒
    });
}
//调用

runAsync().then(value => {
    console.log(1+' then '+value); //I'm ok
    return Promise.reject(value+'*');
}).catch(reason =>{
    console.log(2+' catch '+reason); //I'm ok*
    return Promise.resolve(reason+'*');
}).then(value => {
    console.log(3+' then '+value); // I'm ok**
    console.log('END');
})

console.log('~~~~~~~~~fin~~~~~~~~~~~~')
```
先输出fin,三秒之后才把promise的过程陆续得输出出来  

输出结果为:

```js
~~~~~~~~~fin~~~~~~~~~~~~
do something
1 then I'm ok
2 catch I'm ok*
3 then I'm ok**
END
```

总结:
这里如果不好理解的话可以把 resolve(fulfilled) 当做if; reject(rejected)当做else;(then (if,else)).catch(do something).then(if,else),只要有返回值就可以一只链式连接下去