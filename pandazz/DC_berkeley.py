from datetime import datetime,timedelta

print("enter the total number of clocks")
n = int(input())

time_clock = []
for i in range(n):
    print(f"Enter time in clock {i+1} HH:MM")
    ip = input()
    datetime_obj = datetime.strptime(ip , '%H:%M').time()
    time_clock.append(datetime_obj)


total_seconds = []
print("\ntime entered is")
for t in time_clock:
    print(t)
    total_seconds.append(t.hour*3600 + t.minute*60)
avg_sec = sum(total_seconds)/n
average_time = timedelta(seconds = avg_sec)


print("\nfinal = ",average_time)
j=1
print("outputs to clocks")
for t in time_clock:
    diff_seconds = avg_sec - (t.hour*3600 + t.minute*60)
    print(diff_seconds)
    diff_time = timedelta(seconds=abs(diff_seconds))
    if diff_seconds >=0:
        print(f"clock {j} at time {t} needs +",diff_time)
    else:
        print(f"clock {j} at time {t} needs -",diff_time)
    j=j+1