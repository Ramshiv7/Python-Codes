import os, sys, time, smtplib
from MetaDB import MetaDB
from MetaDBExtension import MetaDBExtension


def ois_hwm():

    mdb = MetaDBExtension(os.path.basename(__file__))
    x = mdb.execute("select deltasplitinterval from syncpublish where publishid={0}".format(sys.argv[2]))  ### Get input from Metadata
    
    format = '%Y%m%d%H%M%S' ### required Output format 
    
    std_del = sys.argv[1] ###### Start Delta to get from Shell output 
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

    ### Converting Start detla into Python Date & Time object
    import datetime
    start_del_val = datetime.datetime(yy, mth, dt, H, M, S)
    print("Start Detla is: ", start_del_val)

    ### New HWM Value 
    time_change = datetime.timedelta(hours = x)
    new_hwm_chge = start_del_val + time_change
    print("New HWM :",new_hwm_chge)


    ### HWM & Current timestamp comparison 
    if new_hwm_chge >= ct_timestamp :
        print("HWM is greater than current timestamp, Assigning current timestamp as HWM")
        end_delta = ct_timestamp.strftime(format)
        print(end_delta)
        return end_delta
    else:
        print('New HWM is less than current timestamp, Assigning New HWM ')
        end_delta = new_hwm_chge.strftime(format)
        print(end_delta)
        return end_delta
    
ois_hwm()
