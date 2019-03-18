import csv
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import datetime



Name = input("Welcome, here. How can I call you?: \n")

print("""
With this program you can make statistics of your sleep.
enter your sleep for every day and get plots, average hours of sleep,
and many else.
Right now this program is still in development so excuse
that it's not running perfectly.
Also updates with more features and options to choose soon!

(At 1.1 your stats will be shown, you can also save your plot
 together with these informations to document it. ..will be
  automated in this program soon)

Available options: (to select an option, just enter index number)

1  Enter sleep of a week for every day                                     
   See sleep of the week as plot
   See my total hours of sleep this week + average hours of sleep per night
 1.1   see log stats for a week
2  Read my stats
3  write my stats to a file (csv)   
""")

def choose_option():
    choose = input("\n What you want to do: \n")
    while choose == '1':
        sleep_monday()
        sleep_tuesday()
        sleep_wednesday()
        sleep_thursday()
        sleep_friday()
        sleep_saturday()
        sleep_sunday()
        plotsee = input("\n see the plot(y/n): ")
        if plotsee == 'y':
            sleep_plot()
            sleep_analize()
            see_stats = input("\n wanna have an overview of your stats?(y/n):  ")
            if see_stats == 'y':
                log_week()
                return
            else:
                return
        else:
            return
        
    if choose == '2':
        stat_read()

    if choose == '3':
        print("Sorry, not available right now..:(..")
        return
    
    return
        
        
def sleep_monday():
    global mon_sleep
    mon_sleep = float(input("sleep sun->mon i h: "))
    return mon_sleep

def sleep_tuesday():
    global tue_sleep
    tue_sleep = float(input("sleep mon->tue in h: "))
    return tue_sleep

def sleep_wednesday():
    global wed_sleep
    wed_sleep = float(input("sleep tue->wed in h: "))
    return wed_sleep

def sleep_thursday():
    global th_sleep
    th_sleep = float(input("sleep wed->thu in h: "))
    return th_sleep

def sleep_friday():
    global fr_sleep
    fr_sleep = float(input("sleep thu->fr in h: "))
    return fr_sleep

def sleep_saturday():
    global sat_sleep
    sat_sleep = float(input("sleep fr>sat in h: "))
    return sat_sleep

def sleep_sunday():
    global sun_sleep
    sun_sleep = float(input("sleep sat->sun in h: "))
    return sun_sleep
    


def sleep_plot():
    """input data of every day for plot..
     x-arryayday_ofweek  y-array: daily_sleep"""

    day_ofweek = [1, 2, 3, 4, 5, 6, 7]
    daily_sleep = [mon_sleep, tue_sleep, wed_sleep, th_sleep, \
                   fr_sleep, sat_sleep, sun_sleep]

    plt.xlabel('Tage')
    plt.ylabel('Schlaf in h')
    startx, endx = 1, 7
    starty, endy = 1, 20
    plt.axis([startx, endx, starty, endy])
    plt.plot(day_ofweek, daily_sleep)
    plt.show()
    return

def sleep_analize():
    global sleep_week
    global sleep_weekav
    sleep_week = float(mon_sleep + tue_sleep + wed_sleep + th_sleep \
                  + fr_sleep + sat_sleep + sun_sleep)
    sleep_weekav = ((sleep_week) / 7)
    print("hours of sleep this week: ", sleep_week)
    print("average h of your sleep: ", sleep_weekav)
    return

def stat_read():
    df = pd.read_csv('MySleep.csv', sep='\t')
    print(df)
    return

def log_week():   #first get current date
    print("\n today's week number: ", datetime.date.today().isocalendar()[1])
    global tday
    tday = datetime.datetime.now()
    print("\n today's date is: \n", tday)

    #Dataframe beschreiben
    dates = tday
    tags = ["total sleep", "averagesleep"]
    totsl = pd.Series([sleep_week])
    avrgsl = pd.Series([sleep_weekav])
    log_df = pd.concat([totsl, avrgsl], axis=1)
    log_df.columns = tags

    print(log_df)
    return


def main():
    print("Hi, ", Name, ". explore the program :) ")
    while True:
        choose_option()
    return
main()
