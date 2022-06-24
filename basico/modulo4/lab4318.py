# Laboratorio 4.3.1.7
#Luis Daniel Sánchez Cabrera

def is_year_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True

def days_in_month(year, month):
    months = [31,28,31,30,31,30,31,30,31,30,31,31]
    if is_year_leap(year)==0 and month == 2:
        return 29
    return months[month -1]

def day_of_year(year, month, day):
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None
    if day > days_in_month(year, month) or day < 1:
        return None
    
    diasTotales = day
    month = month - 1
    while month > 0:
        diasTotales += days_in_month(year, month)
        month -= 1
    return diasTotales

print(day_of_year(2000, 12, 31))