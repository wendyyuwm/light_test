#!/usr/bin/python2.7

import Dynamic
import time

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.6915, 0.3083], "bri":254}', '{"xy":[0.6915, 0.3083], "bri":1}',
                     '{"xy":[0.1700, 0.7000], "bri":254}', '{"xy":[0.1700, 0.7000], "bri":1}',
                     '{"xy":[0.1532, 0.04755], "bri":254}', '{"xy":[0.1532, 0.04755], "bri":1}']

    try:
        # while True:
        print "\nColor gamut point for bri transition test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_bri_TC6", "./logs/color_gamut_bri")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")
