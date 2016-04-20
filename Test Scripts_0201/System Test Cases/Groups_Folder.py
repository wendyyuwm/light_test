#!/usr/bin/python2.7

import lamptestclass
import Process_case

__author__ = 'WendyYu'


if __name__ == "__main__":
    Op = Process_case.OpName
    Group_Tcs = lamptestclass.LampTest()
    method = "PUT"
    scene_name = "groupscene"
    TCs_list = [" IPJ_13546 TC1 ", " IPJ_13552 TC7 ", " IPJ_13547 TC2 ", " IPJ_13553 TC8 ", " IPJ_13548 TC3 ",
                " IPJ_13554 TC9 ", " IPJ_13549 TC4 ", " IPJ_13555 TC10 ", " IPJ_13550 TC5 ", " IPJ_13556 TC11 ",
                " IPJ_13551 TC6 ", " IPJ_13557 TC12 ",  " IPJ_13558 TC13 ", " IPJ_13559 TC14 ", " IPJ_13560 TC15 ",
                " IPJ_13561 TC16 ", " IPJ_13562 TC17 ", " IPJ_13563 TC18 ", " IPJ_13564 TC19 ", " IPJ_13565 TC20 ",
                " IPJ_13566 TC21 ", " IPJ_13567 TC22 ", " IPJ_13568 TC23 ", " IPJ_13569 TC24 ", " IPJ_13570 TC25 ",
                " IPJ_13571 TC26 ", " IPJ_13572 TC27 ", " IPJ_13573 TC28 ", " IPJ_13574 TC29 ", " IPJ_13575 TC30 ",
                ]

    TCs_body = {
        # "TC1": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC7": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC2": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC8": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC3": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC9": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC4": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC10": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC5": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC11": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC6": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC12": [
        #     [Op.CG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC13": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC14": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC15": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC16": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC17": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC18": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        # "TC19": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        "TC20": [
            [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
            [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
            [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
            [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
            [Op.RS]
        ],
        "TC21": [
            [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
            [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
            [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
            [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
            [Op.RS]
        ],
        # "TC22": [
        #     [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
        #     [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
        #     [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
        #     [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
        #     [Op.RS]
        # ],
        "TC23": [
            [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
            [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
            [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
            [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
            [Op.RS]
        ],
        "TC24": [
            [Op.UG], [Op.UC, '{"on": true, "bri":50, "transitiontime":100}', "PUT"],
            [Op.GC, '{"bri": 100, "ct": 454}', "PUT"], [Op.UC, '{"alert": "select"}', "PUT"],
            [Op.GC, '{"alert": "lselect"}', "PUT"], [Op.GC, '{"alert": "none"}', "PUT"],
            [Op.CS, '{"on": true, "bri": 200, "ct": 250}'],
            [Op.RS]
        ],
        "TC25": [[Op.DG]],
        "TC26": [[Op.DG]],
        "TC27": [[Op.DG]],
        # "TC28": [[Op.DG]],
        "TC29": [[Op.DG]],
        "TC30": [[Op.DG]]
    }

    try:
        Process_case.process_case(Group_Tcs, TCs_list, TCs_body, scene_name=scene_name)

    finally:
        Group_Tcs.write_log_all("Groups_Folder", "./logs/system_test/Groups")
