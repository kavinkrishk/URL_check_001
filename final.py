import requests, time
import pandas as pd
import concurrent.futures
import smtplib

output = []
output.append(["url","status_code","reason","Executing_time"])
error_list = []

def url_check1(url,sender,receiver,password,message):
    responce = requests.get(url)
    sts_code = responce.status_code
    reason = responce.reason

    with concurrent.futures.ThreadPoolExecutor() as executor:
        if sts_code == 200:
            executor.map(url_check1)
            time1 = time.time()
            output.append([url,sts_code,reason,f'time taken {time1:.2f} s'])

        else:
            time1 = time.time()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message.format(url=url, sts_code=sts_code))
            error_list.append([url, sts_code, reason, f'time taken {time1:.2f} s'])
            print('mail sent')

if __name__ == "__main__":
    #print("ok")
    sender = "kavinkavinkk35@gmail.com"
    receiver = "kavintriplek001@gmail.com"
    #password = "@1z@12ow!thsnkiomny12jv54a"

    password = input(str("Enter the Password:"))

    message = '''Subject: URL Not Found

    Please check the url here.....{url} and the status_code is {sts_code}

    Thanks for Visiting....!!!!!'''

    def url_add(df):
        increment = 0
        for url in df['0']:
            # print(url)
            if increment <= 5:
                url_check1(url, sender, receiver, password, message)
            increment += 1
        print("Program Completed......!!!!!")

    df = pd.read_csv("url.csv")
    url_add(df)