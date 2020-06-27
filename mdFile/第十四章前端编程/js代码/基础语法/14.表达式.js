function * inc() {
    let i = 0;
    let j = 7;
    while (true) {
        yield i++;
        if (!j--) return 100;
    }
}

let gen = inc()
for (let i=0;i<10;i++) {
    console.log(gen.next());
}