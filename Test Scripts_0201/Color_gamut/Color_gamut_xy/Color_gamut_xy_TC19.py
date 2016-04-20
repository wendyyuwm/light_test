#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.6905, 0.3083], "bri":254, "transitiontime":600}',
                     '{"xy":[0.4308, 0.5032], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1700, 0.699], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1626, 0.3738], "bri":254, "transitiontime":600}',
                     '{"xy":[0.1542, 0.04755], "bri":254, "transitiontime":600}',
                     '{"xy":[0.4224, 0.1789], "bri":254, "transitiontime":600}',
                     '{"xy":[0.6905, 0.3083], "bri":254, "transitiontime":600}']

    try:
        # while True:
        print "\nInside Color gamut and bri:254, tt:600 test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC19", "./logs/color_gamut_xy")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
