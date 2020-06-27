var school = {
    name: 'hxy',
    getNameFunc: function(){
        console.log(this.name);
        console.log(this);
        return function(that){
            console.log(this === global); //this 是否是global对象
            return that.name;
        }
    }
}

console.log(school.getNameFunc()(school));

