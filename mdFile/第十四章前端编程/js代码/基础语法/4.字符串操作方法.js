let school = 'magedu'

console.log(school.charAt(2)) //g
console.log(school[2]) //g
console.log(school.toUpperCase())
console.log(school.concat('.com')) //与后面的字符串连接
console.log(school.slice(2)) // 切片,支持负索引
console.log(school.slice(3,5))
console.log(school.slice(-2,-1))
console.log(school.slice(-1))

let url = 'www.hxy.com'
console.log(url.split('.'))
console.log(url.substr(7,2)) //返回子串从何处开始,取多长
console.log(url.substring(7,10)) //返回子串,从何处开始,到什么为止

let s = 'hxy.com'
console.log(s.indexOf('y')) //3
console.log(s.indexOf('y',4)) //7
console.log(s.replace('.com','.cn'))

s = '\thxy com \r\n'
console.log(s.trim()) // 去除两端的空白字符,trimLeft,triRight是非标函数,少用
