#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys, os, re

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

def getMaxLen(aList):
	if aList:
		return max(len(l) for l in aList)
	else:
		return 0

def getLowerWord(aList):
	if aList:
		return min(l for l in aList)
	else:
		return None

def longest_common_substring(s1, s2):
	m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]

	longest, x_longest = 0, 0

	all_goods = []
	for x in range(1, 1 + len(s1)):
		for y in range(1, 1 + len(s2)):
			if s1[x - 1] == s2[y - 1]:
				m[x][y] = m[x - 1][y - 1] + 1
				if m[x][y] >= longest:
					simillar = s1[x - m[x][y]: x]
					if(len(simillar) > getMaxLen(all_goods)):
						all_goods = []

					if(len(simillar) >= getMaxLen(all_goods)):
						all_goods.append(simillar)
				else:
					m[x][y] = 0

	if(getLowerWord(all_goods)):
		print(getLowerWord(all_goods))
	else:
		print("AUCUN FACTEUR")	




for i in range(1, len(lines)):
	chars = lines[i].split(" ")
	word_1 = chars[0]
	word_2 = chars[1]

	longest_common_substring(word_1, word_2)
