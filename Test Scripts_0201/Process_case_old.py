#!/usr/bin/python2.7

import time
import sys
import json


__author__ = 'WendyYu'


class OpName(object):
    # Group_cast
    GC = 1
    # Uni_cast
    UC = 2
    # Create scene
    CS = 3
    # Create and recall scene
    CRS = 4
    # Update Scene
    US = 5
    # Recall Scene
    RS = 6
    # Get scene details
    GS = 7
    # Delete scene
    DS = 8
    # Create group
    CG = 9
    # Update group
    UG = 10


def sleep(s):
    if s is None:
        s = 1
    time.sleep(s)


def wait_exit(flag, msg=None, s=None):
    if msg is not None:
        print msg
        input_key = raw_input('Press "n" to quit or other key to continue:')
        sys.exit() if input_key.lower() == "n" else sleep(s)
    elif flag is True:
        input_key = raw_input('Press "n" to quit or other key to continue:')
        sys.exit() if input_key.lower() == "n" else sleep(s)
    elif flag is False:
        sleep(s)


def modify_list(original_list):
    return_list = []
    for item in original_list:
        return_list.append(str(item))
        return json.dumps(return_list)


def process_case(tc_operator, tc_list, group_number, lights_list, tcs_body, scene_name, manual_flag=None):
    """
     :param tc_operator: Initialize the LampTest class
    :param tc_list: A list including all test cases
    :param group_number: The group number for test
    :param lights_list: A list contain all the lights need test
    :param tcs_body: The specific content for all test cases
    :param scene_name: Name for the created scene
    :param manual_flag: If test cases need manual test, set this flag to True
    :return:
    """
    for tc_name in tc_list:
        wait_exit(False, tc_operator.init_lamp(group_number), 2)
        print "\n" + "*" * 10 + tc_name + "*" * 10
        tc_operator.msg_list.append("\n%s\n" % tc_name)
        tc_body_set = ""
        tc_number = tc_name.strip(" ").split(" ")[1]
        if tc_number in tcs_body.keys():
            tc_steps = tcs_body[tc_number]
            for tc_body in tc_steps:
                l = len(tc_body)
                action = tc_body[0]
                times = 1
                if l >= 2:
                    tc_body_set = tc_body[1]
                    if l >= 3:
                        method = tc_body[2]
                        if l == 4:
                            times = tc_body[3]
                for run_time in range(times):
                    if action is OpName.GC:
                        print "\nGroup action: " + tc_body_set + "\n"
                        wait_exit(True, tc_operator.group_cast(method, group_number, tc_body_set), 2)

                    elif action is OpName.UC:
                        print "\nUnicast: " + tc_body_set + "\n"
                        wait_exit(True, tc_operator.uni_cast(method, lights_list, tc_body_set), 2)

                    elif action is OpName.CS:
                        if tc_body_set is not None:
                            print "\nCreate Scene: " + tc_body_set + " and recall scene\n "
                            wait_exit(True, tc_operator.create_scene(scene_name, lights_list, tc_body_set))
                        else:
                            print "\nCreate Scene on background and recall scene\n "
                            wait_exit(True, tc_operator.create_scene(scene_name, lights_list, None, False))

                    elif action is OpName.CRS:
                        if tc_body_set is not None:
                            print "\nCreate Scene: " + tc_body_set + " and recall scene\n "
                            wait_exit(False, tc_operator.create_scene(scene_name, lights_list, tc_body_set))
                        else:
                            print "\nCreate Scene on background and recall scene\n "
                            wait_exit(False, tc_operator.create_scene(scene_name, lights_list, None, False))
                        wait_exit(True, tc_operator.recall_scene(group_number), 2)

                    elif action is (OpName.US and OpName.UG):
                        print "\nUpdate the exist Scene or Group\n"
                        option = raw_input("What do you want to update, name, body or both: ")
                        if option is ("name" and "both"):
                            new_name = raw_input("Enter the new name: ")
                            new_body = '{"name":"%s"}' % new_name
                            wait_exit(False, tc_operator.scene_operation("PUT", body=new_body), 5)
                        elif option is ("body" and "both"):
                            new_light_list = raw_input("Enter the new lights list(eg:[1,2]): ")
                            new_body = '{"lights": %s}' % modify_list(new_light_list)
                            wait_exit(False, tc_operator.scene_operation("PUT", body=new_body), 5)
                        else:
                            print "Enter the wrong string"

                    elif action is OpName.RS:
                        print "\nRecall Scene\n"
                        wait_exit(True, tc_operator.recall_scene(group_number), 2)

                    elif action is OpName.GS:
                        print "\nGet Scene details\n"
                        wait_exit(True, tc_operator.scene_operation("GET"), 5)

                    elif action is OpName.DS:
                        print "\nDelete Scene\n"
                        wait_exit(False, tc_operator.scene_operation("DELETE"), 5)

                    elif action is OpName.CG:
                        print "\nCreate a new Group\n"
                        group_name = raw_input("Please enter the group name: ")
                        group_body = '{"name":"%s", "lights":%s}' % (group_name, modify_list(lights_list))
                        wait_exit(True, tc_operator.command("POST", "/groups", group_body))
                wait_exit(False, tc_operator.read_attributes_values(tc_body_set, lights_list), 2)
            tc_operator.msg_list.append("\n" + "*" * 120 + "\n")
            if "colorloop" in tc_body_set:
                tc_operator.effect_none(group_number)
            if manual_flag is not None:
                print "\nPlease finish the test case manually\n"
                wait_exit(True, None)

