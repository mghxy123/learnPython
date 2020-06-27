class Add{
    constructor(x,y){
        this.x = x;
        this.y = y;
    }
    static print(){
        // console.log(this.x);//this是Add, 而不是Add的实例
        console.log('this static method')
    }
}

add = new Add(30,40);
console.log(Add);
Add.print();
// add.print();//实例不能访问直接访问静态方法,和C++,Java一致  this是一个实例,而直接类调用,没有实例,所以会报错(这里是undefined),
add.constructor.print();//实例可以通过constructor访问静态方法


// 静态的就是类的,和python不一样的是实例不能访问类的方法
// 只能用类访问静态方法
