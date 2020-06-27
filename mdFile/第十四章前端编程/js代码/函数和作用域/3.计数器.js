const counter = function () { 
    let   c = 0;
    return function () { 
        return ++c;
     }
 }
 const c = counter()
 console.log(c())
 console.log(c())
 console.log(c())