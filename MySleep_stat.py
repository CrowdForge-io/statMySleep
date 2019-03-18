import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date


Name = input("Welcome, here. How can I call you?: \n")
Now = date.today()
print(Now)

print("""
With this program you can make statistics of your sleep.
enter your sleep for every day and get plots, average hours of sleep,
and many else.
Right now this program is still in development so excuse
that it's not running perfectly.
Also updates with more features and options to choose soon!

Available options: (to select an option, just enter index number)

1  Enter sleep of a week for every day
   See sleep of the week as plot
   See my total hours of sleep this week + average hours of sleep per night
2  Save my stats to a file
""")

def choose_option():
    choose = input("What you want to do: \n")
    while choose == '1':
        sleep_monday()
        sleep_tuesday()
        sleep_wednesday()
        sleep_thursday()
        sleep_friday()
        sleep_saturday()
        sleep_sunday()
        plotsee = input("see the plot + inf? (y/n:  )")
        if plotsee == 'y':
            sleep_plot()
            sleep_analize()
        else:
            return
    while choose == '2':
        print("sorry, not possible right now")
        
        
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
    """Schlafstunden verarbeiten und als graph ausgeben
     x-Achse: day_ofweek  y-Achse: daily_sleep"""

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

def main():
    print("Hi, ", Name, ". explore the program :) ")
    while True:
        choose_option()
    return
main()
