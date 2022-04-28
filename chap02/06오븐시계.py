hour, minute = map(int,input().split())
time = int(input())

min_time=time%60
hour_time=time//60

new_hour=hour+hour_time
new_min =minute+min_time

if new_min>=60:
    new_hour = new_hour +(new_min//60)
    new_min = new_min%60
new_hour = new_hour%24
print("%d %d" %(new_hour,new_min))