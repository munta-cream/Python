from datetime import datetime, date

mydate=datetime.today()
print(mydate)
cdate=datetime.now()
print(cdate)

print(cdate.year)
print(cdate.month)
print(cdate.day)

print(cdate.hour)
print(cdate.minute)
print(cdate.second)
print(cdate.microsecond)

print(cdate.strftime('Weekday short : %a'))
print(cdate.strftime('Weekday long : %A'))
print(cdate.strftime('Weekday number : %w'))

print(cdate.strftime('Month short : %a'))
print(cdate.strftime('Month long : %A'))
print(cdate.strftime('Month number : %w'))

print(cdate.strftime('Day of Month number : %d'))
print(cdate.strftime('Year without century : %y'))
print(cdate.strftime('Year with century : %Y'))

print(cdate.strftime('Hour 24 : %H'))
print(cdate.strftime('Hour 12 : %I'))
print(cdate.strftime('AM/PM : %p'))

print(cdate.strftime('Minute : %M'))
print(cdate.strftime('Second : %S'))
print(cdate.strftime('Microsecond : %f'))

print('-'*40)
print(cdate.strftime('%d-%m-%Y'))
print(cdate.strftime('%A,%m-%d-%Y'))
print(cdate.strftime('%a,%m/%d/%Y'))
print(cdate.strftime('%H:%M:%S.%f'))
print(cdate.strftime('%I:%M:%S.%f'))