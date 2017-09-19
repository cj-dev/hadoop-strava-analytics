# What it is

A prototype for practicing hadoop-y mapreduce fundamentals

# Usage
In general, start with some data (JSON, 1 object per line). In this case, use segment_efforts.py to get every attempt on a segment over the last year. This requires a strava API key (included with a free account).

Test using `cat <filename> | python mapper.py | python reducer.py`

Expected results are some data on stdout and maybe some visualizations.

Until I streamline a more handsome packaging method, numpy and python3 need to be installed on the hadoop nodes, system-wide.

Execute with hadoop using

```
<hadoop work dir>/bin/mapred streaming \
    -files <path to mapper.py>,<path to reducer.py>,<path to maths_util.py> \
    -mapper mapper.py -reducer reducer.py \
    -input <path to input json file> \
    -output <path to desired output dir>
```
