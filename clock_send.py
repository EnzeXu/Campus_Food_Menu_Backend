# -*- coding: utf-8 -*-

import schedule
from utils import get_now_string, one_day_job
from notice import notice_hours, notice_minutes


def clock_send():
    print(get_now_string(), "[ ok ] Starting ...")
    for hour in notice_hours:
        for minute in notice_minutes:
            schedule.every().day.at("%02d:%02d" % (hour, minute)).do(one_day_job)
    print(get_now_string(), "[ ok ] Triggers at {0} : {1} every day".format(
        str(["%02d" % item for item in notice_hours]).replace("'", ""),
        str(["%02d" % item for item in notice_minutes]).replace("'", "")))
    while True:
        schedule.run_pending()


if __name__ == "__main__":
    clock_send()
    # now = datetime.datetime.now()  # + datetime.timedelta(hours=11)
    # time_hour = now.hour
    # time_minute = now.minute
    # print(type(time_hour), time_minute)
