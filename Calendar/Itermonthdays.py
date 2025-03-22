import calendar  

c = calendar.Calendar()

for Iter in c.itermonthdays(2019, 11):
    print(Iter, end=" ")
    