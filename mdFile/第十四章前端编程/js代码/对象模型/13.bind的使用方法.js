var school = {
    name: 'hxy',
    getNameFunc: function(){
        console.log(this.name);
        console.log(this);
        return function(){
            console.log(this == global); //this 是否是global对象
            return this.name;
        }
    }
}

var func = school.getNameFunc();
console.log(func);
console.log('~~~~~~~~~~~~~~~~~~~~')
var boundfunc = func.bind(school); //bind绑定后返回新的函数 ,把新函数绑定在school里面 这个方法目前用得较多.
console.log(boundfunc);
console.log(boundfunc());