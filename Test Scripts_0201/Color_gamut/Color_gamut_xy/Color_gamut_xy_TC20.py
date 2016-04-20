#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.5267, 0.4133], "bri":254, "transitiontime":600}',
                     '{"xy":[0.5056, 0.4152], "bri":254, "transitiontime":600}',
                     '{"xy":[0.4578, 0.4101], "bri":254, "transitiontime":600}',
                     '{"xy":[0.4369, 0.4041], "bri":254, "transitiontime":600}',
                     '{"xy":[0.3804, 0.3768], "bri":254, "transitiontime":600}',
                     '{"xy":[0.3135, 0.3267], "bri":254, "transitiontime":600}']

    try:
        # while True:
        print "\nBBL(2000k-2200k-2700k-3000k-4000k-6500k) and bri:254, tt:600 test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC20", "./logs/color_gamut_xy")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
