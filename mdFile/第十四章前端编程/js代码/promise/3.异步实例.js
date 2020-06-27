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