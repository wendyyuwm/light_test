#!/usr/bin/python2.7

import RFTest

__author__ = 'WendyYu'

if __name__ == '__main__':
    light_list = [1, 2, 3]
    body_list = ['{"on":false}', '{"on":true}']
    try:
        i = 0
        while True:
            i += 1
            print "\nRF Stress Test Round %d" % i
            RFTest.stress(light_list, body_list)
            RFTest.RF_stress_test.write_log_all("RF_Stress_test", "./logs/RF_Stress_Test")

    except KeyboardInterrupt:
        input("\nPress any key to quit...")

    except Exception as e:
        print "\n\033[1;31;0m%s\033[0m" % e
