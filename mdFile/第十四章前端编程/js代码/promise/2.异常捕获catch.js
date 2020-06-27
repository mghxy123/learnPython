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