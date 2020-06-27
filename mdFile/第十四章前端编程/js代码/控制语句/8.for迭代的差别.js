function sum(arr) { 
    for(let x in arr){ // 遍历index或对象属性
        console.log(x, typeof(x), arr[x]);
    }
    for (let x of arr){ //遍历元素
        console.log(x,typeof(x));
    } 
    for(let x=0;x<arr.length;x++){ //自己定义索引数值遍历
        console.log(x,typeof(x),arr[x]);
    }
 }
 sum([3,6,9]);