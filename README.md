# load-PIA-IOI-alerts
## Load PIA &amp; IOI alerts into spreadshet for tracking
Receive alerts from Profits Run on Mon (PIA) and Thur(IOI)
They are in a spreadsheet (sortof) and are OK to read but not usable
to load into a spreadsheet for tracking.

## Approach
  - C&P to txt file giving - see file pro-spec/alert.txt -
  - Read the txt file
  - The "Type	Symbol	Option" header marks a new alert (there can be
  - several)
  - Parse alert in Alert class

## Design 
OK, reset! Need to back up a line when the inner loop finds a header
That doesn't work "oserror-telling-position-disabled-by-next-call-error"
So, 
  1) Read whole mess into list
     1) Throw away blank lines
  2) Then do same as now, but operating on the list, so backing up isn't 
an issue
