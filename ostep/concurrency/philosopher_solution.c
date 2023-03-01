void getchops() {
	if (p == 4) {
		sem_wait(chops[right(p)]);
		sem_wait(chops[left(p)]);
	} else {
		sem_wait(chops[left(p)]);
		sem_wait(chops[right(p)]);
	} 
}