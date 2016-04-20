#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    # group_no_lux = 2
    group_no_lux = 0
    # lux_light_list = [29, 23, 20, 1, 43, 8, 44, 27, 6, 39, 34, 52]
    lux_light_list = [1, 2, 4, 5, 7, 9, 10, 11, 12, 16, 17, 18, 19]
    lux_body_list = ['{"on":true, "bri":1, "transitiontime":50}', '{"bri":254}',
                     '{"on":false, "transitiontime":50}', '{"on":true, "bri":160}',
                     '{"on":true, "bri":225}', '{"bri":254}',
                     '{"on":false}'
                     ]
    try:
        while True:
            print "\nLux dynamic Test Start"
            Dynamic.execute(group_no_lux, lux_light_list, lux_body_list)
            Dynamic.dynamic_test.write_log_all("Dynamic_lux", "./logs/dynamic/lux")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")
