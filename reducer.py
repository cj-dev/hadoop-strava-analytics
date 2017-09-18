#!/bin/env python

import sys
import datetime
import time

import maths_util

def summarize_day_efforts(date, efforts, plot=False):
    print(date,
            len(efforts),
            sum(efforts.values()),
            sum(efforts.values())/len(efforts))
    if plot:
        maths_util.plot_1d(date, efforts)

def summarize_timerange(summaries, plot=False):
    print("From date {begin} to {end}".format(
        begin=list(summaries.keys())[0], end=list(summaries.keys())[-1]))
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
    date, effort_id = key.split("#")

    if current_day == date:
        day_efforts[effort_id] = elapsed_seconds
    else:
        if current_day:
            filtered_efforts = maths_util.filter_outliers_iqr(day_efforts)
            summaries[date] = sum(filtered_efforts.values())/len(filtered_efforts)
        current_day = date
        day_efforts = {}

summarize_timerange(summaries, plot=True)

