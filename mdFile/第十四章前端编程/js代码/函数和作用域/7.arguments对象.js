(function (p1,...args){
    console.log(p1);
    console.log(args);
    console.log('~~~~~~~~~~~~~~~~~~');
    console.log(arguments); //字典
    for (let x of arguments){
        console.log(x);
    }
})('abc',1,3,5)

((x,...args) => {
    console.log(args);//数组
    console.log(x);
    console.log(arguments); //不是传入的值
})(...[1,3,4,5,5])