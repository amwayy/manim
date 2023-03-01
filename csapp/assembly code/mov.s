	.file	"mov.c"
	.text
	.globl	mov
	.type	mov, @function
mov:
.LFB0:
	.cfi_startproc
	endbr64
	movq	$8, (%rdi)
	movslq	%esi, %rax
	movq	%rax, (%rdi)
	ret
	.cfi_endproc
.LFE0:
	.size	mov, .-mov
	.ident	"GCC: (Ubuntu 11.2.0-19ubuntu1) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
