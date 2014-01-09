__author__ = 'jiahuixing'

import time
import os

SLEEP_TIME = 60*10

def schedule():
    block = "       "
    schedule_file = "schedule_file.txt"
    wrap = "\r\n"
    if os.path.exists(schedule_file):
        read_mode = "r"
        ymd = getymd()
        hms = gethms()
        text = ymd + block + hms + wrap
        file_obj = open(schedule_file,read_mode)
        length = len(file_obj.readlines())
        file_obj.close()
        if length > 0:
            file_obj = open(schedule_file,read_mode)
            r_result = file_obj.readlines()[length-1].strip(wrap)
    #        print(r_result)
            result = r_result.split()
            print(result)
            file_obj.close()
            if result != []:
                if result[0] == ymd:
                    print("sleep for %d sec"%SLEEP_TIME)
                    time.sleep(SLEEP_TIME)
                else:
                    read_mode = "a+"
                    file_obj = open(schedule_file,read_mode)
                    file_obj.write(text)
                    file_obj.close()
                    run()
                    getlog()
            else:
                read_mode = "a+"
                file_obj = open(schedule_file,read_mode)
                file_obj.write(text)
                file_obj.close()
                run()
                getlog()
        else:
            read_mode = "a+"
            file_obj = open(schedule_file,read_mode)
            file_obj.write(text)
            file_obj.close()
            run()
            getlog()

    else:
        read_mode = "a+"
        ymd = getymd()
        hms = gethms()
        text = ymd + block + hms + wrap
        file_obj = open(schedule_file,read_mode)
        file_obj.write(text)
        file_obj.close()
        run()

def getymd():

    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")
    ymd = "%s-%s-%s"%(year,month,day)
    return ymd

def gethms():

    hour = time.strftime("%H")
    mini = time.strftime("%M")
    sec = time.strftime("%S")
    hms = "%s:%s:%s"%(hour,mini,sec)
    return hms

def run():

    print("run")
    command_music = "adb shell uiautomator runtest uiautomator.jar -c com.miui.player.test.MusicPlayerTest"
    command_video = "adb shell uiautomator runtest uiautomator.jar -c com.miui.player.test.OnlineVideoTestWithLive"
    os.system(command_music)
    os.system(command_video)

def getlog():

    print("get a log")
    ymd = getymd()
    hms = gethms()
    ymd_hms = ymd + "-" + hms + ".txt"
    command_bugreport = "adb bugreport > " + ymd_hms
    os.system(command_bugreport)

if __name__=='__main__':
    while True:
        schedule()