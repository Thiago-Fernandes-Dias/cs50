#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

int main(void) {
    char *username = NULL;
    size_t size = 0;
    ssize_t len;
    printf("What's your name? ");
    len = getline(&username, &size, stdin);
    if (len == -1) {
        printf("Failed to read line\n");
        return 1;
    }
    username[len - 1] = '\0';
    printf("Hello, %s!\n", username);
    printf("Looks like your name have %li characters.\n", len - 1);
    free(username);
    return 0;
}