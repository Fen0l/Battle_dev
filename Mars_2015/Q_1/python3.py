#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

for i in range(1, len(lines)):
	year = int(lines[i])

	if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
		print("BISSEXTILE")
	else:
		print("NON BISSEXTILE")
