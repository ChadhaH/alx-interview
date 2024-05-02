#!/usr/bin/python3
"""
	 reads stdin line by line and computes metrics
"""


import sys

code_stats = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
sizes = 0
i = 0

try:
    for row in sys.stdin:
	row_l = row.split(" ")
	if len(row_l) > 4:
            cd = row_l[-2]
	    size = int(row_l[-1])
	    if cd in code_stats.keys():
	        code_stats[cd] += 1
	    sizes += size
	    i += 1

        if i == 10:
            i = 0
	    print('File size: {}'.format(sizes))
	    for k, v in sorted(code_stats.items()):
	        if v != 0:
		    print('{}: {}'.format(k, v))

except Exception as error:
    pass

finally:
    print('File size: {}'.format(sizes))
    for k, v in sorted(code_stats.items()):
	if v != 0:
	    print('{}: {}'.format(k,v))
