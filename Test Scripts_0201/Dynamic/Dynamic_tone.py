#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_gu10 = 3
    gu10_light_list = [53, 32, 31, 28, 22, 14, 11, 42, 36, 38, 19, 41, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    gu10_body_list = ['{"on":true, "bri":50, "ct":153}', '{"bri":160, "ct":250}', '{"on":false, "transitiontime":100}',
                      '{"on":true, "bri":225, "ct":370}', '{"bri":254, "ct":454}', '{"on":false}'
                      ]
    try:
        while True:
            print "\nGu10 and BR30 Tone dynamic Test Start\n"
            Dynamic.execute(group_no_gu10, gu10_light_list, gu10_body_list)
            Dynamic.dynamic_test.write_log_all("Dynamic_Tone", "./logs/dynamic/Tone")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")
