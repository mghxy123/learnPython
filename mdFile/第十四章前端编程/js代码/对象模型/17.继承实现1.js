class Serialization{
    constructor(){
        console.log('Serialization constructor~~~');
        if (typeof(this.stringify) !== 'function'){
            throw new ReferenceError('should define stringify.');
        }
    }
}

class Point extends Serialization{
    constructor(x,y){
        console.log('Point Constructor~~~')
        super();//调用父构造器
        this.x = x;
        this.y = y;
    }
}

class Point2 extends Point{
    constructor(x,y,z){
        super(x,y);
        this.z = z;
    }
    stringify (){
        return `<Point x = ${this.x},y = ${this.y}, z = ${this.z}>`
    }
}

p = new Point(1,2);
console.log(p.stringify());
p2 = new Point2(4,5,6);
console.log(p2.stringify());
