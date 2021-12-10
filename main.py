"""
main module of load-PIA-IOI-alerts
Arguments
    fn : str
        filename of c&p from website
"""
import sys

# Globals
line_num = 0
buf = []
prev_line = 0
ra_args = [0, line_num, buf, prev_line]  # args for read_alert - file, line ct, buffer, prev_line position
wrk_list = []  # list to hold lines read from file for processing

def parse_wrk_list():
    """
parse_wrk_list
    Understand alerts & create Alert objects
    Arguments
        ra_args : list
            file, line ct, buffer, prev_line position
    """
    pass


def main():
    if len(sys.argv) > 1:
        fn = sys.argv[1]
        print(f"File {fn} will be processed")
        ra_args[0] = open(fn, 'r')

        for line in ra_args[0]:
            wrk_line = line.strip()  # git rid of nl
            if wrk_line != '':  # skip blank lines
                wrk_list.append(wrk_line)
        print(f"\n wrk_list: {wrk_list}")
        parse_wrk_list()  # Understand alerts & create Alert objects
    else:
        print(f"Enter file name to process")
        sys.exit(1)

if __name__ == '__main__':
    main()
