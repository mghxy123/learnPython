// throw new Error('this is new error');
// throw new ReferenceError('ref error');
// throw 1;
// throw 'not ok';
// throw [1,2,3];
// throw {'a':1};
// throw () => {}; //抛出一个函数作为异常


try {
    throw new Error('this is new error');
    // throw new ReferenceError('ref error');
    // throw 1;
    // throw 'not ok';
    // throw [1,2,3];
    // throw {'a':1};
    // throw () => {}; //抛出一个函数作为异常
} catch(error){
    console.log('that is ~~~~~~~~~error',error);
    console.log('that is ~~~~~~~~~ type',typeof(error));
    console.log('that is ~~~~~~~~~ error name',error.constructor.name)
}