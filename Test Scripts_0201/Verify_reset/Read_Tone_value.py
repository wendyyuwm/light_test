# -*- coding: utf-8 -*-
# !/usr/bin/python2.7

import requests
import json
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
    log_file = open("%s_%s.log" % (file_path, random_num), "w")
    try:
        bridge_ip = "192.168.1.2"
        bridge_user = "HYzvbNC5OqbiquPmh4rOQZOvsf4EWQ8hqh7HuV51"
        group_number = 1
        light_list = [25, 26, 27, 28, 29, 30, 31, 32]
        pre_url = "http://" + bridge_ip + "/api/" + bridge_user
        url = pre_url + "/groups/%s/action" % group_number
        while True:
            return_value_list = []
            real_time = time.strftime("%Y_%m_%d %H:%M:%S", time.localtime())
            print "\n" + real_time + "\n Read ct value for lights"
            log_file.write('\n\t' + real_time + "\n")
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
                            log_file.write("\t\t%5s\t\t|\t\t%s" % (light, read_value))
                            log_file.flush()
                log_file.write('\n')
            time.sleep(3600)

    except Exception as e:
        print ("\n%s" % e)
        sys.exit()

    except KeyboardInterrupt:
        sys.exit()

    finally:
        log_file.close()
