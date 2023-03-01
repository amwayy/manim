main:
    subq    $8, %rsp
    movl    $.LCO, %edi
    call    puts
    movl    $0, %eax
    addq    $8, %rsp
    ret