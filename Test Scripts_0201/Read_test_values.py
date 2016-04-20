# -*- coding: utf-8 -*-
# !/usr/bin/python2.7

import requests
import time
import sys
import os

__author__ = 'WendyYu'

if __name__ == "__main__":
    random_num = time.strftime("%H%M%S", time.localtime())
    path = "./reset/log"
    if os.path.exists(path) == 0:
            os.makedirs(path)
    file_path = os.path.join(path, "reset")
    log_file = open("%s_%s_pk.log" % (file_path, random_num), "w")
    try:
        while True:
            bridge_ip = "192.168.1.14"
            bridge_user = "30b1dfe3727ee523f5bec385f3fff94"
            light_list = [2, 3, 4, 5, 6, 7, 8, 9]
            pre_url = "http://" + bridge_ip + "/api/" + bridge_user
            print "\nRead ct value for lights"
            for light in light_list:
                get_response = requests.get(pre_url + "/lights/%s" % light).text
                if "ct" in get_response:
                    response_list = get_response.split(",")
                    l = len(response_list)
                    for i in range(l):
                        find_string = '"ct":'
                        if find_string in response_list[i]:
                            s_id = response_list[i].index(find_string)
                            read_value = response_list[i][s_id:]
                            print "\nLight %s %s" % (light, read_value)
                            real_time = time.strftime("%H:%M:%S", time.localtime())
                            log_file.write('\n' + real_time + "\tLight %s %s" % (light, read_value))
                            log_file.flush()
                log_file.write('\n')
            time.sleep(5400)

    except Exception as e:
        print ("\n%s" % e)
        sys.exit()

    except KeyboardInterrupt:
        sys.exit()

    finally:
        log_file.close()
