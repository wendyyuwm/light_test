#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.4308, 0.5042], "bri":254}', '{"xy":[0.4308, 0.5042], "bri":1, "transitiontime":600}',
                     '{"xy":[0.1616, 0.3738], "bri":254}', '{"xy":[0.1616, 0.3738], "bri":1, "transitiontime":600}',
                     '{"xy":[0.4224, 0.1779], "bri":254}', '{"xy":[0.4224, 0.1779], "bri":1, "transitiontime":600}']

    try:
        # while True:
        print "\nColor gamut middle point for bri transition test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_bri_TC3", "./logs/color_gamut_bri")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")
