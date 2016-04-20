#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'


if __name__ == '__main__':
    Op = Process_case.OpName
    Monitor_TCs = lamptestclass.LampTest()
    light_list = [1, 2, 3, 4, 7, 8, 9]
    group_number = 0
    scene_name = "MonitorScene"
    TCs_list = [" IPJ_8108 TC1 ", " IPJ_8109 TC2 ", " IPJ_8110 TC3 ", " IPJ_8111 TC4 ", " IPJ_8112 TC5 ",
                " IPJ_8113 TC6 ", " IPJ_8114 TC7 ", " IPJ_8115 TC8 ", " IPJ_15473 TC9 ", " IPJ_15474 TC10 ",
                " IPJ_15475 TC11"]
    TCs_body = {
        "TC1": [
            [Op.MSG, 'Manually powercycle lamps under test'],
            [Op.RA, ["ct", "bri"]]
        ],
        "TC2": [
            [Op.UC, '{"on": false}', "PUT"],
            [Op.RA, ["on"]]
        ],
        "TC3": [
            [Op.GC, '{"on":true, "xy": [0.5175, 0.2664]}', "PUT"],
            [Op.RA, ["xy", "colormode"]],
            [Op.GC, '{"ct": 153}', "PUT"],
            [Op.RA, ["ct", "colormode"]]
        ],
        "TC4": [
            [Op.UC, '{"effect": "colorloop"}', "PUT"],
            [Op.RA, ["effect"]]
        ],
        "TC5": [
            [Op.GC, '{"alert": "lselect"}', "PUT"],
            [Op.RA, ["alert"]]
        ],
        "TC6": [
            [Op.GC, '{"on": true, "hue": 52713, "sat": 254}', "PUT"],
            [Op.RA, ["hue", "sat", "colormode"]]
        ],
        "TC7": [
            [Op.GC, '{"on": true, "ct": 263}', "PUT"],
            [Op.RA, ["ct"]]
        ],
        "TC8": [
            [Op.GC, '{"xy": [0.48953, 0.44854]}'],
            [Op.RA, ["xy"]]
        ],
        "TC9": [
            [Op.GC, '{"on": true, "bri": 130}', "PUT"],
            [Op.RA, ["bri"]]
        ],
        "TC10": [
            [Op.GC, '{"on": false}', "PUT"],
            [Op.RA, ["on"]]
        ],
        "TC11": [
            [Op.GC, '{"on": false}', "PUT"],
            [Op.RA, ["on"]],
            [Op.GC, '{"on": true}'],
            [Op.RA, ["on"]]
        ]
    }

    try:
        Process_case.process_case(Monitor_TCs, TCs_list, TCs_body, group_number, light_list, scene_name)

    finally:
        Monitor_TCs.write_log_all("Monitor_visual", "./logs/system_test/Monitor/Monitor_visual")
