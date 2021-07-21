import time , datetime, sys, os
from MetaDB import MetaDB
from MetaDBExtension import MetaDBExtension

def adg_num_hwm():

    ## LWM into Epoch Value 
    low_water_mark = '2021-07-19 00:54:07' ## redefine to get as input - sys.argv[1]
    pattern = '%Y-%m-%d %H:%M:%S'
    lwm_epoch = int(time.mktime(time.strptime(low_water_mark, pattern)))
    print(lwm_epoch)

    ##Interval + LWM 

    mdb = MetaDBExtension(os.path.basename(__file__))
    del_splt_hrs = mdb.execute("select deltasplitinterval from syncpublish where publishid={0}".format(sys.argv[2])) 
    del_splt_hrs = int(del_splt_hrs) * 60 * 60 
    new_hwm_chge = del_splt_hrs + lwm_epoch

    print(new_hwm_chge)

    curnt_epoch = time.time() ## Current EPOCH Time


    if new_hwm_chge >= curnt_epoch :
        print("HWM is greater than current epoch, Assigning current epoch value as HWM")
        end_delta = curnt_epoch
        print(end_delta)
        return end_delta
    else:
        print('New HWM is less than current epoch, Assigning New HWM ')
        end_delta = new_hwm_chge
        print(end_delta)
        return end_delta


adg_num_hwm()
