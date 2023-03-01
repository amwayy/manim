int buffer[MAX];
int fill = 0;
int use = 0;
int count = 0;

void put(int value) {
	buffer[fill] = value;
	fill = (fill + 1) % MAX;
	count++;
}

int get() {
	int tmp = buffer[use];
	use = (use + 1) % MAX;
	count--;
	return tmp;
}