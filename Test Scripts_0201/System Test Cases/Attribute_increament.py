#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'

if __name__ == '__main__':
    Op = Process_case.OpName
    Attribute_Tcs = lamptestclass.LampTest()
    light_list = [1, 2, 3, 4, 5, 6, 7]
    group_number = 0
    TCs_list = [" IPJ_15525 TC1 ", " IPJ_15526 TC2 ", " IPJ_15527 TC3 ", " IPJ_15537 TC4 ", " IPJ_15538 TC5 ",
                " IPJ_15539 TC6 ", " IPJ_15540 TC7 ", " IPJ_15541 TC8 ", " IPJ_15542 TC9 ", " IPJ_15543 TC10 ",
                " IPJ_15544 TC11 ", " IPJ_15545 TC12 ", " IPJ_15546 TC13 ", " IPJ_15547 TC14 ", " IPJ_15548 TC15 ",
                " IPJ_15549 TC16 ", " IPJ_15550 TC17 ", " IPJ_15551 TC18 ", " IPJ_15552 TC19 ", " IPJ_15553 TC20 ",
                " IPJ_15554 TC21 ", " IPJ_15555 TC22 ", "Added new_case1", "Added new_case2"]
    TCs_body = {
        # "TC1": [
        #     [Op.MSG, "Turn all lights on"],
        #     [Op.GC, '{"bri":100}', "PUT"],
        #     [Op.GC, '{"bri_inc": -254}', "PUT"],
        #     [Op.RA, ["bri"]],
        #     [Op.GC, '{"bri":200}', "PUT"],
        #     [Op.GC, '{"bri_inc": -1}', "PUT"],
        #     [Op.RA, ["bri"]],
        #     [Op.GC, '{"bri":75}', "PUT"],
        #     [Op.GC, '{"bri_inc": 0}', "PUT"],
        #     [Op.RA, ["bri"]],
        #     [Op.GC, '{"bri":150}', "PUT"],
        #     [Op.GC, '{"bri_inc": 1}', "PUT"],
        #     [Op.RA, ["bri"]],
        #     [Op.GC, '{"bri":225}', "PUT"],
        #     [Op.GC, '{"bri_inc": 254}', "PUT"],
        #     [Op.RA, ["bri"]]
        # ],
        # "TC2": [
        #     [Op.GC, '{"ct":153}', "PUT"],
        #     [Op.GC, '{"ct_inc": -153}', "PUT"],
        #     [Op.RA, ["ct"]],
        #     [Op.GC, '{"ct":200}', "PUT"],
        #     [Op.GC, '{"ct_inc": -1}', "PUT"],
        #     [Op.RA, ["ct"]],
        #     [Op.GC, '{"ct":225}', "PUT"],
        #     [Op.GC, '{"ct_inc": 0}', "PUT"],
        #     [Op.RA, ["ct"]],
        #     [Op.GC, '{"ct":153}', "PUT"],
        #     [Op.GC, '{"ct_inc": 1}', "PUT"],
        #     [Op.RA, ["ct"]],
        #     [Op.GC, '{"ct":225}', "PUT"],
        #     [Op.GC, '{"ct_inc": 500}', "PUT"],
        #     [Op.RA, ["ct"]]
        # ],
        # "TC3": [
        #     [Op.GC, '{"hue":20000}', "PUT"],
        #     [Op.GC, '{"hue_inc": -65534}', "PUT"],
        #     [Op.RA, ["hue"]],
        #     [Op.GC, '{"hue":30000}', "PUT"],
        #     [Op.GC, '{"hue_inc": -1}', "PUT"],
        #     [Op.RA, ["hue"]],
        #     [Op.GC, '{"hue":50000}', "PUT"],
        #     [Op.GC, '{"hue_inc": 0}', "PUT"],
        #     [Op.RA, ["hue"]],
        #     [Op.GC, '{"hue":60000}', "PUT"],
        #     [Op.GC, '{"hue_inc": 1}', "PUT"],
        #     [Op.RA, ["hue"]],
        #     [Op.GC, '{"hue":30000}', "PUT"],
        #     [Op.GC, '{"hue_inc": 65534}', "PUT"],
        #     [Op.RA, ["hue"]]
        # ],
        # "TC4": [
        #     [Op.GC, '{"sat":100}', "PUT"],
        #     [Op.GC, '{"sat_inc": -254}', "PUT"],
        #     [Op.RA, ["sat"]],
        #     [Op.GC, '{"sat":200}', "PUT"],
        #     [Op.GC, '{"sat_inc": -1}', "PUT"],
        #     [Op.RA, ["sat"]],
        #     [Op.GC, '{"sat":75}', "PUT"],
        #     [Op.GC, '{"sat_inc": 0}', "PUT"],
        #     [Op.RA, ["sat"]],
        #     [Op.GC, '{"sat":150}', "PUT"],
        #     [Op.GC, '{"sat_inc": 1}', "PUT"],
        #     [Op.RA, ["sat"]],
        #     [Op.GC, '{"sat":225}', "PUT"],
        #     [Op.GC, '{"sat_inc": 254}', "PUT"],
        #     [Op.RA, ["sat"]]
        # ],
        # "TC5": [
        #     [Op.GC, '{"xy":[0.48, 0.39]}', "PUT"],
        #     [Op.GC, '{"xy_inc": [-0.1, -0.1]}', "PUT"],
        #     [Op.RA, ["xy"]],
        #     [Op.GC, '{"xy":[0.52, 0.41]}', "PUT"],
        #     [Op.GC, '{"xy_inc": [-0.1234, -0.1234]}', "PUT"],
        #     [Op.RA, ["xy"]],
        #     [Op.GC, '{"xy":[0.24, 0.15]}', "PUT"],
        #     [Op.GC, '{"xy_inc": [0.0, 0.0]}', "PUT"],
        #     [Op.RA, ["xy"]],
        #     [Op.GC, '{"xy":[0.3, 0.15]}', "PUT"],
        #     [Op.GC, '{"xy_inc": [0.1234, 0.1234]}', "PUT"],
        #     [Op.RA, ["xy"]],
        #     [Op.GC, '{"xy":[0.3, 0.2]}', "PUT"],
        #     [Op.GC, '{"xy_inc": [0.2, 0.2]}', "PUT"],
        #     [Op.RA, ["xy"]]
        # ],
        # "TC6": [
        #     [Op.GC, '{"bri":75}', "PUT"],
        #     [Op.GC, '{"hue":10000}', "PUT"],
        #     [Op.MSG, "Increase bri and hue for 5 times"],
        #     [Op.GC, '{"bri_inc": -1}', "PUT", 5],
        #     [Op.GC, '{"hue_inc": 10000}', "PUT", 5],
        #     [Op.RA, ["bri", "hue"]],
        #     [Op.GC, '{"bri":150}', "PUT"],
        #     [Op.GC, '{"hue":10000}', "PUT"],
        #     [Op.MSG, "Increase bri and hue for 10 times"],
        #     [Op.GC, '{"bri_inc": 1}', "PUT", 10],
        #     [Op.GC, '{"hue_inc": -10000}', "PUT", 10],
        #     [Op.RA, ["bri", "hue"]],
        #     [Op.GC, '{"bri":250}', "PUT"],
        #     [Op.GC, '{"hue":10000}', "PUT"],
        #     [Op.MSG, "Increase bri and hue for 20 times"],
        #     [Op.GC, '{"bri_inc": -10}', "PUT", 20],
        #     [Op.GC, '{"hue_inc": 10000}', "PUT", 20],
        #     [Op.RA, ["bri", "hue"]],
        #     [Op.GC, '{"bri":100}', "PUT"],
        #     [Op.GC, '{"hue":10000}', "PUT"],
        #     [Op.MSG, "Increase bri and hue for 3 times"],
        #     [Op.GC, '{"bri_inc": 10}', "PUT", 3],
        #     [Op.GC, '{"hue_inc": 10000}', "PUT", 3],
        #     [Op.RA, ["bri", "hue"]],
        #     [Op.GC, '{"bri":200}', "PUT"],
        #     [Op.GC, '{"hue":10000}', "PUT"],
        #     [Op.MSG, "Increase bri and hue for 2 times"],
        #     [Op.GC, '{"bri_inc": -50}', "PUT", 2],
        #     [Op.GC, '{"hue_inc": 10000}', "PUT", 2],
        #     [Op.RA, ["bri", "hue"]],
        #     [Op.GC, '{"bri":200}', "PUT"],
        #     [Op.GC, '{"hue":10000}', "PUT"],
        #     [Op.MSG, "Increase bri and hue for 6 times"],
        #     [Op.GC, '{"bri_inc": 50}', "PUT", 6],
        #     [Op.GC, '{"hue_inc": 10000}', "PUT", 6],
        #     [Op.RA, ["bri", "hue"]]
        #  ],
        # "TC7": [
        #     [Op.MSG, "Before transition finished, press button to continue"],
        #     [Op.GC, '{"bri":254}', "PUT"],
        #     [Op.GC, '{"bri":1, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri_inc": -200}', "PUT"],
        #     [Op.RA, ["bri"]],
        #     [Op.GC, '{"bri":254}', "PUT"],
        #     [Op.GC, '{"bri":1, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri_inc": 0}', "PUT"],
        #     [Op.RA, ["bri"]],
        #     [Op.GC, '{"bri":254}', "PUT"],
        #     [Op.GC, '{"bri":1, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri_inc": -0}', "PUT"],
        #     [Op.RA, ["bri"]],
        #     [Op.GC, '{"bri":254}', "PUT"],
        #     [Op.GC, '{"bri":1, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri_inc": 200}', "PUT"],
        #     [Op.RA, ["bri"]]
        # ],
        "TC8": [
            [Op.MSG, "Before transition finished, press button to continue"],
            [Op.GC, '{"ct":500}', "PUT"],
            [Op.GC, '{"ct":153, "transitiontime":100}', "PUT"],
            [Op.GC, '{"hue_inc": -10}', "PUT"],
            [Op.RA, ["ct"]],
            [Op.GC, '{"ct":500}', "PUT"],
            [Op.GC, '{"ct":153, "transitiontime":100}', "PUT"],
            [Op.GC, '{"sat_inc": -10}', "PUT"],
            [Op.RA, ["ct"]],
            [Op.GC, '{"ct":500}', "PUT"],
            [Op.GC, '{"ct":153, "transitiontime":100}', "PUT"],
            [Op.GC, '{"xy_inc": [0.1, 0.1]}', "PUT"],
            [Op.RA, ["ct"]]
        ],
        "TC9": [
            [Op.MSG, "Before transition finished, press button to continue"],
            [Op.GC, '{"hue":65534}', "PUT"],
            [Op.GC, '{"hue":1, "transitiontime":100}', "PUT"],
            [Op.GC, '{"ct_inc": -10}', "PUT"],
            [Op.RA, ["hue"]],
            [Op.GC, '{"hue":65534}', "PUT"],
            [Op.GC, '{"hue":1, "transitiontime":100}', "PUT"],
            [Op.GC, '{"xy_inc": [0.1, 0.1]}', "PUT"],
            [Op.RA, ["hue"]]
        ],
        "TC10": [
            [Op.MSG, "Before transition finished, press button to continue"],
            [Op.GC, '{"sat":254}', "PUT"],
            [Op.GC, '{"sat":1, "transitiontime":100}', "PUT"],
            [Op.GC, '{"ct_inc": -10}', "PUT"],
            [Op.RA, ["sat"]],
            [Op.GC, '{"sat":254}', "PUT"],
            [Op.GC, '{"sat":1, "transitiontime":100}', "PUT"],
            [Op.GC, '{"xy_inc": [0.1, 0.1]}', "PUT"],
            [Op.RA, ["sat"]]
        ],
        "TC11": [
            [Op.MSG, "Before transition finished, press button to continue"],
            [Op.GC, '{"xy":[0.1, 0.1]}', "PUT"],
            [Op.GC, '{"xy":[0.1, 0.1], "transitiontime":100}', "PUT"],
            [Op.GC, '{"ct_inc": -10}', "PUT"],
            [Op.RA, ["xy"]],
            [Op.GC, '{"xy":[0.1, 0.1]}', "PUT"],
            [Op.GC, '{"xy":[0.1, 0.1], "transitiontime":100}', "PUT"],
            [Op.GC, '{"hue_inc": -10}', "PUT"],
            [Op.RA, ["xy"]],
            [Op.GC, '{"xy":[0.1, 0.1]}', "PUT"],
            [Op.GC, '{"xy":[0.1, 0.1], "transitiontime":100}', "PUT"],
            [Op.GC, '{"xy_inc": [0.1, 0.1]}', "PUT"],
            [Op.RA, ["xy"]]
        ],
        "TC12": [
            [Op.GC, '{"ct":200}', "PUT"],
            [Op.GC, '{"hue_inc": 10000}', "PUT"],
            [Op.RA, ["colormode"]],
            [Op.GC, '{"ct":200}', "PUT"],
            [Op.GC, '{"sat_inc": 50}', "PUT"],
            [Op.RA, ["colormode"]],
            [Op.GC, '{"ct":200}', "PUT"],
            [Op.GC, '{"xy_inc": [0.1, 0.1]}', "PUT"],
            [Op.RA, ["colormode"]]
        ],
        "TC13": [
            [Op.GC, '{"hue":40000}', "PUT"],
            [Op.GC, '{"ct_inc": 100}', "PUT"],
            [Op.RA, ["colormode"]],
            [Op.GC, '{"hue":30000}', "PUT"],
            [Op.GC, '{"xy_inc": [0.1, 0.1]}', "PUT"],
            [Op.RA, ["colormode"]]
        ],
        "TC14": [
            [Op.GC, '{"sat":100}', "PUT"],
            [Op.GC, '{"ct_inc": 100}', "PUT"],
            [Op.RA, ["colormode"]],
            [Op.GC, '{"sat":100}', "PUT"],
            [Op.GC, '{"xy_inc": [0.1, 0.1]}', "PUT"],
            [Op.RA, ["colormode"]]
        ],
        "TC15": [
            [Op.GC, '{"xy": [0.5, 0.5]}', "PUT"],
            [Op.GC, '{"ct_inc": 10}', "PUT"],
            [Op.RA, ["colormode"]],
            [Op.GC, '{"xy": [0.5, 0.5]}', "PUT"],
            [Op.GC, '{"hue_inc": 10}', "PUT"],
            [Op.RA, ["colormode"]],
            [Op.GC, '{"xy": [0.5, 0.5]}', "PUT"],
            [Op.GC, '{"sat_inc": 10}', "PUT"],
            [Op.RA, ["colormode"]]
        ],
        "TC16": [
            [Op.MSG, "Need to connect to the portal"]
        ],
        "TC17": [
            [Op.MSG, "Need to connect to the portal"]
        ],
        "TC18": [
            [Op.MSG, "Need to connect to the portal"]
        ],
        "TC19": [
            [Op.MSG, "Need to connect to the portal"]
        ],
        "TC20": [
            [Op.MSG, "Need to connect to the portal"]
        ],
        "TC21": [
            [Op.GC, '{"bri": 10}', "PUT"],
            [Op.GC, '{"bri_inc": -1000000}', "PUT"]
        ],
        "TC22": [
            [Op.CS, '{"bri_inc":10}'],
            [Op.CS, '{"ct_inc":-10}'],
            [Op.CS, '{"hue_inc":10000}'],
            [Op.CS, '{"sat_inc":25}'],
            [Op.CS, '{"xy_inc":[0.1, 0.1]}']
        ],
        "new_case1": [
            [Op.GC, '{"hue":65535}', "PUT"],
            [Op.GC, '{"hue":20000, "transitiontime":200}', "PUT"],
            [Op.GC, '{"sat_inc": -100}', "PUT"],
            [Op.RA, ["hue"]],
            [Op.GC, '{"sat":254}', "PUT"],
            [Op.GC, '{"sat":1, "transitiontime":200}', "PUT"],
            [Op.GC, '{"hue_inc": 10000}', "PUT"],
            [Op.RA, ["sat"]],
        ],
        "new_case2": [
            [Op.GC, '{"ct":454, "bri":50}', "PUT"],
            [Op.GC, '{"ct":153, "transitiontime":200}', "PUT"],
            [Op.GC, '{"bri_inc": 50}', "PUT"],
            [Op.RA, ["ct", "bri"]],
            [Op.GC, '{"xy":[0.17, 0.7], "bri":50}', "PUT"],
            [Op.GC, '{"xy":[0.6925, 0.3083], "transitiontime":200}', "PUT"],
            [Op.GC, '{"bri_inc": 50}', "PUT"],
            [Op.RA, ["xy", "bri"]],
            [Op.GC, '{"hue":65535, "bri":50}', "PUT"],
            [Op.GC, '{"hue":20000, "transitiontime":200}', "PUT"],
            [Op.GC, '{"bri_inc": 50}', "PUT"],
            [Op.RA, ["hue", "bri"]],
            [Op.GC, '{"sat":254, "bri":50}', "PUT"],
            [Op.GC, '{"sat":0, "transitiontime":200}', "PUT"],
            [Op.GC, '{"bri_inc": 50}', "PUT"],
            [Op.RA, ["sat", "bri"]]
        ]
    }

    try:
        Process_case.process_case(Attribute_Tcs, TCs_list, TCs_body, group_number, light_list, scene_name="att_scene")
    finally:
        Attribute_Tcs.write_log_all("Attribute_increment", "./logs/system_test/Attribute")
