"""
main module of load-PIA-IOI-alerts
Arguments
    fn : str
        filename of c&p from website
"""
import sys

# Globals
line_num = 0
alert_buf = []
prev_line = 0
wrk_list = []  # list to hold lines read from file for processing
ra_args = [0, line_num, alert_buf, wrk_list]     # args for read_alert - file, line ct, buffer, prev_line position

def process_alert(alert_buf):
    """
Process ONE alert
    @param alert_buf: collected lines for one alert
    @type alert_buf: list
    """
    print(f"Alert Bufr: {alert_buf}")


def parse_wrk_list(wrk_list):
    """
parse_wrk_list
    Understand alerts & create Alert objects
    Arguments
        wrk_list : list
            list containing the non-blank lines
    """
    # print(f"In parse_Wrk_list - wrk_list: {wrk_list}")
    # Find hdr lines
    hdr_line_indices = []
    for i, line in enumerate(wrk_list):     # Iterate wrk_list
        # print(f"\n line in parse_wrk_list: {line}")
        if "Type" in line:      #hdr of new alert
            hdr_line_indices.append(i)          # remember hdr indices
    print(f"\n hdr_line_indices: {hdr_line_indices}")
    alert_buf = []
    # Process alerts
    for i in hdr_line_indices:
        j = i + 1
        while "Type" not in wrk_list[j]:
            # print(f"wrk_list[j]: {wrk_list[j]}")
            alert_buf.append(wrk_list[j])
            j += 1
        process_alert(alert_buf)        # process one alert
        alert_buf = []


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
        parse_wrk_list(wrk_list)  # Understand alerts & create Alert objects
    else:
        print(f"Enter file name to process")
        sys.exit(1)

if __name__ == '__main__':
    main()
