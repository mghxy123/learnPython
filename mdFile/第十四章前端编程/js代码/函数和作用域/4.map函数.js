const map = function _map(arr,fn) { 
    newarr = []
    for (i in arr){
        newarr[i] = fn(arr[i])
    }
    return newarr
 }
 console.log(map([1,2,3,4],function (x) { return x*x }))