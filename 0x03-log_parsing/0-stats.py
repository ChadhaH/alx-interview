#!/usr/bin/python3
'''a script that reads stdin row by row and computes metrics'''


import sys

cd_stats = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
sizes = 0
i = 0

try:
    for row in sys.stdin:
        row_list = row.split(" ")
        if len(row_list) > 4:
            cd = row_list[-2]
            size = int(row_list[-1])
            if cd in cd_stats.keys():
                cd_stats[cd] += 1
            sizes += size
            i += 1

        if i == 10:
            i = 0
            print('File size: {}'.format(sizes))
            for k, v in sorted(cd_stats.items()):
                if v != 0:
                    print('{}: {}'.format(k, v))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(sizes))
    for k, v in sorted(cd_stats.items()):
        if v != 0:
            print('{}: {}'.format(k, v))
