let store = require('store');

store.set('user','hxy');
console.log(store.get('user'));

store.remove('user');
console.log(store.get('user')); //取不到值,为undifined
console.log(store.get('user','nouser')); //取到默认值nouser

//store 存储字典,
store.set('user',{name:'hxy',age:'30'});
console.log(store.get('user'));
console.log(store.get('user').name);

store.set('school',{name:'yongle'});

// 这里的each相当云for循环一个容器
store.each(function(value,key){
    console.log(key, '-->' , value)
});

// 清除所有值key value
store.clearAll();

console.log(store.get('user')); //undefined