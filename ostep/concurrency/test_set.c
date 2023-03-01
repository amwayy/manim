int TestAndSet(int *ptr, int new) {
	int old = *ptr; // fetch old value at ptr
	*ptr = new; // store ’new’ into ptr
	return old; // return the old value
}