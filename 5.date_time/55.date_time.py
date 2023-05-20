import time
import datetime

epochSeconds = time.time()
print(epochSeconds)

# Convert the epcSeconds readable time
c = time.ctime(epochSeconds)
print(c)

# Get the current date and time
dt = datetime.datetime.today()
print(dt)
print("Month", dt.month)
print("Year", dt.year)
print("Day", dt.day)
print("Hour", dt.hour)
print("Minute", dt.minute)
print("Seconds", dt.second)

# Combining seperate datatime objects
d = datetime.date(2023, 5, 20)
t = datetime.time(14, 30)
cmb = datetime.datetime.combine(d, t)
print(cmb)

# Sorting dates
d1 = datetime.date(1994, 10, 24)
d3 = datetime.date(2003, 7, 14)
d2 = datetime.date(1998, 2, 5)
lst = []
lst.append(d1)
lst.append(d2)
lst.append(d3)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

# Halt the operations for sometime, sleep
import time
# time.sleep(5)
print("This will apppear after system halt for 5 seconds")

# Benchmarking the application
startTime = time.perf_counter()
# time.sleep(5)
endTime = time.perf_counter()
print(endTime - startTime)

# Exercise validate credit card
def validateCard(expDate):
    if expDate > datetime.datetime.now().date():
        print("Valid")
    else:
        print("Not valid")

validateCard(datetime.date(1994, 10, 24))
validateCard(datetime.date(2025, 10, 24))
