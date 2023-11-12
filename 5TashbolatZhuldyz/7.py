zh,ts = input().split()
zh,ts = int(zh),int(ts)
for i in range (zh):#include <stdio.h>
#include <string.h>

int main() {
    char path[1024];
    scanf("%s", path);

    int i = 0;
    int j = 0;
    int len = strlen(path);
    while (i < len) {
        if (path[i] == '/') {
            while (path[i] == '/' && i < len) {
                i++;
            }
        } else {
            path[j++] = path[i++];
        }
    }
    if (j > 0 && path[j-1] != '/') {
        path[j++] = '/';
    }
    path[j] = '\0';

    printf("Normalized path: %s\n", path);
    return 0;
}