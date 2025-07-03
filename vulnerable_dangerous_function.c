#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {
    char buffer[50];
    
    srand(time(0));
    
    int luckyNumber = rand() % 100 + 1;
    
    sprintf(buffer, "Your lucky number is %d", luckyNumber);
    
    printf("%s\n", buffer);
    
    return 0;

}