// for of 
let arr = [1,2,3,4,5]
let obj = {
    a:1,
    b:'hxy',
    c:true
}

for(let i of arr){ // 返回数组的元素
    console.log(i)
}

// for(let i of obj){ //异常,不可迭代
//     console.log(i)
// }