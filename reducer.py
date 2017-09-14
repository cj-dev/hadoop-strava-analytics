#!/bin/env python

import sys
import datetime
import time

current_day = ""
day_total_time = 0
day_total_entries = 0

def timestring_to_seconds(time):
    h, m, s = time.split(":")
    return int(h)*3600 + int(m)*60 + int(s)

for line in sys.stdin:
    key, elapsed_time = line.split()
    elapsed_seconds = timestring_to_seconds(elapsed_time)
    date, effort_id = key.split("#")

    if current_day == date:
        day_total_time += elapsed_seconds
        day_total_entries += 1
    else:
        if current_day:
            print(current_day, day_total_entries, day_total_time, day_total_time/day_total_entries)
        current_day = date
        day_total_time = elapsed_seconds
        day_total_entries = 1

print(current_day, day_total_entries, day_total_time, day_total_time/day_total_entries)
