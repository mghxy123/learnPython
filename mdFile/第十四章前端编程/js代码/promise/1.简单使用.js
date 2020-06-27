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