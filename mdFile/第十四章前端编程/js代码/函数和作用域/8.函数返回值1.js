a = (x=5,y=6,true);
console.log(a);//true

b = (123,true,z = 'test');
console.log(b);

function c() { 
    return z = 5,y = 6,true,'ok';
 }

 console.log(c());//ok