const obj = {
    a:100,
    b:200,
    c:300
};

console.log(Object.keys(obj)); //key,ES5
console.log(Object.values(obj));// 值,实验性
console.log(Object.entries(obj)); //键值对,实验性

//assign

var metadata = {
    title: "Scratchpd",
    translation: [
        {
            locale: "de",
            localization_tags: [],
            last_edit: "2019-07-12",
            url: "/etc/hosts",
            title: "JavaScript"
        }
    ],
    url: "/en-US/docs/Tools/Scratchpad"
};
var copy = Object.assign({}/*目标对象*/,metadata,//填充源
    {schoolName:'hxy',
    url:'www.hxy.com'},//增加新的属性,同名属性覆盖
    {translations:null} //覆盖metadata的translations
);

console.log(copy);

