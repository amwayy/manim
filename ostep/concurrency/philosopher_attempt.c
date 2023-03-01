int left(int p) {
	return p; }
int right(int p) {
	return (p + 1) % 5; }

void getchops() {
	sem_wait(chops[left(p)]);
	sem_wait(chops[right(p)]);
}

void putforks() {
	sem_post(chops[left(p)]);
	sem_post(chops[right(p)]);
}