#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.6915, 0.3083], "bri":2}', '{"xy":[0.3804, 0.3768], "bri":2}',
                     '{"xy":[0.1700, 0.7000], "bri":2}', '{"xy":[0.3804, 0.3768], "bri":2}',
                     '{"xy":[0.1532, 0.04755], "bri":2}', '{"xy":[0.3804, 0.3768], "bri":2}']

    try:
        # while True:
        print "\nColor gamut top point to 4000k and bri:1 test\n"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC14", "./logs/color_gamut_xy")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
