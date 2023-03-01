cel2fahr:
	mulsd	.LC0(%rip), %xmm0
	addsd	.LC1(%rip), %xmm0
	ret
.LC0:
	.long	-858993459
	.long	1073532108
	.align 8
.LC1:
	.long	0
	.long	1077936128