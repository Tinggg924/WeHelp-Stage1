#Task 1: Parse data from internet and save to files by Python
    # Here are URLs for tourist spots in Taipei provided by Taipei City Government:
    # https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1
    # https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2
    # Write a Python program without third-party libraries to parse data from above URLs and
    # output 2 files in CSV format:
    # 1. Output one spot information per line into spot.csv. If there are many image URLs in
    # source data, we only output the first one.
    # 2. Grouping spot titles by MRT station, output 1 MRT station and nearby spot titles per
    # line into mrt.csv.
    # Put spot.csv and mrt.csv files in your weekly task folder.

import urllib.request as request
import json

def get_mrt_data():
    scr1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
    scr2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
    with request.urlopen(scr1) as response:
        data1=json.load(response)
    clist1=data1["data"]["results"]

    with request.urlopen(scr2) as response:
        data2=json.load(response)
    clist2=data2["data"]

    mrt_data={}
    for i in clist2:
        if i["MRT"] not in mrt_data:
            mrt_data[i["MRT"]] = []
        for j in clist1:
            if i["SERIAL_NO"] == j["SERIAL_NO"]:
                mrt_data[i["MRT"]].append(j["stitle"])

    return mrt_data
mrt_data=get_mrt_data()
print(mrt_data)

import csv
with open("mrt.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for mrt, spots in mrt_data.items():
        row = [mrt]
        for spot in spots:
            row.append(spot)
        writer.writerow(row) 


# with open("mrt.csv", "w", newline="", encoding="utf-8") as csvfile:
#     for station, attractions in mrt_data.items():
#         attractions_str="," .join(attractions)
#         csvfile.write("{},{}\n".format(station, attractions_str))

# import urllib.request as request
# import json

# def get_spot_data():
#     scr1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
#     scr2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
    
#     with request.urlopen(scr1) as response:
#         data1 = json.load(response)
#     clist1 = data1["data"]["results"]

#     with request.urlopen(scr2) as response:
#         data2 = json.load(response)
#     clist2 = data2["data"]
    
#     spot_data_list = []
#     for spot in clist1:
#         for district in clist2:
#             if spot["SERIAL_NO"] == district["SERIAL_NO"]:
#                 spot_data = {}
#                 spot_data["stitle"] = spot["stitle"]
#                 spot_data["address"] = district["address"][5:8]
#                 spot_data["longitude"] = spot["longitude"]
#                 spot_data["latitude"] = spot["latitude"]
#                 spot_data["image"] = spot["filelist"].split("https://")[1].split()[0]
#                 spot_data_list.append(spot_data)
    
#     return spot_data_list

# spot_data_list = get_spot_data()

# import csv
# with open("spot.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     for spot_data in spot_data_list:
#         writer.writerow(spot_data.values())
   



    
    

