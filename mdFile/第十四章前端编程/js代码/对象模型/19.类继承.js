const Serialization = Sup => class extends Sup {
    constructor(...args){
        console.log('Serialization constructor~~~');
        super(...args);
        if (typeof(this.stringify) !== 'function'){
            throw new ReferenceError('should define stringify.');
        }
    }
}

class Point{
    constructor(x,y){
        console.log('Point Constructor~~~')
        this.x = x;
        this.y = y;
    }
}

class Point2 extends Serialization(Point){
    constructor(x,y,z){
        super(x,y); //super是Serialization(Point)包装过的新类型
        this.z = z;
    }
    stringify (){
        return `<Point2 x = ${this.x},y = ${this.y}.>`;
    }
}

let p2 = new Point2(7,8,9);
console.log(p2.stringify());

