# JoinClass
join zoom classes automatically :~)

# TODO

- function to go through gmail find zoom invites and get link, meeting ID, and passcode 
    *  import webbrowser as wb
    *  zoom_invites = 'https://mail.google.com/mail/u/0/#search/join+zoom' 
    *  wb.open_new(zoom_invites) 
    * THIS WILL AT LEAST GET U TO THE EMAILS BUT I NEED TO FIGURE OUT HOW TO GET INTO EACH EMAIL AND FIND THESE NICE INFOS :) 
   - this function should also be looking for the date and time of the meeting and comparing it to the current time and giving you a nice countdown until its time to go to that meeting. Clearly if the meetings are OLD and current date > zoom invite, then we should ignore the invite entirely 
    
- Alert when breakout rooms are initiated 
- Alert when you automatically go into a class 
- Autorecord classes / screen record when in class
- Auto-screencapture chat every 15 minutes  
