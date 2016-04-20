#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 3
    # hue_body_list = ['{"xy":[0.5267, 0.4133]}', '{"xy":[0.5056, 0.4152]}',
    #                  '{"xy":[0.4578, 0.4101]}',  '{"xy":[0.4369, 0.4041]}',
    #                  '{"xy":[0.3804, 0.3768]}', '{"xy":[0.3135, 0.3267]}']
    # hue_body_list = ['"ct": 454', '"ct": 370', '"ct": 333', '"ct": 250', '"ct": 153']

    try:
        # while True:
        print "\nBBL(2000k-2200k-2700k-3000k-4000k-6500k) test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_TC4", "./logs/color_gamut")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
