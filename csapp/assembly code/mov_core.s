mov:
	movq	$8, (%rdi)
	movslq	%esi, %rax
	movq	%rax, (%rdi)
	ret