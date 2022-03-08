""" update the address field of labii accounts """
import os
import json
from labii_sdk.sdk import LabiiObject

# update the ids here
organization__sid = "xxx"
column__sid = {
    "address": "xxx",
    "city": "xxx",
    "state": "xxx",
    "zipcode": "xxx",
    "country": "xxx"
}
column__address__sid__new = "xxx"
table__sid = "xxx"

def process_one_item(labii, item):
    """ process for one item """
    print(f'Working on item {item["row"]["name"]}...')
    # download the cell data
    cells = labii.Cell.list(serializer="detail", query=f"row__sid={item['row']['sid']}&column__sid__in={column__sid['address']},{column__sid['city']},{column__sid['state']},{column__sid['zipcode']},{column__sid['country']}")
    # prepare the data
    data = {
        "address": "",
        "address2": "",
        "city": "",
        "state": "",
        "zipcode": "",
        "country": ""
    }
    for field in column__sid:
        for cell in cells["results"]:
            if cell["column"]["sid"] == column__sid[field]:
                if cell["data"] != "":
                    data[field] = cell["data"]
                break
    # save the data
    # exists = labii.Cell.list(query=f"row__sid={item['row']['sid']}&column__sid={column__address__sid__new}")
    labii.Cell.create({"data": data}, query=f"row__sid={item['row']['sid']}&column__sid={column__address__sid__new}")

def process_one_page(labii, cell_list, processed):
    """ process one page of data """
    print(f"Working on page {cell_list['page_number']}/{cell_list['page_count']}...")
    for item in cell_list["results"]:
        if not item["sid"] in processed:
            processed.append(item["sid"])
            process_one_item(labii, item)
    # save data
    with open('labii_address.json', 'w') as outfile:
        json.dump(processed, outfile)
    return processed

def update_address():
    """ function to change address """
    labii = LabiiObject(organization__sid=organization__sid)
    labii.api.login()
    # load the processed data
    processed = []
    if os.path.exists("labii_address.json"):
        file_handle = open ('labii_address.json', "r")
        processed = json.loads(file_handle.read())
    # get initial data
    column__country__sid = column__sid["country"]
    query = f'column__sid={column__country__sid}&data__isnull=false'
    cell_list = labii.Cell.list(page_size=50, query=query)
    page_count = cell_list["page_count"]
    page = 1
    while page <= page_count:
        processed = process_one_page(labii, cell_list, processed)
        page += 1
        cell_list = labii.Cell.list(serializer="detail", page_size=50, page=page, query=query)
