const add = (x,y) => x+y;
console.log(add(4,5));

const add1 = (x,y) => x+y;
console.log(add1(4,6));
console.log(add1(3))


const add2 = (x=6,y) => x+y;

console.log(add2());
console.log(add2(1));
console.log(add2(y=2,z=3))
console.log(add2(y=2,z=3,4,5,6,7,8,9))
