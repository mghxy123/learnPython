function Point(x,y) { 
    this.x = x;
    this.y = y;
    this.show = () => console.log(this,this.x,this.y);
    console.log('Point~~~~~~~~~~~~');
 }

 console.log(Point);
 p1 = new Point(4,5);
 console.log(p1);
 console.log('~~~~~~~~~~~~~~~~~~~~');

// new 就是构建对象实例,没有调用会返回undefined ,这里的this就是全局的global

 //继承
 function Point3D(x,y,z) { 
     Point.call(this,x,y); //继承
     this.z = z
     console.log('Ponit3D~~~~~~~~~~~~~');
  }
  console.log(Point3D);
  p2 = new Point(14,15,16);
  console.log(p2);
  p2.show(); //调用父类的show方法