import csv
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import datetime

print(""" –\____ Coder: m1ghtfr3e, see more: https://github.com/m1ghtfr3e  ___/–


                             .__
          ()(/ _ `._.--.
        ((|_.   ) ) )   \_    _.-.-._
     -- ((|   .' /  (\   \`--'  _)--=' ------ .
   '    acab.. -' ._)_\   \.-.-._.             .
  '    ''`````\        \  .  _)--='             .
 '-----------\/'-. ---- `--"'-------------------.
|             |\\                                |
|                                                |
`----------------------------------------.....---'

march_19, 2019                  https://github.com/m1ghtfr3e/statMySleep

""")

Name = input("Welcome, here. How can I call you?: \n")

print("""
With this program you can make statistics of your sleep.
enter your sleep for every day and get plots, average hours of sleep,
and many else.

[ number of hours please in full numbers or half numbers (e.g. 5 or 6.5) for now! ]

Right now this program is still in development so excuse
that it's not running perfectly.
Also updates with more features and options to choose soon!

Available options: (to select an option, just enter index number)

1  Enter sleep of a week for every day                                     
   See sleep of the week as plot
   
   
 1.1   See log stats of a week
       See my total hours of sleep this week + average hours of sleep per night
       
 (1.2   create a csv file and write)  use this at the first time or for creting new file, if you wanna update, skip to 3!
         [the program and the file will be in the same path, please keep them together.]
 
 
2  Read my stats (you can read your csv file here, if it's existing)
""")

def choose_option():
    
    choose = input("\n What you want to do: \n")
    if choose == '1':
        sleep_monday()
        sleep_tuesday()
        sleep_wednesday()
        sleep_thursday()
        sleep_friday()
        sleep_saturday()
        sleep_sunday()
        plotsee = input("\n continue to your plot?(y/n): ")
        if plotsee == 'y':
            sleep_plot()
            average_week()
            see_stats = input("\n wanna have an overview of your stats?(y/n):  ")
            if see_stats == 'y':
                see_week()
                create_write = input("\n Wanna write to/ create a file?(update/create): \n")
                if create_write == 'update':
                    write_csv()
                if create_write == 'create':
                    create_csv()
                    return
                return
            else:
                return
        else:
            return  
    if choose == '2':
        read_csv()
        return
    else:
        print(" I don't know what to do..maybe there's no file?! ")
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
    starty, endy = 1, 24
    plt.axis([startx, endx, starty, endy])
    plt.title("Progress of your sleep this week")
    plt.plot(day_ofweek, daily_sleep, '--mo')
    what = input("Do you want to see or save the file?:  ")
    if what == 'see':
        plt.show()
        return
    if what == 'save':
        plt.savefig('MySleep_plot.png')
        return
    return

def average_week():
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

def see_week():   #first get current date
    print("\n today's week number: ", datetime.date.today().isocalendar()[1])
    global tday
    global weekn
    tday = datetime.datetime.now()
    weekn = datetime.date.today().isocalendar()[1]
    print("\n today's date is: \n", tday)

    #Dataframe beschreiben
    dates = tday
    tags = ["Name","Date of entry", "week number", "total sleep", "averagesleep",
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    name = pd.Series([Name])
    ttday = pd.Series([tday])
    totsl = pd.Series([sleep_week])
    avrgsl = pd.Series([sleep_weekav])
    wknm = pd.Series([weekn])
    mon = pd.Series([mon_sleep])
    tue = pd.Series([tue_sleep])
    wed = pd.Series([wed_sleep])
    thu = pd.Series([th_sleep])
    fri = pd.Series([fr_sleep])
    sat = pd.Series([sat_sleep])
    sun = pd.Series([sun_sleep])
    global log_df
    log_df = pd.concat([name, ttday, wknm, totsl, avrgsl, mon, tue, wed, thu,
                        fri, sat, sun], axis=1)
    log_df.columns = tags

    print(log_df)
    return

def write_csv():
    log_df.to_csv('MySleep.csv', sep=',', encoding='utf-8', mode='a', header=False, index=False)
    return

def create_csv():
    log_df.to_csv('MySleep.csv', sep=',', encoding='utf-8', index=False)
    print("you can find your file, in the same directory as this program :) ")
    return

def read_csv():
    reader = pd.read_csv('MySleep.csv', sep='\t')
    print(reader)
    return


def main():
    print("Hi, ", Name, ". explore the program :) ")
    while True:
        choose_option()
    return

main()
