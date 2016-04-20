#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.6915, 0.3083]}', '{"xy":[0.5611, 0.4062]}',
                     '{"xy":[0.4308, 0.5042]}', '{"xy":[0.3004, 0.6012]}',
                     '{"xy":[0.1700, 0.7000]}', '{"xy":[0.1658, 0.5369]}',
                     '{"xy":[0.1616, 0.3738]}', '{"xy":[0.1574, 0.2107]}',
                     '{"xy":[0.1532, 0.04755]}', '{"xy":[0.2878, 0.1127]}',
                     '{"xy":[0.4224, 0.1779]}', '{"xy":[0.5569, 0.2431]}',
                     '{"xy":[0.6915, 0.3083]}']

    try:
        # while True:
        print "\nColor gamut test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC1", "./logs/color_gamut")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

