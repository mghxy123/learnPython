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
// s= new Serialization();//构建serialization失败
// p = new Point(4,5); //构造子类对象是,调用父类构造器执行也会失败