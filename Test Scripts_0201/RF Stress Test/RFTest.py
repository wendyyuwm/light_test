#!/usr/bin/python2.7

import lamptestclass
import time
import sys

__author__ = 'WendyYu'

RF_stress_test = lamptestclass.LampTest()


def wait_exit(msg=None):
    if msg is not None:
        print msg
        input_key = raw_input('Press "n" to quit or other key to continue:')
        if input_key.lower() == "n":
            sys.exit()


def stress(light_list,  body_list):
    for body in body_list:
        print "*** Command:%s ***" % body
        wait_exit(RF_stress_test.uni_cast("put", light_list, body))
        # time.sleep(1.5)
        RF_stress_test.msg_list.append("\n" + "*" * 120 + "\n")
