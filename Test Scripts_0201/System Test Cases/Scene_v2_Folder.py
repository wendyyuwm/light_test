#!/usr/bin/python2.7


import lamptestclass
import Process_case

__author__ = 'WendyYu'

if __name__ == '__main__':
    Op = Process_case.OpName
    Scene_v2_TCs = lamptestclass.LampTest()
    one_light_list = [1]
    three_lights_list = [1, 2, 3, 4, 5, 6, 7]
    one_light_group_no = 1
    three_lights_group_no = 0
    scene_name1 = "1_lamp_scene"
    scene_name2 = "3_lamps_scene"
    TCs_list_1_lamp =[" IPJ_16524 TC1 ", " IPJ_16530 TC5 "]
    TCs_list_3_lamps = [" IPJ_16525 TC2 ", " IPJ_16526 TC3 ", " IPJ_16528 TC4 ",  " IPJ_16531 TC6 ", " IPJ_16532 TC7 ",
                        " IPJ_16533 TC8 "]
    # TCs_body_1_lamp = {
    #     "TC1": [
    #         [Op.CS, '{"on": true, "bri": 100}'],
    #         [Op.RS]
    #     ],
    #     "TC5": [
    #         [Op.CS],
    #         [Op.MSG, "Change the color for the test lamp"]
    #         [Op.RS]
    #     ]
    # }
    TCs_body_3_lamps = {
        "TC2": [
            [Op.CS, '{"on": true, "bri": 212, "ct":454, "transitiontime": 10}'],
            [Op.RS],
            [Op.GS]
        ],
        "TC3": [
            [Op.CS, '{"on": false}'],
            [Op.US],
            [Op.MSG, "Change the status for the test lamp"],
            [Op.RS]
        ],
        "TC4": [
            [Op.CS, '{"on": true, "bri": 100, "transitiontime": 100}'],
            [Op.DS],
            [Op.RS]
        ],
        "TC6": [
            [Op.CS],
            [Op.GS]
        ],
        "TC7": [
            [Op.CS],
            [Op.US],
            [Op.MSG, "Change the status for the test lamp"],
            [Op.RS]
        ],
        "TC8": [
            [Op.CS],
            [Op.DS],
            [Op.RS]
        ]
    }

    try:
        # Process_case.process_case(Scene_v2_TCs, TCs_list_1_lamp, TCs_body_1_lamp, one_light_group_no, one_light_list,
        #                           scene_name1)
        Process_case.process_case(Scene_v2_TCs, TCs_list_3_lamps, TCs_body_3_lamps, three_lights_group_no,
                                  three_lights_list, scene_name2)

    finally:
        Scene_v2_TCs.write_log_all("Scene_v2", "./logs/system_test/Scene_V2")
