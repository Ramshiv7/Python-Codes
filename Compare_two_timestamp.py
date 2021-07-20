x = 30
format = '%Y%m%d%H%M%S'

std_del = '20210720152706' ###### Start Delta to get from Shell output 
yy = int(std_del[:4])
mth = int(std_del[4:6])
dt = int(std_del[6:8])
H = int(std_del[8:10])
M = int(std_del[10:12])
S = int(std_del[12:14])

from datetime import datetime
ct_time = datetime.now()   #### TO get current timestamp Value 
ct_time = ct_time.strftime('%Y-%m-%d %H:%M:%S')
ct_timestamp = datetime.strptime(ct_time,'%Y-%m-%d %H:%M:%S') ## Current Timestamp Value 

print("Current Time is : ", ct_timestamp)

import datetime
start_del_val = datetime.datetime(yy, mth, dt, H, M, S)

print("Start Detla is: ", start_del_val)

time_change = datetime.timedelta(hours = x)

new_hwm_chge = start_del_val + time_change

print("New HWM :",new_hwm_chge)

diff = new_hwm_chge - ct_timestamp

if new_hwm_chge >= ct_timestamp :
    print("HWM is greater than current timestamp, Assigning currnt timestamp")
    start_delta = ct_timestamp.strftime(format)
    print(start_delta)
else:
    print('New HWM is less than current timestamp, providing new hwm ')
    start_delta = new_hwm_chge.strftime(format)
    print(start_delta)
