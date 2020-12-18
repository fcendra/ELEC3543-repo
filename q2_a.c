/*
Assignment 1, ELEC3543 - Advanced Systems Programming
Question 2A
*/
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#define STDERR_FILENO 2

void err_sys(char *msg){
    int n =strlen(msg);

    if(write(STDERR_FILENO, msg, n) != n)
        exit(-1);
}
int main(void){
    if (open("tz_file", O_RDWR | O_CREAT | O_TRUNC) < 0)
    // if (open("tz_file", O_RDWR) < 0)
        err_sys("open error");
    // if (unlink("tz_file") < 0)
    //     err_sys("unlink error");

    printf("done\n");
    exit(0);
}

/*
what if "tz_file" is non-existent in the current directory and the first open function
is changed to if (open("tz_file", O_RDWR)< 0)
                    err_sys("open error");

moreover, explain why the above program simply opens a file then unlink it. What is the 
possible use for the above program


Answer:
The open() function creates and returns a new file descriptor for the corresponding filename.
the return value of open() is a file descriptor.
assume the "tz_file" is an non-existent directory, then if the first open function only has
one flag (i.e. O_RDWD, which is a flag for open the file for both reading and writing),
then it will result in error because there is no file to open (return -1).

It is basically acts as a delete file system where first it will check whether the file 
is exist or not in the corresponding directory, if it exists it will continue to the next 
function which is the unlink() where it will return 0 on succesfull completion (i.e. deletion)
and -1 if the unlink fucntion had an error. this program is useful to act as a delete file function
*/