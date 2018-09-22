
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime


from datetime import datetime, date, timedelta
import locale


locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")


dt_now = datetime.now()
dt_yest = dt_now - timedelta(days=1)
dt_month_ago= dt_now - timedelta(days=31)

dts = [dt_yest, dt_now, dt_month_ago]

for dt in dts:
	print(dt.strftime('%A %d-%m-%Y \n'))


date_string = "01/01/17 12:10:03.234567"

date_s = date_string.split('.')
date_dt = datetime.strptime(date_s[0], '%m/%d/%y %H:%M:%S')

print(date_dt)
