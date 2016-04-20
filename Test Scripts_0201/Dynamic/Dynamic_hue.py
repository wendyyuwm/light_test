#!/usr/bin/python2.7

import Dynamic

__author__ = 'WendyYu'

if __name__ == '__main__':
    group_no_hue = 0
    hue_light_list = [1, 2, 3, 4, 7, 8, 9]
    hue_body_list = ['{"on":true, "bri":150,"ct":454}', '{"effect":"colorloop", "sat":254}', '{"effect":"none"}',
                     '{"on":false,"transitiontime":100}', '{"on":true, "bri":30, "ct":153, "transitiontime":300}',
                     '{"bri":254, "xy":[0.16195, 0.02948], "transitiontime":200}',
                     '{"hue": 4274, "sat": 204}', '{"on":false}', '{"on":true, "bri":254, "xy":[0.67725, 0.32008], '
                                                                  '"transitiontime":600}',
                     '{"hue": 47014, "sat": 172}', '{"on":false, "transitiontime":200}'
                     ]
    try:
        while True:
            print "\nHue dynamic Test Start\n"
            Dynamic.execute(group_no_hue, hue_light_list, hue_body_list)
            Dynamic.dynamic_test.write_log_all("Dynamic_hue", "./logs/dynamic/hue")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")
