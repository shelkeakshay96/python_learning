import datetime
import schedule
import time

def scheduleMinute():
    print('Schedular schedules after a minute')
    print(datetime.datetime.now())

def scheduleHour():
    print('Schedular schedules after a hour')
    print(datetime.datetime.now())

def scheduleSunday():
    print('Schedular schedules after a hour')
    print(datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(scheduleMinute)
    schedule.every().hour.do(scheduleHour)
    schedule.every().sunday.do(scheduleSunday)
    
    while(True):
        schedule.run_pending()
        time.sleep(50)

if (__name__ == '__main__'):
    main()
