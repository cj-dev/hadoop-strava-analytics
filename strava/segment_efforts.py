#!/bin/env python
import stravalib
import datetime
import json
import sys

ACCESS_TOKEN=""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Requires a segment ID to query")
        exit(1)

    if not ACCESS_TOKEN:
        print("Provide an ACCESS_TOKEN")
        exit(0)

    segment_id = sys.argv[1]
    client = stravalib.Client(access_token=ACCESS_TOKEN)
    segment = client.get_segment(segment_id)
    upper_date_limit = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    lower_date_limit = upper_date_limit - datetime.timedelta(days=365)
    print("Querying efforts for {0}".format(segment.name))
    efforts = client.get_segment_efforts(segment_id,
            start_date_local=lower_date_limit,
            end_date_local=upper_date_limit)

    filename = 'results-{0}.json'.format(segment_id)
    with open(filename, 'w') as result_file:
        for e in efforts:
            effort_dict = {
                    "name": e.name,
                    "segment_id": e.segment.id,
                    "activity_id": e.activity.id,
                    "athlete_id": e.athlete.id,
                    "kom_rank": e.kom_rank,
                    "pr_rank": e.pr_rank,
                    "moving_time": str(e.moving_time),
                    "elapsed_time": str(e.elapsed_time),
                    "start_date": str(e.start_date),
                    "start_date_local": str(e.start_date_local),
                    "distance": e.distance.num,
                    "average_watts": e.average_watts,
                    "device_watts": e.device_watts,
                    "average_heartrate": e.average_heartrate,
                    "max_heartrate": e.max_heartrate,
                    "average_cadence": e.average_cadence,
                    "start_index": e.start_index,
                    "end_index": e.end_index,
            }
            json_line = json.dumps(effort_dict)
            print(json_line, file=result_file)
    print("Wrote efforts to {0}".format(filename))
