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

    print("{0}-{1}".format(date_string, activity_id), elapsed_time)

