def add_time(start, duration, *args):
  week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  if 'PM' in start :
    start = str(int(start[:-6])+12)+start[-6:-3]
  else: start = start[:-3]

  hour = int(start[:-3]) + int(duration[:-3])
  minute = int(start[-2:]) + int(duration[-2:])

  hour += minute // 60
  minute = minute % 60

  n = 0
  if hour >= 24 :
    n = hour // 24
  hour = hour % 24
  if hour == 12 :
    hour = str(hour)
    minute = str(minute) + ' PM'
  elif hour > 12 :
    hour = str(hour-12)
    minute = str(minute) + ' PM'
  else:
    if hour == 0 :
        hour += 12
    hour = str(hour)
    minute = str(minute) + ' AM'
  
  if len(minute) != 5:
    minute = '0' + minute
  
  day = ''
  if args :
    start_day = args[0]
    day = week_days[(week_days.index(start_day.lower())+n)%7].capitalize()

  if n == 0 :
    if day :
      new_time = hour + ':' + minute + ', ' + day
    else: new_time = hour + ':' + minute
  elif n == 1 :
    if day :
      new_time = hour + ':' + minute + ', ' + day + ' (next day)'
    else: new_time = hour + ':' + minute + ' (next day)'
  else:
    if day :
      new_time = hour + ':' + minute + ', ' + day + ' ({} days later)'.format(n)
    else: new_time = hour + ':' + minute + ' ({} days later)'.format(n)

  return new_time
