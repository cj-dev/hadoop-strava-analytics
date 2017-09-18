from matplotlib import pyplot
from matplotlib import dates as ppdates
import numpy

def timestring_to_seconds(time):
    h, m, s = time.split(":")
    return int(h)*3600 + int(m)*60 + int(s)

def plot_1d(efforts, date=None):
    times = list(efforts.values())
    pyplot.plot(times,
            numpy.zeros_like(times),
            "x"
    )
    pyplot.suptitle("Efforts on {date}".format(date=date if date else "Some day"))
    pyplot.show()

def plot_2d(summaries):
    dates = list(summaries.keys())
    values = list(summaries.values())
    pyplot.gca().xaxis.set_major_formatter(ppdates.DateFormatter('%m/%d/%Y'))
    pyplot.gca().xaxis.set_major_locator(ppdates.DayLocator())
    pyplot.plot(dates,
            values
            )
    pyplot.gcf().autofmt_xdate()
    pyplot.show()

def filter_outliers_iqr(efforts):
    times = list(efforts.values())
    q25, q75 = numpy.percentile(times, [25, 75])
    iqr = q75 - q25

    filtered = {}
    for e_id, time in efforts.items():
        if time >= q25 - 1.5*iqr and time <= q75 + 1.5*iqr:
            filtered[e_id] = time
        # else:
        #     print("Filtered item {e_id} for time of {time}".format(
        #         e_id=e_id, time=time))

    return filtered

def filter_outliers_distance(efforts):
    pass


