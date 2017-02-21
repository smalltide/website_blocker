import time
from datetime import datetime as dt

host_temp = 'hosts'
host_path = r'/etc/hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com']

def is_work_time():
    return dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16)

while True:
    if is_work_time():
        print('Working hours')
        with open(host_temp, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f'{redirect} {website}\n')
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print('Fun hours')
    time.sleep(5)
