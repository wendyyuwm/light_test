#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_light_list = [15, 16, 17, 22, 18, 20, 23, 19, 21, 24, 4, 12, 11, 6, 1, 5, 9, 8, 2, 13, 7, 3, 14, 10]
    # hue_light_list = [12, 13, 25, 33, 24, 21, 9, 18, 15, 16, 30, 2, 40, 17, 35, 37, 51, 4, 26, 10, 45, 3, 7, 5, 46,
    #                   47, 48, 49, 50]
    hue_body_list = ['{"xy":[0.4308, 0.5042]}', '{"xy":[0.3804, 0.3768]}',
                     '{"xy":[0.1616, 0.3738]}', '{"xy":[0.3804, 0.3768]}',
                     '{"xy":[0.4224, 0.1779]}', '{"xy":[0.3804, 0.3768]}']

    try:
        # while True:
        print "\nColor gamut middle point to 4000k test\n"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC7", "./logs/color_gamut")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
