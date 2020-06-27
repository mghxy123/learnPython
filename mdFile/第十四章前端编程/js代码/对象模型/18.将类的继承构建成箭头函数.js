//普通继承
class A extends Object {};
console.log(A);

// 匿名类
const A1 = class {
    constructor(x){
        this.x = x;
        
    }
}

console.log(A1);
console.log(new A1(100).x);

//匿名继承
const B = class extends Object{
    constructor(){
        super();
        console.log('B constructor');
    }
};

console.log(B);
b = new B();
console.log(b); 

//箭头函数,参数是类,返回值也是类,
// 把上列中的Object看成参数

const x = (Sup) =>{
    return class extends Sup{
        constructor(){
            super();
            console.log('C constructor');
        }

    }
}

//演化成下面的形式
const C = (Sup) => class extends Sup {
    constructor(){
        super();
        console.log('C constructor');
    }
}

// cls = new C(Object); //不可以new,因为是一个普通函数,他的返回值是一个待constructor的类
cls = C(A); //调用他返回一个类,一个带constructor的class
console.log(cls);
c = new cls();
console.log(c);

//其他写法
c1 = new (C(Object))();//new 优先级太高了,所有后面要加括号才能先调用  