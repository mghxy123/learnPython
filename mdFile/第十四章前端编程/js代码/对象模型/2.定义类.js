//基类定义

class Point{
    constructor(x,y)/*构造器*/{
        this.x = x;
        this.y = y;
    }
    show(){//方法
        console.log(this,this.x,this.y);
    }
}

let p1 = new Point(10.11);
p1.show()

// 继承
class Point2 extends Point{
    constructor (x,y,z){
        super(x,y); //父类构造器,应该放在有效语句的第一条
        this.x = z;
    }
}

let p2 = new Point2(20,21,22);
p2.show()