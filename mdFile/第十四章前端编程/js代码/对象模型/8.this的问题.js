var school = {
    name: 'hxy',
    getNameFunc: function(){
        console.log(this.name);
        console.log(this);
        return function(){ //这是一个匿名的普通函数,而不是实例,如果要用this需要使用new,所以this.name是undefined未定义
            console.log(this === global); //this 是否是global对象
            return this.name;
        }
    }
}

console.log(school.getNameFunc()());

// 运行结果为
/*
hxy
{ name: 'hxy', getNameFunc: [Function: getNameFunc] }
true
undefined
*/