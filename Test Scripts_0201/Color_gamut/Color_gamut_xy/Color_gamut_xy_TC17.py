#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.6915, 0.3083], "bri":254, "transitiontime":600}',
                     '{"xy":[0.5611, 0.4062], "bri":254, "transitiontime":600}',
                     '{"xy":[0.4308, 0.5042], "bri":254, "transitiontime":600}',
                     '{"xy":[0.3004, 0.6012], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1700, 0.7000], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1658, 0.5369], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1616, 0.3738], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1574, 0.2107], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1532, 0.04755], "bri":254, "transitiontime":600}',
                     '{"xy":[0.2878, 0.1127], "bri":254, "transitiontime":600}',
                     '{"xy":[0.4224, 0.1779], "bri":254, "transitiontime":600}',
                     '{"xy":[0.5569, 0.2431], "bri":254, "transitiontime":600}',
                     '{"xy":[0.6915, 0.3083], "bri":254, "transitiontime":600}']

    try:
        # while True:
        print "\nColor gamut and bri:254, tt:600 test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC17", "./logs/color_gamut_xy")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
