import schedule
import time

def send_notification():
    print("this is your scheduled notification")

#schedule the notification every 10 sec
schedule.every(10).seconds.do(send_notification)

print("scheduler started. press Ctrl+c to stop. ")
while True:
    schedule.run_pending()
    time.sleep(1)