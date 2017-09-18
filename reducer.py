#!/bin/env python

import sys
import datetime
import time

from matplotlib import pyplot
from matplotlib import dates as ppdates
import numpy

def timestring_to_seconds(time):
    h, m, s = time.split(":")
    return int(h)*3600 + int(m)*60 + int(s)

def plot_1d(date, efforts):
    times = list(efforts.values())
    pyplot.plot(times,
            numpy.zeros_like(times),
            "x"
    )
    pyplot.suptitle("Efforts on {date}".format(date=date))
    pyplot.show()

def plot_2d(summaries):
    dates = [ppdates.datestr2num(date) for date in summaries.keys()]
    averages = list(summaries.values())
    pyplot.plot(dates,
            averages
            )
    pyplot.show()

def filter_outliers_iqr(efforts):
    times = list(efforts.values())
    q25, q75 = numpy.percentile(times, [25, 75])
    iqr = q75 - q25

    filtered = {}
    for e_id, time in efforts.items():
        if time > q25 - 1.5*iqr and time < q75 + 1.5*iqr:
            filtered[e_id] = time
        # else:
        #     print("Filtered item {e_id} for time of {time}".format(
        #         e_id=e_id, time=time))

    return filtered

def filter_outliers_distance(efforts):
    pass

def summarize_day_efforts(date, efforts, plot=False):
    print(date,
            len(efforts),
            sum(efforts.values()),
            sum(efforts.values())/len(efforts))
    if plot:
        plot_1d(date, efforts)

def summarize_timerange(summaries, plot=False):
    print("From date {begin} to {end}".format(
        begin=list(summaries.keys())[0], end=list(summaries.keys())[-1]))
    for date, average in summaries.items():
        print(date, average)
    if plot:
        plot_2d(summaries)

current_day = ""
day_efforts = {}
summaries = {}

for line in sys.stdin:
    key, elapsed_time = line.split()
    elapsed_seconds = timestring_to_seconds(elapsed_time)
    date, effort_id = key.split("#")

    if current_day == date:
        day_efforts[effort_id] = elapsed_seconds
    else:
        if current_day:
            filtered_efforts = filter_outliers_iqr(day_efforts)
            summaries[date] = sum(filtered_efforts.values())/len(filtered_efforts)
        current_day = date
        day_efforts = {}

summarize_timerange(summaries, plot=True)

