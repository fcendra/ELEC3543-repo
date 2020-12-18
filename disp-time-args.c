#include <stdio.h>
#include <time.h>
#include <string.h>
#define MAX_BUF_SZ 80

int argument_check(int argc, char* argv[]){
	const char *a[6];
	a[0] = "-h"; a[1] = "-H"; a[2] = "-m"; a[3] = "-M"; a[4] = "-t"; a[5] = "-T";
	for (size_t i = 0; i < 6 ; ++i){
		if(strcmp(argv[1], a[i]) == 0){
			if (i % 2 == 0) return i;
			else return i - 1;
		}
	}
	return -1;
}

int main(int argc, char *argv[]) {
	time_t         x;
	struct tm      *tm_ptr;
	char           buf[MAX_BUF_SZ];
	if (argc != 2){printf("Invalid number of arguments !\nUsage : disp-time-args  <-H|-h|-M|-m|-T|-t>");}
	else {
		time(&x);
		printf("Local time: %ld minutes since Jan. 1, 1970!\n", (int)x / 60); 
		strftime(buf, MAX_BUF_SZ, "%c", localtime(&x));
		printf("Local date and time by ctime() are: %s \n\n", buf);
		if (argument_check(argc, argv) == -1){printf("Unknown argument !\nUsage : disp-time-args  <-H|-h|-M|-m|-T|-t>");}
		else{
			int location_number = argument_check(argc, argv);
			int time_zone[5];
			const char *location[5];
			time_zone[0] = 8; time_zone[2] = 3; time_zone[4] = 11;
			location[0] = "Hong Kong"; location[2] = "Madagascar"; location[4] = "Tasmania";
			x = x + (time_zone[location_number] * 3600);
			tm_ptr = gmtime(&x);
			printf("Time in %s:   %02d:%02d \nDate and time of the above time zone by asctime() are: %s", 
				location[location_number], (tm_ptr->tm_hour), tm_ptr->tm_min, asctime(tm_ptr));
		}
	}
	return 0;
}