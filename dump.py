import json
import os
import datetime

from const import LOCATION_DICTIONARY


def is_date_string_valid(date_string, date_format="%Y-%m-%d"):
    """
    Check if the given date string exactly matches the specified date format.

    Parameters:
    - date_string: The string representation of the date to check.
    - date_format: The format against which to validate the date_string.

    Returns:
    - True if date_string exactly matches the date_format, False otherwise.
    """
    try:
        datetime_object = datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def load_one_data(read_path):
    with open(read_path, "r") as f:
        date_data = json.load(f)
    date_data = dict(date_data)
    # print(date_data.keys())

    product_data_dic = dict()
    for one_product in date_data["Menu"]["MenuProducts"]:
        simplified_product = dict()
        for one_key in ["PeriodId", "StationId", "ProductId"]:
            simplified_product[one_key] = one_product[one_key] if one_key in one_product else None
        for one_key in ["MarketingName", "ShortDescription", "IsOrganic", "IsVegan", "IsVegetarian", "ServingSize", "ServingUnit", "Calories", "CaloriesFromFat", "IngredientStatement"]:
            simplified_product[one_key] = one_product["Product"][one_key] if one_key in one_product["Product"] else None
        if one_product["PeriodId"] not in product_data_dic:
            product_data_dic[one_product["PeriodId"]] = []
        product_data_dic[one_product["PeriodId"]].append(simplified_product)
    return product_data_dic


def dump_all_data_to_json(save_path="saves/", location_dictionary=LOCATION_DICTIONARY):
    assert os.path.exists(save_path)
    available_location_list = os.listdir(save_path)

    available_location_list = [item for item in available_location_list if item in location_dictionary]
    available_location_list = sorted(available_location_list)
    # print(available_location_list)

    data = dict()
    data["location_num"] = len(available_location_list)
    data["location_list"] = available_location_list
    data["location_dictionary"] = location_dictionary
    data["location_data"] = dict()
    for one_available_location in available_location_list:
        data["location_data"][one_available_location] = dict()
        available_date_list = os.listdir(f"{save_path}/{one_available_location}")
        available_date_list = [item for item in available_date_list if is_date_string_valid(item)]
        available_date_list = sorted(available_date_list)
        data["location_data"][one_available_location]["date_list"] = available_date_list
        data["location_data"][one_available_location]["date_num"] = len(available_date_list)
        data["location_data"][one_available_location]["date_data"] = dict()
        for one_available_date in available_date_list:
            read_file_path = f"{save_path}/{one_available_location}/{one_available_date}/{one_available_date}.json"
            one_data = load_one_data(read_file_path)
            data["location_data"][one_available_location]["date_data"][one_available_date] = one_data

    # print(json.dumps(data, indent=4))
    with open(f"{save_path}/data.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    dump_all_data_to_json()
    # load_one_data("saves/78390/2024-03-26/2024-03-26.json")
