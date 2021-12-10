"""
Main for load-PIA-IOI-alerts
"""

import sys
# Globals
fn = ""  # the filename we'll get from args'
# infile =  None	  # to hold the opened file
line_num = 0
buf = []
prev_line = 0
ra_args = [0,line_num, buf, prev_line]      # args for read_alert - file, line ct, buffer, prev_line position


def read_alert(ra_args):
    """
read_alert reads the lines in one alert
    @param ra_args:
    @type ra_args:  list
    @return: ra_args
    @rtype: list
    """
    alert_bufr = []
    for i in  range(50):
   # while True:     # Keep looping, exit by return
        ra_args[3] = ra_args[0].tell()   # get curr file position; to back up if it's the next header
        line = ra_args[0].readline()
        ra_args[1] += 1
        print(f"line in read_alert: {line} line_num: {ra_args[1] }")
        if 'Type' in line.strip():
            ra_args[2] = alert_bufr
            print(f">>>>alert_bufr: {alert_bufr} ra_args[2 {ra_args[2]}")
            ra_args[0].seek(ra_args[3])     # reset to prev line start pos
            return(ra_args)
        else:
            alert_bufr.append(line.strip())


def main():
    if len(sys.argv) > 1:
        fn= sys.argv[1]
        print(f"File {fn} will be processed")
        ra_args[0] = open(fn, 'r')
        for line in ra_args[0]:
            print(f"line in main: {line} line_num: {ra_args[1] }")

            if 'Type' in line.strip() and ra_args[1] == 0:    # First alert
                read_alert(ra_args)
                #print(f"Alert buffer: {ra_args[2]}")
            elif ra_args[1] > 0:
                read_alert(ra_args)
                print(f"Alert buffer: {ra_args[2]}")
    else:
        print(f"Enter file name to process")
        sys.exit(1)




if __name__ == '__main__':
    main()
