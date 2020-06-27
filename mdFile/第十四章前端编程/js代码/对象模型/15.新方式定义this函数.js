class school{ //这是ES6的新语法
    constructor(){
        this.name = 'hxy';
    }
    getNameFunc() {
        console.log(this.name);
        console.log(this,typeof(this));
        return () => {
            console.log(this == global); //this 是否是global对象
            return this.name;
        }
    }
}
console.log(new school().getNameFunc()());
let f = new school().getNameFunc()
console.log(f);