#!/bin/env python

import sys
import datetime
import time

import maths_util
from statistics import median

def summarize_day_efforts(efforts, date=None, plot=False):
    print("{date}: {num_efforts} with median elapsed time {median}".format(
            date=date if date else "",
            num_efforts=len(efforts),
            median=median(list(efforts.values()))))
    if plot:
        maths_util.plot_1d(efforts, date)

def summarize_timerange(summaries, plot=False):
    for date, average in summaries.items():
        print(date, average)
    if plot:
        maths_util.plot_2d(summaries)

current_day = ""
day_efforts = {}
summaries = {}

for line in sys.stdin:
    key, elapsed_time = line.split()
    elapsed_seconds = maths_util.timestring_to_seconds(elapsed_time)
    date_str, effort_id = key.split("#")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    if current_day == date:
        day_efforts[effort_id] = elapsed_seconds
    else:
        if current_day:
            filtered_efforts = maths_util.filter_outliers_iqr(day_efforts)
            summaries[date] = median(list(filtered_efforts.values()))
        current_day = date
        day_efforts = {}

summarize_timerange(summaries, plot=False)

