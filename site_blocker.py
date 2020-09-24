# This script blocks sites at specific times of the day by adding domain names to the host directly

import time
from datetime import datetime as dt
# import calendar

hosts_temp = "hosts"
hosts_file_path = "/etc/hosts"  # for linux

redirect = "127.0.0.1"
website_list = ["facebook.com", "google.com", "youtube.com", "google.com"]

#day = dt.weekday(dt.now())
#current_time = dt.now().hour
# dt.strptime(str(dt.now()), '%Y-%m-%d %H:%M:%S.%f').weekday()


while True:
    if dt.weekday(dt.now()) <= 4 and dt.now().hour < 18:
        print("User cannot visit this site today")
        with open(hosts_file_path, 'r+') as file:
            content = file.read()
            # print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_file_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)  # place cursor at the beginning of file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()  # exit file and return new file size to the operating system
            # print(content)
        print("Fun hours.........")

    time.sleep(5)
