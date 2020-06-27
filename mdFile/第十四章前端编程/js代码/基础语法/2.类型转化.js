//类型转化

// 弱类型
console.log('=====string=====')
console.log(a = 3 + 'hxy', typeof(a))
console.log(a = null +'hxy',typeof(a))
console.log(a = undefined +'hxy',typeof(a))
console.log(a = true+ 'hxy',typeof(a))

// 数字
console.log('=====number=====')
console.log(a = 3+ 8,typeof(a))
console.log(a = null + 8,typeof(a)) // undefined没法转换成一个对应的数字
console.log(a = true + 8,typeof(a))
console.log(a = false + 8,typeof(a))

// boolean
console.log('=====bool=====')
console.log(a = null + true,typeof(a))
console.log(a = null + false,typeof(a))
console.log(a = undefined + true,typeof(a)) //undefined没办法转换成一个对应的数字
console.log(a = undefined + false,typeof(a)) //NaN
console.log(a = null & true,typeof(a))
console.log(a = undefined & true,typeof(a))

// 短路
console.log(a = null && true,typeof(a)) // 逻辑运算符,null 直接就是false短路
console.log(a = null && false,typeof(a)) //逻辑运算符,false短路返回false
console.log(a = false && 'hxy',typeof(a)) //boolean
console.log(a = true && 'hxy',typeof(a)) //字符串
console.log(a = true && '',typeof(a)) //字符串

//null 
console.log('=====null=====')
console.log(a = null +undefined,typeof(a))

