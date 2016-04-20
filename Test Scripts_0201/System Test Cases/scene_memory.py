#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'

if __name__ == '__main__':
    Op = Process_case.OpName
    SceneMem_Tcs = lamptestclass.LampTest()
    light_list = [2, 5, 6]
    group_number = 0
    TCs_list = [" IPJ_15819 TC1 ", " IPJ_15821 TC2 ", " IPJ_15822 TC3 ", " IPJ_16513 TC4 ", " IPJ_16514 TC5 "]
    TCs_body = {
        "TC1": [
            [Op.MSG, "Bridge contain 200 scenes (not locked, recycle true)\n"
                     "Lamp memory should empty: <factory reset all lamps>"],
            [Op.CS, '{"on":true, "bri":100}']
        ],
        "TC2": [
            [Op.MSG, "Bridge memory empty\n"
                     "A lamp linked to remote controller and this lamp is included in the scene"],
            [Op.CS, '{"on":true, "bri":200, "transitiontime":100}'],
            [Op.RS]
        ],
        "TC3": [
            [Op.MSG, "This case can't test, lamp memory should be full (48 scenes)"]
        ],
        "TC4": [
           [Op.MSG, "This case can't test, lamp memory should be full (48 scenes)"]
        ],
        "TC5": [
           [Op.MSG, "This case can't test, lamp memory should be full (48 scenes)"]
        ]
    }

    try:
        Process_case.process_case(SceneMem_Tcs, TCs_list, TCs_body, group_number, light_list)
    finally:
        SceneMem_Tcs.write_log_all("Scene_memory", "./logs/system_test/Scene_Memory")


