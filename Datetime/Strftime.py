from datetime import date
from datetime import time
from datetime import datetime
#Date
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

#Time
t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S")) #B devuelve con el nombre del mes completo
print(dt.strftime("%y/%b/%d %H:%M:%S")) #b devuelve con el nombre del mes abreviado
    