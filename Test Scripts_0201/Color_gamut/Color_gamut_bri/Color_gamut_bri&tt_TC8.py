#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_body_list = ['{"xy":[0.5267, 0.4133], "bri":254}', '{"xy":[0.5267, 0.4133], "bri":1}',
                     '{"xy":[0.5056, 0.4152], "bri":254}', '{"xy":[0.5056, 0.4152], "bri":1}',
                     '{"xy":[0.4578, 0.4101], "bri":254}', '{"xy":[0.4578, 0.4101], "bri":1}',
                     '{"xy":[0.4369, 0.4041], "bri":254}', '{"xy":[0.4369, 0.4041], "bri":1}',
                     '{"xy":[0.3804, 0.3768], "bri":254}', '{"xy":[0.3804, 0.3768], "bri":1}',
                     '{"xy":[0.3135, 0.3237], "bri":254}', '{"xy":[0.3135, 0.3237], "bri":1}']

    try:
        # while True:
        print "\nBBL for bri transition test"
        Dynamic.execute(group_no_hue, hue_body_list)
        Dynamic.color_gamut.write_log_all("Color_gamut_bri_TC8", "./logs/color_gamut_bri")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")
