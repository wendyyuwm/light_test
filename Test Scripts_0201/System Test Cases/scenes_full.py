#!/usr/bin/python

import lamptestclass
import Process_case
import time

__author__ = 'WendyYu'

if __name__ == '__main__':
    scene_full = lamptestclass.LampTest()
    try:
        numbers = raw_input("How many scenes do you want to create: ")
        lights_list = [1, 2, 3]
        Lights_body = None
        All_diff = raw_input("Set the same status for the lights for all scenes(y or n): ")
        if All_diff == 'y':
            Lights_body = raw_input('Enter the status of the lights(eg:{"on":true}): ')
        for i in range(int(numbers)):
            real_time = time.strftime("%H%M%S", time.localtime())
            scene_name = "Scene%s_%s" % (str(i + 1), real_time)
            if All_diff == 'n':
                Lights_body = raw_input('Enter the lights status for %s (eg:{"on":true}): ' % scene_name)
            print "*" * 10 + "\t" + str(i+1) + " scene(s)\t" + "*" * 10
            scene_full.msg_list.append("*" * 10 + "\t" + str(i+1) + " scene(s)\t" + "*" * 10)
            Process_case.wait_exit(False, scene_full.create_scene(scene_name, lights_list, Lights_body))

    except Exception as e:
        print "\nError:%s" % e
        raw_input("Press any key to quit...")

    except KeyboardInterrupt:
        raw_input("\nPress any key to quit...")

    finally:
        scene_full.write_log_all("Scene_full", "./logs/system_test/scene_full")





