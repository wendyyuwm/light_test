#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"bri":1}', '{"bri":254, "transitiontime":600}']

    try:
        # while True:
        print "\nColor gamut point for bri transition test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_bri_TC1", "./logs/color_gamut_bri")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")
