#!/bin/python
import os
import psutil
import time



# function will use above to format bytes to kilobytes or megabyte ...... 
def data_format(text, bytes):

    while (bytes > 1024):
        if bytes > 1073741824:
            return f"{text} {bytes/1073741824:.2f}GB"
        elif bytes > 1048576 :
            return f"{text} {bytes/1048576:.2f}MB"
        elif bytes > 1024 :
            return f"{text} {bytes/1024:.2f}KB"    
    else:
        return f"{text} {bytes}B"


# initialize the module with network interfaces
io = psutil.net_io_counters(pernic=True)

# variable to store the interfaces in device with downloaded bytes and recieved bytes
data = []

# get all interfaces in device and append in data list
for interface, io_interface in io.items():
    data.append([interface,  [io_interface.bytes_recv, io_interface.bytes_sent]])

# sort the interfaces in list to visualize it sorted by the most downloaded interface
data.sort(key=lambda a : a[1][0], reverse=True)
#print(data[1][1])


##### program loop #####

while (1) :
    # set one second to refresh screen
    time.sleep(1)

    # to refresh screen
    os.system('clear')

    # initialize the module second time to override new data with network interfaces
    io_2 = psutil.net_io_counters(pernic=True)
    data2 = []

    for interface2, io_interface2 in io_2.items():
        data2.append([interface2,  [io_interface2.bytes_recv, io_interface2.bytes_sent]])
    data2.sort(key=lambda a : a[1][0], reverse=True)

    # make loop to all interfaces in device and collect all bytes downloaded to visualize it
    Total_Data_Downloaded = data_format("", sum([i[1][0] for i in data2]))
    # make loop to all interfaces in device and collect all bytes uploaded to visualize it
    Total_Data_uploaded = data_format("", sum([i[1][1] for i in data2]))



    # head of the program
    print(f"""
    TOTAL_USAGE
    -------------------------------------------
    Data_Downloaded      :      {Total_Data_Downloaded}
    Data_uploaded        :      {Total_Data_uploaded}
    """)

    for i in range(len(data2)):
        print(f"""
    {data2[i][0]} 
    --------------------------------------
    data_downloaded     :        {data_format("", data2[i][1][0])}
    download_speed      :        {data_format("", data2[i][1][0] - data[i][1][0])}/s
    data_uplaoded       :        {data_format("", data2[i][1][1])}
    upload_speed        :        {data_format("", data2[i][1][1] - data[i][1][1])}/s 
        """)

        #refresh uploaded data to calculate speed
        data[i][1][1] = data2[i][1][1]
        #refresh downloaded data to calculate speed
        data[i][1][0] = data2[i][1][0]

