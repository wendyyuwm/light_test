#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'

if __name__ == '__main__':
    Op = Process_case.OpName
    Lamp_TCs = lamptestclass.LampTest()
    light_list = [1, 2, 3, 4, 5, 6, 7]
    group_number = 0
    scene_name = "lampscene"
    TCs_list = [" IPJ_8095 TC1 ", " IPJ_8096 TC2 ", " IPJ_8097 TC3 ", " IPJ_8098 TC4 ", " IPJ_8099 TC5 ",
                " IPJ_8100 TC6 ", " IPJ_8101 TC7 ", " IPJ_8102 TC8 ", " IPJ_8103 TC9 ", " IPJ_8104 TC10 ",
                " IPJ_8105 TC11 ", " IPJ_8106 TC12 ", " New_Case TC13 "]
    TCs_body = {
        # "TC1": [
        #     [Op.GC, '{"effect": "colorloop"}', "PUT"],
        #     [Op.RA, ["effect"]],
        #     [Op.CS, '{"effect": "none"}'],
        #     [Op.RS],
        #     [Op.RA, ["effect"]]
        # ],
        # "TC2": [
        #     [Op.GC, '{"on": false}', "PUT"],
        #     [Op.RA, ["on"]],
        #     [Op.GC, '{"on": true, "effect": "colorloop"}', "PUT"],
        #     [Op.RA, ["on", "effect"]]
        # ],
        # "TC3": [
        #     [Op.GC, '{"alert": "lselect"}', "PUT"],
        #     [Op.UC, '{"alert": "none"}', "PUT"]
        # ],
        # "TC4": [
        #     [Op.GC, '{"on": true, "bri": 254}', "PUT"],
        #     [Op.RA, ["on", "bri"]],
        #     [Op.MSG, "Before lamps off, press continue to do the next step"],
        #     [Op.CS, '{"on": false, "transitiontime": 600}'],
        #     [Op.RS],
        #     [Op.CS, '{"on": false}'],
        #     [Op.RS],
        #     [Op.RA, ["on"]]
        # ],
        # "TC5": [
        #     [Op.MSG, "Please manually power down lamps"],
        #     [Op.CS, '{"bri": 0}'],
        #     [Op.RS],
        #     [Op.GS]
        # ],
        # "TC6": [
        #     [Op.MSG, "Please manually power up lamps"],
        #     [Op.GC, '{"on": true, "bri": 150, "ct": 200}', "PUT"],
        #     [Op.RA, ["on", "bri", "ct"]],
        #     [Op.CS, '{"xy": [0.5175, 0.2664]}'],
        #     [Op.RS],
        #     [Op.RA, ["xy"]]
        # ],
        # "TC7": [
        #     [Op.GC, '{"on": true, "bri": 150, "xy": [0.5175, 0.2664]}', "PUT"],
        #     [Op.RA, ["on", "bri", "xy"]],
        #     [Op.CS, '{"ct": 200}'],
        #     [Op.RS],
        #     [Op.RA, ["ct"]]
        # ],
        # "TC8": [
        #     [Op.GC, '{"on": true, "bri": 150, "xy": [0.5175, 0.2664]}', "PUT"],
        #     [Op.RA, ["on", "bri", "xy"]],
        #     [Op.CS, '{"bri": 254, "hue": 65535, "sat": 254}'],
        #     [Op.RS],
        #     [Op.RA, ["bri", "hue", "sat", "colormode"]]
        # ],
        # "TC9": [
        #     [Op.GC, '{"on": true, "bri": 150, "xy": [0.5175, 0.2664]}', "PUT"],
        #     [Op.RA, ["on", "bri", "xy"]],
        #     [Op.GC, '{"alert": "select"}', "PUT"],
        #     [Op.RA, ["alert"]]
        # ],
        # "TC10": [
        #     [Op.GC, '{"on": true, "bri": 150, "xy": [0.5175, 0.2664]}', "PUT"],
        #     [Op.RA, ["on", "bri", "xy"]],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"],
        #     [Op.RA, ["alert"]]
        # ],
        "TC11": [
            [Op.GC, '{"on": true, "bri": 150, "xy": [0.5175, 0.2664]}', "PUT"],
            [Op.RA, ["on", "bri", "xy"]],
            [Op.MSG, "Please wait for 10s to transition"],
            [Op.CS, '{"on": false, "transitiontime": 100}'],
            [Op.RS],
            [Op.RA, ["on"]]
        ],
        "TC12": [
            [Op.GC, '{"on": false}', "PUT"],
            [Op.RA, ["on"]],
            [Op.CS, '{"on": true}'],
            [Op.RS],
            [Op.RA, ["on"]]
        ],
        "TC13": [
            [Op.GC, '{"hue": 65535, "sat":254, "bri":254}', "PUT"],
            [Op.RA, ["hue", "sat", "bri"]],
            [Op.MSG, "Please wait for 10s to transition"],
            [Op.GC, '{"hue": 65535, "sat":0, "transitiontime":100}', "PUT"],
            [Op.RA, ["hue", "sat"]]
        ]
    }

    try:
        Process_case.process_case(Lamp_TCs, TCs_list, TCs_body, group_number, light_list, scene_name)
    finally:
        Lamp_TCs.write_log_all("lamp", "./logs/system_test/Lamp")
