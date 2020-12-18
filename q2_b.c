/*
Assignment 1, ELEC3543 - Advanced Systems Programming
Question 2B
*/
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define STDERR_FILENO 2

struct stat statbuf;

void err_sys(char *msg){
    int n =strlen(msg);

    if(write(STDERR_FILENO, msg, n) != n)
        exit(-1);
}
int main(void){
    
    if (open("tz_file", O_RDWR | O_CREAT | O_TRUNC) < 0)
        err_sys("open error");

    if (chmod("tz_file", S_IRUSR | S_IWUSR | S_IXUSR | S_IWGRP | S_IXGRP | S_IROTH | S_IWOTH ) < 0)
		perror("chmod error for tz_file"); // check fromm left most side to right most whether flag return error, if all error, return error message

      /* get the stat record of the file "tz_file" */
	if (stat("tz_file", &statbuf) < 0)
		perror("stat error for tz_file");

	if (chmod("tz_file", (statbuf.st_mode & ~S_IXGRP)) < 0)
		perror("chmod error for tz_file");

	printf("done\n");

    return 0;
}
/*
rm -f tz_file is to try to remove the "tz_file" directory
ls -al tz_file shows the file inside the directory with its corresponding file permissions
*/
