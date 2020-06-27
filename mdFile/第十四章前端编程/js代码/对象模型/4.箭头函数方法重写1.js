// 基类定义
class Point{
    constructor(x,y){//构造器
    this.x = x;
    this.y = y;
    this.show = () => console.log('Point');
    }
}

//继承
class Point2 extends Point{
    constructor (x,y,z){
        super(x,y);
        this.z = z;
        this.show = () => console.log('Point2');
    }
}
let p2 = new Point2(21,22,23);
p2.show();//Point2