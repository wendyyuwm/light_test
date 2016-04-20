#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.6915, 0.3083], "bri":2, "transitiontime":600}',
                     '{"xy":[0.1700, 0.7000], "bri":2, "transitiontime":600}',
                     '{"xy":[0.1532, 0.04755], "bri":2, "transitiontime":600}',
                     '{"xy":[0.6915, 0.3083], "bri":2, "transitiontime":600}']

    try:
        # while True:
        print "\nColor gamut top point and bri:1, tt:600 test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC29", "./logs/color_gamut")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
