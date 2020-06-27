a = 200;
c = 'asdfads';
f =200;

b = `test
 q34
 aaas
 this is var a ${a}
 $(a+b)
 ${a+f}
 ${a+c}
 s
 sa`;
// console.log(b);

c[2] = 'h';
console.log(c);
console.log(c.concat('opa'));
console.log(c.replace('as','00'));
console.log(c.indexOf(2));  //是字母鸥f 不是数字零f
console.log(c.repeat(4));
console.log(c.endsWith('d'));
console.log(c.search('a'));
console.log(c.indexOf('d',3));
console.log(c.split('d'));

console.log(`\t \n a b cd \t efg`.trim()); // 去掉空白和换行
// 截取字符串
console.log(c.substr(1,4));
console.log(c.substring(1,4));
//切分,切片;
console.log(c.slice(1,3));

// 取长度
console.log(c.length);