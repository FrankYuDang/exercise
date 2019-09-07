#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	char first[255], last[255];
	
	printf("Enter your first name: ");
	fgets(first, 255, stdin);
	first[strlen(name) - 1] = '\0'; /* remove the newline at the end*/
	
	printf("Now enter your last name: "); /* debug line */
	gets(last); /* buffer overflow? what's that*/
	
	Printf("Hello %s %s!\n", first, last);
	return 0;
}