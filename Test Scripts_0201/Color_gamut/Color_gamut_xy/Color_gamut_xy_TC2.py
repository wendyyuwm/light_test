#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    # hue_body_list = ['{"xy":[0.7115, 0.3083]}', '{"xy":[0.4308, 0.5242]}',
    #                  '{"xy":[0.1700, 0.72]}',  '{"xy":[0.1416, 0.3738]}',
    #                  '{"xy":[0.1332, 0.04755]}', '{"xy":[0.4224, 0.1579]}',
    #                  '{"xy":[0.7115, 0.3083]}']
    hue_body_list = ['{"xy":[0.7415, 0.3083]}', '{"xy":[0.4308, 0.5542]}',
                     '{"xy":[0.1700, 0.75]}',  '{"xy":[0.1116, 0.3738]}',
                     '{"xy":[0.1032, 0.04755]}', '{"xy":[0.4224, 0.1279]}',
                     '{"xy":[0.7415, 0.3083]}']

    try:
        # while True:
        print "\nOutside Color gamut test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC2", "./logs/color_gamut")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
