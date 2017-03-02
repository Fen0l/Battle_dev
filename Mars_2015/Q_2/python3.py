#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys, re

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    

valid_pwd = 0
for i in range(1, len(lines)):
	password = lines[i]

	if len(password) == 6 and re.match("[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{4}", password):
		valid_pwd += 1

print(valid_pwd)