import requests
import re
import time
import json
import os
import pickle
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

# from baidu_api import baidu_translate
# from mail import Mail
# from strings import *
from const import *
from get_cookie import get_cookie
import pytz
import logging
# from pretty_html_table import build_table


# def now_time_string(string_format="%Y-%m-%d %H:%M:%S"):
#     return stamp_to_string(time.time(), string_format)


def get_now_string(time_string="%Y%m%d_%H%M%S_%f"):
    # return datetime.datetime.now().strftime(time_string)
    est = pytz.timezone('America/New_York')

    # Get the current time in UTC and convert it to EST
    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    est_now = utc_now.astimezone(est)

    # Return the time in the desired format
    return est_now.strftime(time_string)

def http_get(cookie, url):
    # url = f"https://williamandmary.campusdish.com/api/menu/GetMenus?locationId=78391&mode=Daily&date={date}&periodId={periodId}"
    # url = f"https://williamandmary.campusdish.com/api/menu/GetMenuPeriods?locationId=78391&storeId=&date={date}&mode=Daily"
    logging.basicConfig(filename="./saves/logs.log", filemode="a", level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    headers = {
        # 'Content-Type': 'application/x-www-form-urlencoded',
        "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "Referer": "https://williamandmary.campusdish.com/LocationsAndMenus/FoodHallSadler",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        # "Cookie": "visid_incap_2829404=lWY16Y6USw6KfeLBPVa5kdxU5WUAAAAAQUIPAAAAAACq4USWD3LleZAx9Qu9PoYc; incap_ses_1544_2829404=lJyUDcj8y0oY2mQod2RtFdxU5WUAAAAAE5o5dOcbVuCAq6MPZfN8AQ==; shell#lang=en; AramarkContextInfo=9739|{53f130c4-cd67-4cf8-8db4-50b089c478de}|Higher Education; __CLAnonymousUser=024h/Ijtl3AEk0a/msuDIuvCQ==2WGg6NA8lpDjEpqCFh2DlwzIbqiRtwjZd2OMH4+3q/pg/BJ5ppkX00CjjIDW7LzPwPw4mwjB0clcKkNHk5OmGGkhC4MkivZzb6XYtSfETPOkSxciTYVXTFTdVW+FA5et09MESW4iwCC9lHIqMrz9hsf8HJ9vQkP05wX800WsZ8wqLbz5C46rvBO/VGJsfx3pm16/UJU0lCu45r/h+ZpyhfnFAa0Msi2rSaDqe2Y6tYBfjATgzJAd5HAiJp+cB7nevDSND0HJMuA97WSvp+qCLI0/DZBNfpkPlNs938dbDcCp9yusghwFMf3JWRfV5noY/f7ed1+W2lzMWgiBmen/kejs8CdgX7zaqiKix3HanBKakJe8Bz0TEj5R56kkRB1IXB3QyJJDoc3WMW9TzcZevBG3ejjr2PBrQgBv3DYKYGn40Dg0MzJawD2ixIED3aDqtfmMHuqsLpLV3aa3DQ5xrW0l4ZIb1PCUYzaFRgJLzyFBVWppfjklYlG14Rl/EBNSM/yxnVmn0/9Jv1WilnBWuLaPx65TiU9aUF34fgs5GK43AXKUUV2u24F60L3eUSV53tzmr0ethIAvcSLGsm6yTq5oKkuRmbD5t/H4Sjo+MPoKLUYqaJybihP3Hme2z8pZ9qkNol+fOawW6Oy2xo+9/j6PtIoQMsCdTuoXV6MKpTXf0l/l9Y7JuRGKuAgLN2h/brcMwmxj9dXeaGq/5iX7mposvNye6ZrXK5xY+HH8CgYC7WwLNdtCZY1GArVsQVncG992RgmB/koktTq37oc3lMz7jjJo7/SajvHdYqpvPZA=; IsShownMailSubscriptionWidget=1; _ga=GA1.1.1554382821.1709528286; _fbp=fb.1.1709528286303.880731857; OptanonAlertBoxClosed=2024-03-04T04:58:09.094Z; _ga_4PWL0638HD=GS1.1.1709528286.1.1.1709528300.46.0.0; _ga_30LZ5B848R=GS1.1.1709528286.1.1.1709528300.46.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Mar+03+2024+23%3A58%3A20+GMT-0500+(Eastern+Standard+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=8ef42c1f-5517-4021-9a7e-9c1aefef645d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=US%3BVA&AwaitingReconsent=false",
        "Cookie": cookie,
    }
    params = {}# 'date': date
    logging.info(url)
    data = requests.get(url, params=params, headers=headers, timeout=30)
    return data.text



def get_new_cookie(url):
    # Send a request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Return the cookies received from the server
        return response.cookies
    else:
        # Handle error if the request was not successful
        return f"Error: Received response code {response.status_code}"


# def translate_one_dish(string):
#     baidu_return = baidu_translate(string)
#     if len(baidu_return) == 0:
#         res = "FAILED TO TRANSLATE"
#     elif "dst" in baidu_return[0]:
#         res = baidu_return[0]["dst"]
#     else:
#         res = "FAILED TO TRANSLATE"
#     return "{} ({})".format(string, res)


# class MyTranslate:
#     def __init__(self):
#         self.count = 0
#
#     def translate(self, string):
#         self.count += len(string)
#         return translate_one_dish(string)


# def get_menu(date, save_flag=True):
#     save_full_time = stamp_to_string(time.time(), "%Y%m%d%H%M%S")
#     text = http_get(date)
#     soup = BeautifulSoup(text, "lxml")
#     period_names = soup.find_all("div", {"class": "c-tabs-nav__link-inner"})
#     period_names = [item.text for item in period_names]
#     # print(data)
#     data_dic = dict()
#     data_concerned_dic = dict()
#     data_concerned_dic["Lunch"] = dict()
#     data_concerned_dic["Dinner"] = dict()
#
#     periods = soup.find_all("div", {"class": "c-tab__content"})
#     # assert len(periods) == 4
#     word_count = 0
#     word_count_need = 0
#     for i in range(len(periods)):
#         period_dic = dict()
#         # print()
#         # print(tabs[i])
#         blocks = periods[i].find_all("h4", {"class": "toggle-menu-station-data"})
#         block_names = [item.text for item in blocks]
#         # print(len(blocks))
#         # print(blocks)
#         block_texts = periods[i].find_all("div", id=re.compile('^menu-station-data-'))
#         # print(len(block_texts))
#         assert len(blocks) == len(block_texts)
#
#         # print(block_texts)
#         # block_names = [item.text for item in blocks]
#         # print(periods[i].text)
#         for j in range(len(block_texts)):
#             dishes = block_texts[j].find_all("a", {"tabindex": "0"})
#             dishes = [item.text for item in dishes]
#             for item in dishes:
#                 word_count += len(item)
#             if ("LUNCH" in period_names[i] or "LATE BRUNCH" in period_names[i]) and block_names[j].lower() in CONCERNED_STATION_LIST:
#                 for item in dishes:
#                     word_count_need += len(item)
#                 # if translate_flag:
#                 #     dishes = ["{}({})".format(item, baidu_translate(item)[0]["dst"]) for item in dishes]
#                 data_concerned_dic["Lunch"][block_names[j]] = dishes
#             elif ("DINNER" in period_names[i]) and block_names[j].lower() in CONCERNED_STATION_LIST:
#                 for item in dishes:
#                     word_count_need += len(item)
#                 # if translate_flag:
#                 #     dishes = ["{}({})".format(item, baidu_translate(item)[0]["dst"]) for item in dishes]
#                 data_concerned_dic["Dinner"][block_names[j]] = dishes
#             period_dic[block_names[j]] = {
#                 "station": block_names[j],
#                 "dish_num": len(dishes),
#                 "dishes": list(dishes)
#             }
#         data_dic[period_names[i]] = {
#             "period": period_names[i],
#             "station_num": len(blocks),
#             "station_menu": period_dic
#         }
#     dic = {
#         "date": date,
#         "word_count": word_count,
#         "word_count_concerned": word_count_need,
#         "data": data_dic,
#         "data_concerned": data_concerned_dic
#     }
#     # print(json.dumps(dic, indent=4, ensure_ascii=False))
#     if save_flag and dic["word_count"] > 10:
#         folder_path = "saves/{}".format(date)
#         if not os.path.exists(folder_path):
#             os.makedirs(folder_path)
#         target_path = "saves/{}/{}_{}.pkl".format(date, date, save_full_time)
#         with open(target_path, "wb") as f:
#             pickle.dump(dic, f)
#     match_flag = False
#     match_reason_list_lunch = []
#     match_reason_list_dinner = []
#     for period_key in dic["data_concerned"]:
#         for station_key in dic["data_concerned"][period_key]:
#             for one_dish in dic["data_concerned"][period_key][station_key]:
#                 for one_word in CONCERNED_DISH_KEYWORD_LIST:
#                     if one_word.lower() in one_dish.lower():
#                         match_flag = True
#                         if period_key == "Lunch":
#                             match_reason_list_lunch.append("{}".format(one_dish))
#                         elif period_key == "Dinner":
#                             match_reason_list_dinner.append("{}".format(one_dish))
#     return dic, match_flag, [match_reason_list_lunch, match_reason_list_dinner]


def stamp_to_string(stamp, string_format="%Y-%m-%d %H:%M"):
    return time.strftime(string_format, time.localtime(stamp))


def get_week_day(string, string_format="%Y-%m-%d"):
    return datetime.datetime.fromtimestamp(time.mktime(time.strptime(string, string_format))).isoweekday()


def get_week_day_name(string, string_format="%Y-%m-%d"):
    day = get_week_day(string, string_format="%Y-%m-%d")
    day_name_dic = {
        1: "Mon",
        2: "Tue",
        3: "Wed",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun"
    }
    return day_name_dic[day]


# def daily_job():
#     time_stamp = time.time()
#     today_date = stamp_to_string(time_stamp, "%Y-%m-%d")
#
#     df_date = []
#     df_day = []
#     df_match = []
#     df_match_reason_lunch = []
#     df_match_reason_dinner = []
#     mt = MyTranslate()
#     dic_list = []
#     while True:
#         new_date = stamp_to_string(time_stamp, "%Y-%m-%d")
#         menu_dic, match_flag, match_reason = get_menu(new_date)
#         # print("{}: \"{}\", \"{}\"".format(new_date, match_flag, match_reason))
#         dic_list.append(menu_dic)
#         if menu_dic["word_count"] <= 10:
#             break
#         df_date = df_date + [new_date]
#         df_day = df_day + [get_week_day_name(new_date)]
#         df_match = df_match + (["Yes"] if match_flag else ["No"])
#         new_lunch = match_reason[0]
#         new_lunch = [mt.translate(item) for item in new_lunch]
#         new_dinner = match_reason[1]
#         new_dinner = [mt.translate(item) for item in new_dinner]
#         df_match_reason_lunch = df_match_reason_lunch + (["[br]".join(new_lunch)] if len(match_reason[0]) > 0 else [""])
#         df_match_reason_dinner = df_match_reason_dinner + (["[br]".join(new_dinner)] if len(match_reason[1]) > 0 else [""])
#         time_stamp += 86400
#     # print(df_date)
#     # print(df_match)
#     # print(df_match_reason_lunch)
#     # print(df_match_reason_dinner)
#     df = pd.DataFrame()
#     df["Date"] = df_date
#     df["Day"] = df_day
#     df["Match"] = df_match
#     df["Lunch"] = df_match_reason_lunch
#     df["Dinner"] = df_match_reason_dinner
#     df.reset_index(drop=True, inplace=True)
#     df.index += 1
#
#     df_today_lunch = pd.DataFrame()
#     lunch_list_dic = dict()
#     for station_key in dic_list[0]["data_concerned"]["Lunch"]:
#         station_dishes = dic_list[0]["data_concerned"]["Lunch"][station_key]
#         station_dishes = [mt.translate(item) for item in station_dishes]
#         lunch_list_dic[station_key] = station_dishes
#     lunch_list_max = max([len(lunch_list_dic[one_key]) for one_key in lunch_list_dic])
#     # print("lunch_list_max:", lunch_list_max)
#     # print(lunch_list_dic)
#     for one_key in lunch_list_dic:
#         df_today_lunch[one_key] = lunch_list_dic[one_key] + [""] * (lunch_list_max - len(lunch_list_dic[one_key]))
#     df_today_lunch.reset_index(drop=True, inplace=True)
#     df_today_lunch.index += 1
#
#     df_today_dinner = pd.DataFrame()
#     dinner_list_dic = dict()
#     for station_key in dic_list[0]["data_concerned"]["Dinner"]:
#         station_dishes = dic_list[0]["data_concerned"]["Dinner"][station_key]
#         station_dishes = [mt.translate(item) for item in station_dishes]
#         dinner_list_dic[station_key] = station_dishes
#     dinner_list_max = max([len(dinner_list_dic[one_key]) for one_key in dinner_list_dic])
#     # print("dinner_list_max:", lunch_list_max)
#     # print(dinner_list_dic)
#     for one_key in dinner_list_dic:
#         df_today_dinner[one_key] = dinner_list_dic[one_key] + [""] * (dinner_list_max - len(dinner_list_dic[one_key]))
#     df_today_dinner.reset_index(drop=True, inplace=True)
#     df_today_dinner.index += 1
#
#     mail = Mail()
#     to_receivers = ["xue20@wfu.edu"]  # ["zhanj318@wfu.edu"]
#     bcc_receivers = ["jiaol20@wfu.edu", "xuz218@wfu.edu", "zhuy319@wfu.edu", "sunz19@wfu.edu", "lij520@wfu.edu", "chenj322@wfu.edu"] # "zhanj318@wfu.edu"
#     mail.set_receivers(to_receivers, [], bcc_receivers)
#     content_html = STRING_MAIL_TEXT_HEAD + STRING_MAIL_TEXT_TITLE.format(today_date)
#     content_html += STRING_MAIL_TEXT_PART_NONE_BLUE.format(
#         "Calendar",
#         build_table(df, 'blue_light')  #df.to_html().replace(" style=\"text-align: right;\"", "")
#     ).replace("[br]", "<br>")
#     content_html += STRING_MAIL_TEXT_README.format(
#         "Keywords: {}".format(str(CONCERNED_DISH_KEYWORD_LIST)),
#         "Station Interest: {}".format(str(CONCERNED_STATION_LIST)),
#         "Translation Cost: {} characters".format(mt.count),
#     )
#     content_html += STRING_MAIL_TEXT_PART_NONE_RED.format(
#         "Today Menu - Lunch",
#         build_table(df_today_lunch, 'red_light')  # df_today_lunch.to_html().replace(" style=\"text-align: right;\"", "")
#     )
#     content_html += STRING_MAIL_TEXT_PART_NONE_RED.format(
#         "Today Menu - Dinner",
#         build_table(df_today_dinner, 'red_light')  # df_today_dinner.to_html().replace(" style=\"text-align: right;\"", "")
#     )
#
#     content_html += STRING_MAIL_TEXT_TAIL
#     # print(content_html)
#     mail.send(content_html, [], "PIT Daily [{}] - Today [{}]".format(today_date, df_match[0]), "html")
#     print(now_time_string(), "[ ok ] Finished")

def get_available_date_list(cookie):
    # cookie = "shell#lang=en; AramarkContextInfo=9739|{53f130c4-cd67-4cf8-8db4-50b089c478de}|Higher Education; IsShownMailSubscriptionWidget=1; visid_incap_2829404=u/xy2pfyRByH54zO5BAB2Z6MBWYAAAAAQUIPAAAAAACnuHw9DFOlK4XjgDG2Foh2; _fbp=fb.1.1711639713005.1525317211; _ga=GA1.1.569354958.1711639713; __CLAnonymousUser=0242QPkJrIEuj+vnob75AR5KQ==dkFHCnvN+2JPtTihU+jolUBxCPPOd5CRbprDOTVYM3sTtmu82O0jkgMLIE8H+1kOY4L6LvllrbRW2xchagUz16vRWbyYyEP/XVW2pcTHBLQ9/+1d5BdQ1hEfTGI7IEb2KwF/0jfJRRtyGrinWaYkOn40pnEgS+D2bHoDnnnT095OY4b862zb40L9farexV7DQ8+39peJC9bdz6VLfOQ/zOS70NpRhn5YbLeFgxeA9E0j+4eGtTyKF4VpE3lX35Jxa7eiK3JypVXgmDNaMzhFsPnfZrRG7EyCqPfdmZ4syBu5u2Yq1vo8eEgeeTePzFoqIUggC4fF5T0p6OSm3sSh6Wi2VD0lWXkMlXfw2pOnO6+UXcvGA0cBAAgFTVmHccucMeRj2P3Msl1FSJUJAQyz3EiMRuZTjlolBzMznvXuiwbUrkTmEZ3wDhItD3dqody65AgcE4jRt3lUBkLF3ME482m+BmW9dF0C478dZ8Bg6laxeJYrUFiOBAXsLydZr0YYyeh0NW5Sc30e9iqI2wkPvjnAXnG8xV0DaJEmN+H5MljDDO0r73xKFJYZU1BikplMTFOV8i3xlnjzMhhLsuJS1i1StdocUrvyaxjMpRqB2kuUhhGF4xbEdC5LoLYDhzpVWM9qKcpOahuzr2YjNxsNLTxoOD8Hriek9ReTA+DpBqiRJW2riijltVq1pcgG1zOBGA3UNOeQ5+m+vcUveLghM+T0xKY3kPI4Y5WZ7IHg2UMQUT9JdnvOzEW/e6hh837F775PMIeUMxPxUcQ7fB4E2CaaE7deIslWl90nrOPkr3M=; incap_ses_482_2829404=paYlMDmEAFdKSSaVdGiwBojFBWYAAAAApTQyYhpXb58IUZXENm1vqA==; _ga_4PWL0638HD=GS1.1.1711654280.2.1.1711654281.59.0.0; _ga_30LZ5B848R=GS1.1.1711654280.2.1.1711654281.59.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Mar+28+2024+15%3A31%3A21+GMT-0400+(Eastern+Daylight+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=b1b33fcb-5583-4cba-9c07-9601d680dd2c&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false"
    logging.basicConfig(filename="./saves/logs.log", filemode="a", level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    try:
        url = "https://williamandmary.campusdish.com/api/menus/GetMenuCalendar?locationId=78390&storeIds="
        data = http_get(cookie, url)
        data = json.loads(data)
        date = data["AvailableDates"]
        # print(data)
        # print(date_list)
        date = list(date)
        date = sorted(date)
        date_list = []
        date_list_save = []
        for one_obj in date:
            datetime_obj = datetime.datetime.strptime(one_obj, "%Y-%m-%dT%H:%M:%S")
            formatted_date_str = datetime_obj.strftime("%m/%d/%Y")
            formatted_date_str_save = datetime_obj.strftime("%Y-%m-%d")
            date_list.append(formatted_date_str)
            date_list_save.append(formatted_date_str_save)
        logging.info(f"Available date number: {len(date_list)}")
    except Exception as e:
        # print("Error", e)
        logging.error(f"An error occurred in fetching available date list: {str(e)}", exc_info=True)
        date_list = get_following_days(n=14)
        date_list_save = get_following_days(n=14, format="%Y-%m-%d")
        logging.info("Using default available dates...")
        logging.info(f"Available date number: {len(date_list)}")
    return date_list, date_list_save


def get_following_days(n=10, format="%m/%d/%Y"):
    est = pytz.timezone('America/New_York')
    today = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    today = today.astimezone(est)
    date_list = [(today + datetime.timedelta(days=i)).strftime(format) for i in range(n)]
    return date_list


def one_day_job(force=False, one_time_flag=False):
    date_string = get_now_string("%m/%d/%Y")
    print(get_now_string(), f"[ ok ] Triggered on {date_string}.")
    if not os.path.exists("./saves"):
        os.makedirs("./saves")
    logging.basicConfig(filename="./saves/logs.log", filemode="a", level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(f"Starting [Schedule Mode] ..." if not one_time_flag else f"Starting [One-time Mode] ...")
    # date_string_save = get_now_string("%Y-%m-%d")
    date_string_full = get_now_string()
    complete_cookie = get_cookie(f'https://williamandmary.campusdish.com/api/menu/GetMenus?locationId=78391&mode=Daily&date={date_string}')
    # date_string_available_list = get_following_days(n=14)
    # date_string_available_list_save = get_following_days(n=14, format="%Y-%m-%d")
    date_string_available_list, date_string_available_list_save = get_available_date_list(cookie=complete_cookie)
    logging.info(f"date_string_available_list (length={len(date_string_available_list)}): {str(date_string_available_list)}")
    location_list = LOCATION_LIST
    logging.info(f"location_list: {str(location_list)}")

    task_count = 0
    skip_existing_count = 0
    skip_short_count = 0

    for one_date_string, one_date_string_save in zip(date_string_available_list, date_string_available_list_save):
        for one_location in location_list:
            if not force and os.path.exists(f"./saves/{one_location}/") and one_date_string_save in os.listdir(f"./saves/{one_location}/"):
                logging.info(f"'{one_date_string_save}' exists in './saves/{one_location}/'. Skipped.")
                skip_existing_count += len(PERIOD_LIST)
                task_count += len(PERIOD_LIST)
                continue
            for one_period in PERIOD_LIST:
                task_count += 1
                try:
                    url_menu = f"https://williamandmary.campusdish.com/api/menu/GetMenus?locationId={one_location}&mode=Daily&date={one_date_string}&periodId={one_period}"
                    data = http_get(complete_cookie, url_menu)
                    data = json.loads(data)
                    content_length = len(str(json.dumps(data)))
                    logging.info(f"data length: {content_length} ({one_location} ({LOCATION_DICTIONARY.get(one_location)}) on {one_date_string}: {one_period} ({PERIOD_DICTIONARY[one_period]}))")
                    limit = 15000
                    if content_length < limit:
                        logging.info(f"Too short response: {content_length} < {limit}. Skipped.")
                        skip_short_count += 1
                        continue
                    save_folder = f"./saves/{one_location}/{one_date_string_save}"
                    if not os.path.exists(save_folder):
                        os.makedirs(save_folder)
                    save_path = f"{save_folder}/{one_period}.json"
                    with open(save_path, "w") as f_json:
                        json.dump(data, f_json, indent=4)
                    save_path_log = f"{save_folder}/save_log.txt"
                    record_date_string = get_now_string()
                    log_content = {
                        "target_date_string": one_date_string,
                        "launch_time": date_string_full,
                        "record_time": record_date_string,
                        "content_length": content_length,
                        "Cookie": complete_cookie,
                    }
                    with open(save_path_log, "a") as f_log:
                        f_log.write(str(log_content) + "\n")
                except Exception as e:
                    logging.error(f"An error occurred in fetching data: {str(e)}", exc_info=True)
                    logging.info(f"Failed to deal with {one_location} ({LOCATION_DICTIONARY[one_location]}) on {one_date_string}: {one_period} ({PERIOD_DICTIONARY[one_period]})! Skipping")
    logging.info(f"Finished. {date_string}. Total: {task_count} | Newly-downloaded: {task_count - skip_existing_count - skip_short_count} | Existing-skip: {skip_existing_count} | Short-skip: {skip_short_count}")
    print(get_now_string(), f"[ ok ] Finished {date_string}. Total: {task_count} | Newly-downloaded: {task_count - skip_existing_count - skip_short_count} | Existing-skip: {skip_existing_count} | Short-skip: {skip_short_count}")




if __name__ == "__main__":
    # print(stamp_to_string(time.time()))
    # print(stamp_to_string(time.time() + 86400))
    # date = "2022-10-20"
    # menu = get_menu(date)
    # print(json.dumps(menu, indent=4, ensure_ascii=False))
    # res = http_get("2022-09-20")
    # print(res)
    # menu = get_menu("2022-09-16")
    # print(json.dumps(menu, indent=4, ensure_ascii=False))
    # print(get_week_day_name("2022-10-08"))
    # daily_job()

    # url_cookie = "https://williamandmary.campusdish.com/LocationsAndMenus/FoodHallSadler"

    # url = 'https://williamandmary.campusdish.com/api/menu/GetMenus?locationId=78391&mode=Daily&date=03/29/2024&periodId=5409'  # Replace with the actual URL
    # cookies = get_cookie(url)
    # get_available_date_list(cookies)

    # print(os.listdir("saves/78390/"))

    # cookie_dict = cookies.get_dict()
    # print("cookie dict:")
    # print(cookie_dict)
    # print()
    # cookie_text = '; '.join([f'{name}={value}' for name, value in cookie_dict.items()])
    # # # Output the cookie text
    # print("cookie text:")
    # print(cookie_text)
    # print()
    # print(cookies)
    # data = http_get(cookie_text + const_cookie)
    # data = json.loads(data)
    # print(json.dumps(data, indent=4))

    # data = http_get("__CLAnonymousUser=024lS2vUWDvoatoVBDgDQU5jQ==Bvd/IOf+iUSneipNMNpxhOIEr1/UtEkxe+1Cm6Dj3axcsAOU/L4TxxHURHAQeRzLthlQhddnRryZGzj0+EuKfxG2swLzFqf5SNr5+6vzVi1hFmlXnFlEr/JBez/sWtTi4Vq5ZrSPdvTS53/ueD6NVSUmJrQu9iKuIMuE73bpTUS2VitLt/DGPOPqv1kmC3DiV591prKhXld/WKksNxkljhnrotoPolhthTNxSyiTNOlLq2CvAS13VPOl3mdeowoBIRvSzHWOGoChb2eRALD2dAS0N5fssULEAirjsAZFjyvky8IFQGu6DvxYB63/2QoJZ+QCsB0Hkx5+PfpivzXj4xDgB+nkuuB0Etu60YcR4p8R8Fu9JqQMlrpyO6CNFGjuVtwtdvt+sbzjJyXDu0kFkZw9mUgwtXQCVCt3rJ6r1/kirPpDRSkdqE3x0R+C+HfsRLgZmhW+Jnx6CLgLGMZ3sgbg2RFtYmrOWVm/LumJbHMvxtMHDnkJwCOXAfwbDq4jWClXJAQbmA8FI+Lal9rGfg1TfgVoLfMKSMZa6pJygrqLNoTE03fuQKWV/sgFMxBK66uV6PTIxYKts+n2YA4GNEpNXChxt8xBVoyxWgZ1Z+DoeHeClDLoRnuV2cYKps3iaNyROB0Y4IeWUS3nWEBgpo2TBkNN08HdFflw0Z627996eA0pYn9GgbwVC4NFfNqgptP3EiLAVn48bFWysKLYLe86iSD5sl6wqGiM4fqZOblc+Mk4jpBDmn5WWQtF2ACCLa4wbW5bIHBwAbJ4dHDb9Qi9gl5zlrfUuraBN2YrmK8=;AramarkContextInfo=9739|{53f130c4-cd67-4cf8-8db4-50b089c478de}|Higher Education;incap_ses_1544_2829404=uywfV/pVhTumyWood2RtFTJg5WUAAAAAK7sbDVi5FTHKB+MjVFhh6A==;visid_incap_2829404=u5AcbDl/Ri2iONyU9xSc9TJg5WUAAAAAQUIPAAAAAAB3OPdsUom3CXbuAXcdA/Bt;")


    # data = http_get()
    # print(data)

    # data = http_get(cookies, date="03/24/2024")
    # data = json.loads(data)
    # with open("test/test.json", "w") as f:
    #     json.dump(data, f, indent=4)
    # # # print(data)
    # print(json.dumps(data, indent=4))

    one_day_job(one_time_flag=True)
    # logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO,
    #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # logging.info("An error occurred1")
    # try:
    #     # Code block where you suspect an exception could occur
    #     logging.info("An error occurred0")
    #     1 / 0
    # except Exception as e:
    #     # Log the exception as an error
    #     logging.info("An error occurred1")
    #     logging.error("An error occurred2", exc_info=True)
    #     logging.error(f"An error occurred3: {str(e)}", exc_info=True)

    pass
