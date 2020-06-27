var  trees = new Array('redwood', 'bay', 'cedar', 'oak', 'maple');
console.log(0 in trees);            //returns true,0 在数组对象的index中
console.log(3 in trees);            //returns true ,3在数组对象的index中
console.log(6 in trees);            //returns false ,6不在数组对象index中
console.log("bay"in trees);         //returns false ,bay不是属性,是值
console.log("length" in trees);     //returns true, length是对象的属性
console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

delete  trees[3];
console.log(3 in trees);
for(var i=0;i<trees.length;i++){
    console.log(trees[i]);
}
console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

// Custom objects
let mycar = {
    color:'red',
    year:1988
};

console.log('color' in mycar); //returns true
console.log('model' in mycar); //returns false
console.log('year' in mycar); //true