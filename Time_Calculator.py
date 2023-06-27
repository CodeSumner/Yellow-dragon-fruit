#https://replit.com/@CodeSumner/boilerplate-time-calculator#time_calculator.py

# set function arguments optinal.
def add_time(*args):

    week_day = "" # record the day of week user entered.
    day_time = 0 # record the days number after start time.
    duration_hour_min = [] # list of duration hours and minutes.
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    start_time = list(args[0].split(" ")) # list of start time elements.
    am_or_pm = start_time[1] # record the AM or PM user entered.
    start_hour_min = list(start_time[0].split(":")) # list of start time hours and minutes.
    duration_hour_min = list(args[1].split(":")) # list of duration hours and minutes.

    new_hour = int(start_hour_min[0]) + int(duration_hour_min[0])  # the sum of hours.
    new_min = int(start_hour_min[1]) + int(duration_hour_min[1])   # the sum of minutes.

    # check the sum of minutes value.
    if new_min >= 60:
        new_min = new_min - 60
        new_hour += 1

    # make sure minutes print out at right format.
    if new_min < 10:
        new_min = "0" + str(new_min)

    # check the sum of hours value to determine the AM or PM, 
    # and days added as the duration time added.
    if new_hour == 12:
        if am_or_pm != "AM":
            am_or_pm = "AM"
            day_time += 1 
        else:
            am_or_pm = "PM"
    
    if new_hour > 12 and new_hour < 24:
        new_hour = new_hour - 12
        if am_or_pm != "AM":
            am_or_pm = "AM"
            day_time += 1  
        else:
            am_or_pm = "PM"           
    
    if new_hour >= 24:
        day_time += new_hour//24
        if new_hour%24 == 12:
            if am_or_pm != "AM":
                am_or_pm = "AM"
                day_time += 1  
            else:
                am_or_pm = "PM"
        if new_hour%24 > 12:
            new_hour = new_hour%24 - 12
            if am_or_pm != "AM":
                am_or_pm = "AM"
                day_time += 1  
            else:
                am_or_pm = "PM"        
        else:
            new_hour = new_hour%24
    
    # if user enter the start day of week, according to days added calculate the new day of week.
    if len(args) == 3:
        week_day = args[2].capitalize()
        j = 0
        for i in range(len(day_of_week)):
            if day_of_week[i] == week_day:
                j = i
                if j + day_time > 6:
                    week_day = day_of_week[(j + day_time)%7]   
        # make sure the new day time pint out at right format when there is day of week entered.   
        if day_time == 1:
            day_time = ", " + day_of_week[j + day_time] + " (next day)"
        elif day_time == 0:
            day_time = ", " + day_of_week[j + day_time]
        elif j + day_time < 6 and j + day_time > 1:
            day_time = ", " + day_of_week[j + day_time] + " (" + str(day_time) + " days later" + ")"   
        else:
            day_time = ", " + day_of_week[(j + day_time)%7] + " (" + str(day_time) + " days later" + ")"
    # make sure the new day time pint out at right format when there is not day of week entered.
    else:
        if day_time == 1:
            day_time = " (next day)"
        elif day_time == 0:
            day_time = ""
        else:
            day_time = " (" + str(day_time) + " days later" + ")"
    # connect the new hour, new minutes, new AM or PM and new day time as string.
    new_time =  str(new_hour) + ":" + str(new_min) + " " + am_or_pm + day_time 
    
    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))