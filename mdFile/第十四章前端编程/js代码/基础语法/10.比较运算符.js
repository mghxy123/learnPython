console.log(100 > '200') //false
console.log(300 > '200') // true
console.log(300 > '2000') // false
console.log(3000 > '2a') // false
console.log(3000 > 'a2') // false
console.log('300' > '200') // true

// 比较宽松
console.log(300 == '300') // true
console.log('300' == '300') // true

//严格比较 ===
console.log(300 === '300') // false
console.log('200' === '200') // true