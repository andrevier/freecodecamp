def add_time(start, duration, weekday = ""):
  '''
  Receives a start time, in AM or PM, and a duration
  variables and return the time after the duration.
  The program can receive the day as a third ptional
  variable.
  For example:
  add_time("3:00 PM", "3:10")
  Returns: 6:10 PM
  
  add_time("11:30 AM", "2:32", "Monday")
  Returns: 2:02 PM, Monday
  add_time("10:10 PM", "3:30")
  Returns: 1:40 AM (next day)
  
  add_time("11:43 PM", "24:20", "tueSday")
  Returns: 12:03 AM, Thursday (2 days later)
  '''
  # Part the times in hours and minutes.
  start_time = start.split()[0]
  h1 = int(start_time.split(":")[0])
  m1 = int(start_time.split(":")[1])
  
  # Period of the day can be "AM" or "PM"
  period = start.split()[1]
  
  duration_time = duration.split()[0]
  h2 = int(duration_time.split(":")[0])
  m2 = int(duration_time.split(":")[1])
  
  h = int(h1) + int(h2)
  m = int(m1) + int(m2)
  # The hours has the form x*12 + y*12. The x is an integer and
  # the number of changes (AM to PM or PM to AM) and y*12 is the 
  # hours in that period of time. 
  # Total amount of hours are the sum of the hours plus the floor 
  # division of the minutes by 60. 
  h = h + m // 60
  changes = h // 12
  new_hour = h % 12
  new_min = m % 60
  
  # AM = 1 and PM = 2
  changes_dict = {"AM": 1, "PM":2}
  sum_changes = changes_dict[period] + changes

  if (sum_changes % 2) == 0:
    new_period = "PM"
  elif (sum_changes % 2) == 1:
    new_period = "AM"
  else:
    new_period = "Error"

  # The number of days passed
  days = sum_changes // 2 + sum_changes % 2 - 1
  if days == 1:
    days_passed = "(next day)"
  elif days > 1:
    days_passed = "(" + str(days) + " days later)"
  else:
    days_passed = ""
  
  # Error chek
  #print(f"start time: {h1}:{m1} {period}")
  #print(f"duration: {h2}:{m2}")
  #print(f"sum: {h}:{m}")
  #print(f"new time: {new_hour}:{new_min} {new_period}")
  
  # Find the new day of the week.
  week = ["Sunday", "Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday"]
  
  new_weekday = weekday
  if (weekday != ""):
    day_id = week.index(weekday.lower().capitalize())
    new_day_id = (day_id + days) % 7
    new_weekday = ", " + week[new_day_id]
  
  # Correct the minutes if less than 10 or the hours if 12 AM or PM
  if new_min < 10:
    new_min = "0" + str(new_min)
  else:
    new_min = str(new_min)

  if new_hour == 0:
    new_hour = "12"
  else:
    new_hour = str(new_hour)

  new_time = new_hour + ":" + new_min + " " +\
             new_period + new_weekday + " " + days_passed
  return new_time
