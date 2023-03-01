void lock() {
	DisableInterrupts();
} 
void unlock() {
	EnableInterrupts();
}