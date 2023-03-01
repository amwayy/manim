absdiff_se:
	cmpq	%rsi, %rdi
	jge	.L2
	movq	%rsi, %rax
	subq	%rdi, %rax
	ret
.L2:
	movq	%rdi, %rax
	subq	%rsi, %rax
	ret