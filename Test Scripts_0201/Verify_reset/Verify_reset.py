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
        bridge_ip = "192.168.1.3"
        bridge_user = "5eoCtKE89GTnziEBEHmAMxiS3GY95NO1pWHJo-yq"
        group_number = 1
        light_list = [25, 26, 27, 28, 29, 30, 31, 32]
        pre_url = "http://" + bridge_ip + "/api/" + bridge_user
        url = pre_url + "/groups/%s/action" % group_number
        j = 0
        while True:
            j += 1
            return_value_list = []
            print '\n' + '*' * 10 + " %s time(s) " % str(j) + '*' * 10
            log_file.write('\n' + '*' * 30 + " %s time(s) " % str(j) + '*' * 30 + '\n')
            body_list = [{"on": False}, {"on": True, "ct": 454, "bri": 25},
                         {"ct": 156, "bri": 203, "transitiontime": 3000}]
            for body in body_list:
                format_body = json.dumps(body)
                print '\nLights status %s' % format_body
                log_file.write('\nLights status %s\n' % format_body)
                response = requests.put(url, format_body).text
                log_file.write('\n' + response + "\n")
                log_file.flush()
                time.sleep(120)
            time.sleep(360)
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

    except Exception as e:
        print ("\n%s" % e)
        sys.exit()

    except KeyboardInterrupt:
        sys.exit()

    finally:
        log_file.close()
