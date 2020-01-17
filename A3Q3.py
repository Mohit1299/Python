input_time = input("Enter the time : ")
time = input_time.split(":")
minute_angle = int(time[1])*6
print(minute_angle)
hour_angle = int(time[0])*30 + (minute_angle/12)
print(hour_angle)
if(hour_angle > minute_angle):
    res_angle = hour_angle - minute_angle
else:
    res_angle = minute_angle - hour_angle

if(res_angle > 180):
    print("The Smaller angle between the clock hands is : ",360-res_angle)
else:
    print("The smaller angle between the clock hands is : ",res_angle)
