//数组
let  arr = [10, 20, 30, 40]

console.log(arr[1]) //20

for(let x in arr){
    console.log(x); //返回索引
}

for(let index in arr){
    console.log(`${index} : ${arr[index]}`);//插值
}

//C风格
for(let i=0;i<arr.length;i++){
    console.log(arr[i]);
}

// 对象
let obj={
    a:1,
    b:'hxy',
    c:true
};

console.log(obj.a);
console.log(obj['b']);
console.log(obj.d);//undefined
console.log('~~~~~~~~~~~~')

for(let x in obj){
    console.log(x); //属性名
}

for(let key in obj){ //返回数组的index
    console.log(`${key} :${obj[key]}`);
}