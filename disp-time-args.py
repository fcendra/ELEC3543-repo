import time
import sys
from time import asctime, gmtime

def check_argument(arg):
    try:
        arg_slice_0 = arg[0]
        arg_slice_1 = arg[1]
    except:
        return -1
    list_of_argument = ["h", "m", "t"]
    for i in list_of_argument:
        if (i  == arg_slice_1.lower() and arg_slice_0 == "-" and len(arg) == 2):
            return list_of_argument.index(i) 
    return -1

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid number of arguments !" + "\n" + "Usage : disp-time-args  <-H|-h|-M|-m|-T|-t>")
    else:
        print("Local time: " + str(int(time.time() / 60)) + " minutes since Jan. 1, 1970!" + "\n" +
                "Local date and time by ctime are: " + str(time.ctime()) + "\n")
        location_arg = check_argument(sys.argv[1])
        if location_arg == -1:
            print("Unknown argument !" + "\n" + "Usage : disp-time-args  <-H|-h|-M|-m|-T|-t>")
        else:
            locationDict = {0 : ["Hong Kong", 8], 1 : ["Madagascar", 3], 2 : ["Tasmania", 11]}
            corr_time = time.time() + (locationDict[location_arg][1] * 3600)
            str_modified_time = [str(gmtime(corr_time).tm_hour), str(gmtime(corr_time).tm_min)]
            for index in range(len(str_modified_time)):
                if (int(str_modified_time[index]) < 10):
                    str_modified_time[index] = "0" + str_modified_time[index]
            print("Time in " + locationDict[location_arg][0] + ":   " + str_modified_time[0] + ":" + str_modified_time[1] + 
                "\n" + "Date and time of the above time zone by asctime() are: " + asctime(gmtime(corr_time)))
        
