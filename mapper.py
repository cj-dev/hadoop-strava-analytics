#!/bin/env python

import sys
import datetime
import json

for line in sys.stdin:
    line = line.strip()
    effort = json.loads(line)
    date_string = effort['start_date'].split(" ")[0]
    activity_id = effort['activity_id']
    elapsed_time = effort['elapsed_time']
    if len(elapsed_time.split(":")[0]) < 2: # zero-pad the hour
        elapsed_time = "0" + elapsed_time

    print("{0}#{1}".format(date_string, activity_id), elapsed_time)

