for (i=1;i<10;i++){
    let line = ' '
    for(j=1;j<=i;j++){
        line += j + '*'+ i + '=' + j*i + ' '
    }
    console.log(line)
}