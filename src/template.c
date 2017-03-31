#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <errno.h>

int file_is_readable(char *filename) {
    if ( access(filename, R_OK) != -1 ) {
        return 1;
    } else {
        return 0;
    }
}

int main(int argc, char *argv[]) {
    clock_t t0, t1;

    if (argc <= 1) {
        printf("Usage: %s [arguments]\n", argv[0]);
         return EXIT_FAILURE;
    }

    t0 = clock();
    printf("Hello World!\n");
    if (file_is_readable(argv[1])) {
        printf("Input File = '%s'\n", argv[1]);
    } else {
        printf("Input File = '%s' (file does not exist or read permissions absent)\n", argv[1]);
    }
    t1 = clock();
    printf("Time elapsed = %f (ms)\n", (t1-t0)*1000/(double)CLOCKS_PER_SEC );
    return EXIT_SUCCESS;
}
