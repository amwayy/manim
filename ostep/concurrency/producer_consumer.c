cond_t cond;
mutex_t mutex;

void *producer(void *arg) {
	int i;
	for (i = 0; i < loops; i++) {
		Pthread_mutex_lock(&mutex);
		if (count == 1)
			Pthread_cond_wait(&cond, &mutex);
		put(i);
		Pthread_cond_signal(&cond);
		Pthread_mutex_unlock(&mutex);
	}
}

void *consumer(void *arg) {
int i;
for (i = 0; i < loops; i++) {
	Pthread_mutex_lock(&mutex);
	if (count == 0)
		Pthread_cond_wait(&cond, &mutex);
	int tmp = get();
	Pthread_cond_signal(&cond);
	Pthread_mutex_unlock(&mutex);
	printf("%d\n", tmp);
	}
}