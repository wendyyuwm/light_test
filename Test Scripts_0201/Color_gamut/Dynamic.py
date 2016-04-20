#!/usr/bin/python2.7

import lamptestclass
import time
import sys

__author__ = 'WendyYu'

color_gamut = lamptestclass.LampTest()


def sleep(s):
    if s is None:
        s = 1
    time.sleep(s)


def wait_exit(msg=None, s=None):
    if msg is not None:
        print msg
        input_key = raw_input('Press "n" to quit or other key to continue:')
        sys.exit() if input_key.lower() == "n" else sleep(s)
    else:
        sleep(s)


def execute(group_no, body_list):
    for body in body_list:
        print "\n********** Command:%s **********" % body
        wait_exit(color_gamut.group_cast("put", group_no, body), 5)
        if "transitiontime" in body:
            id_start = body.find('"transitiontime":')
            l = len('"transitiontime":')
            id_end = body.find("}")
            s = int(body[(id_start+l):id_end])/10
            time.sleep(s)
        color_gamut.msg_list.append("\n" + "*" * 120 + "\n")
