from fillform import fill_form_and_submit
import schedule
import time
from dotenv import load_dotenv
import os

load_dotenv()

bkx = os.getenv("bkx")
browser_driver = os.getenv("browser_driver")
loai_xe = os.getenv("loai_xe")

def task():
    fill_form_and_submit(browser_driver=browser_driver, bkx=bkx, loai=loai_xe)

if __name__ == "__main__":
    schedule.every().day.at("06:00").do(task)
    schedule.every().day.at("12:00").do(task)

    print("running")

    while True:
        schedule.run_pending()
        time.sleep(1)