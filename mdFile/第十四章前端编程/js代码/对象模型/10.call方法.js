var school = {
    name: 'hxy',
    getNameFunc: function(){
        console.log(this.name);
        console.log(this);
        return function(){
            console.log(this === global); //this 是否是global对象
            return this.name;
        }
    }
}

console.log(school.getNameFunc().call(school));

