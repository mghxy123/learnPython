function Print(){
    this.print = function(x,y){
        console.log(x+y);
    }
}

p = new Print(1,2)
p.print(10,20)
p.print.call(p,10,20);
p.print.apply(p,[10,20])

/* 这里实例化new Print(1,2),并没有接受的对象,所以输出的都是30 */