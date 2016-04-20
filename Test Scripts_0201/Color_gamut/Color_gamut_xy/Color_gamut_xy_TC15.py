#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.4308, 0.5042], "bri":2}', '{"xy":[0.3804, 0.3768], "bri":2}',
                     '{"xy":[0.1616, 0.3738], "bri":2}', '{"xy":[0.3804, 0.3768], "bri":2}',
                     '{"xy":[0.4224, 0.1779], "bri":2}', '{"xy":[0.3804, 0.3768], "bri":2}']

    try:
        # while True:
        print "\nColor gamut middle point to 4000k and bri:1 test\n"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC15", "./logs/color_gamut_xy")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
