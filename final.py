import requests, time
import pandas as pd
import concurrent.futures
import smtplib

output = []
output.append(["url","status_code","reason","Executing_time"])
error_list = []

def url_check1(url,sender,receiver,password,message):
    responce = requests.get(url)
    st_code = responce.status_code
    reason = responce.reason

    with concurrent.futures.ThreadPoolExecutor() as executor:
        if st_code == 200:
            executor.map(url_check1)
            time1 = time.time()
            output.append([url,st_code,reason,f'time taken {time1:.2f} s'])

        else:
            time1 = time.time()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message.format(url=url, st_code=st_code))
            error_list.append([url, st_code, reason, f'time taken {time1:.2f} s'])
            print('mail sent')

sender = "kavinkavinkk35@gmail.com"
receiver = "kavinmanok1975@gmail.com"
password = "zowthsnkiomnyjva"

message = '''Subject: URL Not Found

Please check the url here.....{url} and the status_code is {st_code}

Thanks for Visiting....!!!!!'''

df = pd.read_csv("url.csv")
i = 0
for url in df['0']:
    #print(url)
    if i<=5:
        url_check1(url,sender,receiver,password,message)
    i+=1

print("Program Completed......!!!!!")
