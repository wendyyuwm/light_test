#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'


if __name__ == '__main__':
    Op = Process_case.OpName
    Monitor_TCs = lamptestclass.LampTest()
    light_list = [1, 2, 3, 4, 7, 8, 11]
    group_number = 0
    scene_name = "MonitorScene"
    TCs_list = [" IPJ_15465 TC1 ", " IPJ_15466 TC2 ", " IPJ_15467 TC3 ", " IPJ_15468 TC4 ", " IPJ_15469 TC5 ",
                " IPJ_15470 TC6 ", " IPJ_15471 TC7 ", " IPJ_15472 TC8 ", " IPJ_15473 TC9 ", " IPJ_15474 TC10 ",
                " IPJ_15475 TC11 ", " New_Case1 TC12 ", " New_Case2 TC13 ", " New_Case3 TC14 "]
    TCs_body = {
        # "TC1": [
        #     [Op.MSG, 'Power cycle lamp manually'],
        #     [Op.RA, ["ct", "bri"]]
        # ],
        # "TC2": [
        #     [Op.CS, '{"on": false, "transitiontime": 100}'],
        #     [Op.RS],
        #     [Op.RA, ["on"]]
        # ],
        # "TC3": [
        #     [Op.GC, '{"on": true, "ct": 345}', "PUT"],
        #     [Op.RA, ["ct", "colormode"]],
        #     [Op.CS, '{"xy": [0.16195, 0.02948]}'],
        #     [Op.RS],
        #     [Op.RA, ["xy", "colormode"]]
        # ],
        # "TC4": [
        #     [Op.GC, '{"on": true}', "PUT"],
        #     [Op.RA, ["on"]],
        #     [Op.CS, '{"effect": "colorloop"}'],
        #     [Op.RS],
        #     [Op.RA, ["effect"]]
        # ],
        # "TC5": [
        #     [Op.GC, '{"on": true, "alert": "select"}', "PUT"],
        #     [Op.RA, ["alert"]]
        # ],
        # "TC6": [
        #     [Op.GC, '{"on": true}', "PUT"],
        #     [Op.RA, ["on"]],
        #     [Op.CS, '{"hue": 4274, "sat": 204}'],
        #     [Op.RS],
        #     [Op.RA, ["hue", "sat", "colormode"]]
        # ],
        # "TC7": [
        #     [Op.GC, '{"on": true}', "PUT"],
        #     [Op.RA, ["on"]],
        #     [Op.CS, '{"ct": 300}'],
        #     [Op.RS],
        #     [Op.RA, ["ct", "colormode"]]
        # ],
        "TC8": [
            [Op.GC, '{"on": true}', "PUT"],
            [Op.RA, ["on"]],
            [Op.CS, '{"xy": [0.49137, 0.45064]}'],
            [Op.RS],
            [Op.RA, ["xy", "colormode"]]
        ],
        "TC9": [
            [Op.GC, '{"on": true, "bri": 254}', "PUT"],
            [Op.RA, ["on", "bri"]],
            [Op.CS, '{"bri": 25}'],
            [Op.RS],
            [Op.RA, ["bri"]]
        ],
        "TC10": [
            [Op.GC, '{"on": true}', "PUT"],
            [Op.RA, ["on"]],
            [Op.CS, '{"on": false}'],
            [Op.RS],
            [Op.RA, ["on"]]
        ],
        "TC11": [
            [Op.GC, '{"on": false}', "PUT"],
            [Op.RA, ["on"]],
            [Op.CS, '{"on": true}'],
            [Op.RS],
            [Op.RA, ["on"]]
        ],
        "TC12": [
            [Op.GC, '{"on": true}', "PUT"],
            [Op.RA, ["on"]],
            [Op.MSG, "Wait for all lamps transition off"],
            [Op.CS, '{"on": false, "transitiontime": 600}'],
            [Op.RS],
            [Op.RA, ["on"]]
        ],
        "TC13": [
            [Op.GC, '{"on": false}', "PUT"],
            [Op.RA, ["on"]],
            [Op.MSG, "Wait for all lamps transition on"],
            [Op.CS, '{"on": true, "bri":150, "transitiontime": 600}'],
            [Op.RS],
            [Op.RA, ["on", "bri"]]
        ],
        "TC14": [
            [Op.GC, '{"bri": 254}', "PUT"],
            [Op.RA, ["bri"]],
            [Op.MSG, "Wait for all lamps transition to bri 1"],
            [Op.CS, '{"bri": 1, "transitiontime": 600}'],
            [Op.RS],
            [Op.RA, ["bri"]]
        ]
    }

    try:
        Process_case.process_case(Monitor_TCs, TCs_list, TCs_body, group_number, light_list, scene_name)

    finally:
        Monitor_TCs.write_log_all("Monitor_clipsdk", "./logs/system_test/Monitor")
