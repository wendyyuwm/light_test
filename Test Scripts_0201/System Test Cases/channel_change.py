#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'

if __name__ == '__main__':
    Op = Process_case.OpName
    Channel_TCs = lamptestclass.LampTest()
    group_number = 0
    lights_list = [3]
    scene_name = "Channelscene"
    TCs_list = ["IPJ_13494 TC1", "IPJ_13495 TC2", "IPJ_13496 TC3", "IPJ_13497 TC4",
                "IPJ_13498 TC5", "IPJ_13499 TC6", "IPJ_13500 TC7", "IPJ_13501 TC8"]
    TCs_body = {
        "TC1": [
            [Op.GC, '{"on": false}', "PUT"]
        ],
        "TC2": [
            [Op.UC, '{"on": false}', "PUT"],
        ],
        "TC3": [
            [Op.GC, '{"effect": "colorloop"}', "PUT"]
        ],
        "TC4": [
            [Op.UC, '{"effect": "colorloop"}', "PUT"]
        ],
        "TC5": [
            [Op.GC, '{"on": true}', "PUT"],
            [Op.GC, '{"on": false, "transitiontime": 600}', "PUT"]
        ],
        "TC6": [
            [Op.GC, '{"on": true}', "PUT"],
            [Op.UC, '{"on": false, "transitiontime": 600}', "PUT"]
        ],
        "TC7": [
            [Op.GC, '{"on": true, "bri": 255, "hue": 65535, "sat": 255}', "PUT"]
        ],
        "TC8": [
            [Op.UC, '{"on": true, "bri": 255, "hue": 65535, "sat": 255}', "PUT"]
        ]
    }

    try:
        Process_case.process_case(Channel_TCs, TCs_list, group_number, lights_list, TCs_body, scene_name)

    finally:
        Channel_TCs.write_log_all("Channel_change", "./logs/system_test")
