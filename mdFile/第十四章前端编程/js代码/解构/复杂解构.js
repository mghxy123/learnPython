const arr = [1,[2,3],4];
const [a,[b,c],d] = arr;
console.log(a,b,c,d);

const [e,f] = arr;
console.log(e,f);

const [g,h,i,j]  = arr;
console.log(g,h,i,j);

const [k,...l] = arr;
console.log(k,l);

// 对象
var metadata = {
    title:"Scratchpad",
    translations: [
        {
            local: 'de',
            localizaton_tags: [],
            last_edit:"2019-07-10 18:01:22",
            url: 'www.baidu.com',
            title: 'test javascript'
        }
    ],
    url:"/en-US/docs/Tools/Scripchpad"
}

var {title:enTitle,translations: [{title: loacleTitle }]} = metadata;
console.log(enTitle);
console.log(loacleTitle)
//复杂的解构,只要记住,按位置解构就行了.