x = 42; 
var y = 43;
let z = 60;
myobj = new Number();

myobj.h = 4; //create property h
console.log(delete x);              //returns true (can delete if declated implicitly)
console.log(delete y);              //return false (cannot delete if declared with var)
console.log(delete z);              //return false 
console.log(delete Math.PI);        //return false (cannot delete predefined  propertied)
console.log(delete myobj.h);        //return true (can delete user-defined propertied)
console.log(delete myobj);          //return true (can delete if declared implicitly)
console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~');

var  trees = new Array('redwood', 'bay', 'cedar', 'oak', 'maple');
for (var i=0;i<trees.length;i++){
    console.log(trees[i])
}
console.log('=========================')
delete trees[3]; // 数组中元素被删除,但空着的位置是undefined
for(var i=0;i<trees.length;i++){
    console.log(trees[i])
}