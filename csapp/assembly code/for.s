fact_for:
	movl	$1, %edx
	movl	$2, %eax
	jmp	.L2
.L3:
	imulq	%rax, %rdx
	addq	$1, %rax
.L2:
	cmpq	%rdi, %rax
	jle	.L3
	movq	%rdx, %rax
	ret