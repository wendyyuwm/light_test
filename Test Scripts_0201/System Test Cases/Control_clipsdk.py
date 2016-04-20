#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'

if __name__ == '__main__':
    Op = Process_case.OpName
    Control_TCs = lamptestclass.LampTest()
    light_list = [1, 2, 3, 4, 7, 8, 9]
    group_number = 0
    scene_name = "controlscene"
    TCs_list = [" IPJ_8413 TC1 ", " IPJ_8393 TC2 ", " IPJ_8392 TC3 ", " IPJ_15487 TC4 ", " IPJ_15488 TC5 ",
                " IPJ_15489 TC6 ", " IPJ_15490 TC7 ", " IPJ_15491 TC8 ", " IPJ_15491 TC9 ", " IPJ_15493 TC10 ",
                " IPJ_15494 TC11 ", " IPJ_15495 TC12 ", " IPJ_15496 TC13 "]
    TCs_body = {
        "TC1": [
            [Op.GC, '{"on": true, "effect": "colorloop"}', "PUT"],
            [Op.RA, ["effect"]],
            [Op.GC, '{"effect": "none"}', "PUT"],
            [Op.RA, ["effect"]]
        ],
        "TC2": [
            [Op.CS, '{"on": true, "effect": "colorloop"}'],
            [Op.RS],
            [Op.RA, ["effect"]],
            [Op.GS]
        ],
        "TC3": [
            [Op.MSG, "Before long select stops, press continue"],
            [Op.GC, '{"alert": "lselect"}', "PUT"],
            [Op.GC, '{"alert": "none"}', "PUT"],
            [Op.RA, ["alert"]]
        ],
        "TC4": [
            [Op.GC, '{"on": true, "ct": 209}', "PUT"],
            [Op.RA, ["ct", "colormode"]],
            [Op.GC, '{"hue": 47014, "sat": 172}', "PUT"],
            [Op.RA, ["hue", "sat", "colormode"]]
        ],
        "TC5": [
            [Op.GC, '{"on": true, "ct": 439}', "PUT"],
            [Op.RA, ["ct", "colormode"]],
            [Op.CS, '{"xy": [0.67725, 0.32008]}'],
            [Op.RS],
            [Op.RA, ["xy", "colormode"]]
        ],
        "TC6": [
            [Op.UC, '{"on": true, "xy": [0.5175, 0.2664]}', "PUT"],
            [Op.RA, ["xy", "colormode"]],
            [Op.UC, '{"ct": 390}', "PUT"],
            [Op.RA, ["ct", "colormode"]]
        ],
        "TC7": [
            [Op.GC, '{"on": false}', "PUT"],
            [Op.RA, ["on"]],
            [Op.GC, '{"on": true}', "PUT"],
            [Op.RA, ["on"]]
        ],
        "TC8": [
            [Op.GC, '{"on": true}', "PUT"],
            [Op.RA, ["on"]],
            [Op.CS, '{"on": false}'],
            [Op.RS],
            [Op.RA, ["on"]]
        ],
        "TC9": [
            [Op.MSG, 'Please manually power down lamps under test']
        ],
        "TC10": [
            [Op.GC, '{"on": true, "bri": 39}', "PUT"],
            [Op.RA, ["bri"]],
            [Op.GC, '{"bri": 206}', "PUT"],
            [Op.RA, ["bri"]]
        ],
        "TC11": [
            [Op.GC, '{"on": true, "bri": 255, "xy": [0.16011, 0.0358]}', "PUT"],
            [Op.RA, ["bri", "xy"]],
            [Op.MSG, 'Wait for 10s before print continue'],
            [Op.CS, '{"xy": [0.68093, 0.32429],"transitiontime":100}'],
            [Op.RS],
            [Op.RA, ["xy"]]
        ],
        "TC12": [
            [Op.GC, '{"on": true, "alert": "lselect"}', "PUT"],
            [Op.RA, ["alert"]]
        ],
        "TC13": [
            [Op.UC, '{"on": true, "alert": "select"}', "PUT"],
            [Op.RA, ["alert"]]
        ]
    }

    try:
        Process_case.process_case(Control_TCs, TCs_list, TCs_body, group_number, light_list, scene_name)
    finally:
        Control_TCs.write_log_all("Control_clipsdk", "./logs/system_test/Control")
