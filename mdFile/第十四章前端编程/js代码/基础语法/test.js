function func(i) {
    return i*i
}

const map = function (array,func) {
    a = '';
    for (i of array)
        a+=  func(i);
    console.log(a)
};

console.log(map([1,2,3,4],func));

