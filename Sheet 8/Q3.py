print("\n""Time 1\n"
      "------------------------")
hours=int(input("Hours: "))
minutes=int(input("Minutes: "))
seconds=int(input("Seconds: "))
print("------------------------")
time1=hours, minutes, seconds


print("\n""Time 2\n"
      "------------------------")
hours=int(input("Hours: "))
minutes=int(input("Minutes: "))
seconds=int(input("Seconds: "))
print("------------------------")
time2=hours, minutes, seconds

def time_to_seconds_time(hours, minutes, seconds):
    hours = hours % 12
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def time_difference(time1, time2):
    seconds1 = time_to_seconds_time(*time1)
    seconds2 = time_to_seconds_time(*time2)
    difference = abs(seconds1 - seconds2)
    return difference
print("Seconds since last struck 12 for time1:", time_to_seconds_time(*time1))
print("Seconds since last struck 12 for time2:", time_to_seconds_time(*time2))
print("Difference in seconds:", time_difference(time1, time2))
