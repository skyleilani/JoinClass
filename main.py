# PyAutoGUI lets your Python scripts control the 
# mouse and keyboard to automate interactions with other applications.
import pyautogui as pyauto
import webbrowser as wb
import datetime
import time
import click

# translating date to python interperatable format 
# should translate them to list format 
def translate_date(date): 
    dates = date.split("-",3)
    return list(map(int, dates))

def translate_time(time):
    times = time.split(":", 2)
    print(list(map(int, times)))
    return list(map(int, times))

def meeting_datetime(meeting_date, meeting_time):
    # (YY, MM, DD, HR, MIN, SEC)    
    composed_datetime = datetime.datetime(meeting_date[2], meeting_date[1], meeting_date[0], meeting_time[0], meeting_time[1], meeting_time[2])
   
    return composed_datetime 

# join the meeting 
# meeting_link = str 
# meeting_date = str
# meeting_time = str

def join_zoom (meeting_link, meeting_date, meeting_time): 

    translated_date = translate_date(meeting_date)
    translated_time = translate_time(meeting_time) 
    scheduled_meeting = meeting_datetime(translate_date, translated_time)

    # account for time difference between current time and meeting time 
    time_til_meeting = (scheduled_meeting - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    print("class starts in " + str(time_til_meeting/60) + " minutes")
    time.sleep(time_til_meeting)

    # zoom plumbing 
    # open the zoom link in a new chrome window 
    wb.get(using='chrome').open(meeting_link, new=2)
    time.sleep(5)

    # open link on zoom app -- would like for this to be conditional for if app is installed 
    # & if no response for a certain amount of time, move on and open in browser 
    pyauto.click(x=805, y=254, clicks=1, interval=0, button='left')
    time.sleep(10)

    # maximize zoom app 
    pyauto.click(x=195, y =31, clicks=1, interval=0, button='left')
    time.sleep(3)
    pyauto.click(x=50, y=776, clicks=1, interval=0, button='left')


# join_zoom("https://zoom.us/j/5146739899?pwd=Z3JTZzZHd1lyMzRhcHJpemlLUDJOZz09", "3-8-2022", "9:12" )
meeting_datetime("3-8-2022", "9:12")

