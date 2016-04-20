#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.4308, 0.5242]}', '{"xy":[0.3804, 0.3768]}',
                     '{"xy":[0.1416, 0.3738]}', '{"xy":[0.3804, 0.3768]}',
                     '{"xy":[0.4224, 0.1579]}', '{"xy":[0.3804, 0.3768]}']

    try:
        # while True:
        print "\nOutside color gamut middle point to 4000k test\n"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC8", "./logs/color_gamut")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
