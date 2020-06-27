var map = function * (fn,arr) { 
    for(i in arr){
        yield fn(arr[i]);
    }
 }

 let newarr = map(x => x+10 ,[1,2,3,4]);

 for(x of newarr){
     console.log(x)
 }