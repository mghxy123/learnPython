const add = (x,y) => {console.log(x,y);return x+y};
console.log(add(...[100,200]));
console.log(add(...[100,200,300,3,4,5]));
console.log(add(...[1000]));