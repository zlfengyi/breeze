#include <stdlib.h>
#include <stdio.h>

int main() {
	FILE* file = fopen("test.lpcm", "wb");
	int i;
	for (i = 0; i < 10; i++) {
		fprintf(file, "hehe\n");
		usleep(1000 * 1000);
		printf("%d\n", i);
	}
	fclose(file);
}