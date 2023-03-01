top:
	lock(L1);
	if (trylock(L2) == -1) {
		unlock(L1);
		goto top;
	}