console.log('a' instanceof String) //false
console.log(1 instanceof Number) //false

a = new String('b')
console.log(a instanceof String) //false
console.log(new  Number(1) instanceof Number) //false
console.log(a instanceof Object) //false

console.log(typeof('a'))
console.log(typeof 'a')
console.log(typeof a )