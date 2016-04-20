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
    # Update Scene
    US = 4
    # Recall Scene
    RS = 5
    # Get scene details
    GS = 6
    # Delete scene
    DS = 7
    # Create group
    CG = 8
    # Update group
    UG = 9
    # Delete group
    DG = 10
    # Read attributes
    RA = 11
    # Print message
    MSG = 12


def sleep(s):
    if s is None:
        s = 1
    time.sleep(s)


def wait_exit(flag, msg=None, s=None):
    if msg is not None:
        print "%s\n" % msg
        input_key = raw_input('Press "n" to quit or other key to continue:')
        sys.exit() if input_key.lower() == "n" else sleep(s)
    elif flag is True:
        input_key = raw_input('Press "n" to quit or other key to continue:')
        sys.exit() if input_key.lower() == "n" else sleep(s)
    elif flag is False:
        sleep(s)


def process_case(tc_operator, tc_list, tcs_body, group_number=None, lights_list=None, scene_name=None):
    """
     :param tc_operator: Initialize the LampTest class
    :param tc_list: A list including all test cases
    :param group_number: The group number for test, if it is none, must create new group
    :param lights_list: A list contain all the lights need test, if it is none, must create new group
    :param tcs_body: The specific content for all test cases
    :param scene_name: Name for the created scene
    :return:
    """
    light_list = None
    group_no = None
    for tc_name in tc_list:
        print "\n" + "*" * 10 + tc_name + "*" * 10
        tc_operator.msg_list.append("\n%s\n" % tc_name)
        tc_body_set = ""
        attribute_list = []
        tc_number = tc_name.strip(" ").split(" ")[1]
        if tc_number in tcs_body.keys():
            tc_steps = tcs_body[tc_number]
            for tc_body in tc_steps:
                l = len(tc_body)
                action = tc_body[0]
                times = 1
                if l >= 2:
                    if type(tc_body[1]) is list:
                        attribute_list = list(tc_body[1])
                    else:
                        tc_body_set = tc_body[1]
                    if l >= 3:
                        method = tc_body[2]
                        if l == 4:
                            times = tc_body[3]
                if group_number is None:
                    if group_no is not None:
                        group_number = group_no
                    else:
                        "\nError: please enter the group number"
                if lights_list is None:
                    if light_list is not None:
                        lights_list = light_list
                    else:
                        "\nError: please enter the lights list"
                for run_time in range(times):
                    if times > 1:
                        print "\n< Times: %s >" % str(int(run_time)+1)
                        tc_operator.msg_list.append("\n< Times: %s >" % str(int(run_time)+1))
                    if action is OpName.GC:
                        print "\nGroup action: " + tc_body_set + "\n"
                        wait_exit(True, tc_operator.group_cast(method, group_number, tc_body_set))

                    elif action is OpName.UC:
                        print "\nUnicast: " + tc_body_set + "\n"
                        wait_exit(True, tc_operator.uni_cast(method, lights_list, tc_body_set))

                    elif action is OpName.CS:
                        if scene_name is not None:
                            if tc_body_set is not None:
                                print "\nCreate Scene: " + tc_body_set + "\n"
                                wait_exit(True, tc_operator.create_scene(scene_name, lights_list,
                                                                         light_body=tc_body_set))
                            else:
                                print "\nCreate Scene on background\n "
                                wait_exit(True, tc_operator.create_scene(scene_name, lights_list,
                                                                         set_in_background=False))

                    elif action is OpName.US:
                        print "\nUpdate the exist Scene\n"
                        option = raw_input("What do you want to update, name(n), lghtslist(l) or both(b): ")
                        if option == "n":
                            new_name = raw_input("Enter the new name: ")
                            new_body = '{"name":"%s"}' % new_name
                        elif option == "l":
                            new_lights = raw_input("Enter the new lights list(eg:1,2): ")
                            light_list = new_lights.split(",")
                            new_body = '{"lights": %s}' % json.dumps(light_list)
                            # wait_exit(False, tc_operator.scene_operation("PUT", body=new_body), 2)
                        elif option == "b":
                            new_name = raw_input("Enter the new name: ")
                            new_lights = raw_input("Enter the new lights list(eg:1,2): ")
                            light_list = new_lights.split(",")
                            new_body = '{"name":"%s", "lights": %s}' % (new_name, json.dumps(light_list))
                        else:
                            print "\nEnter the wrong string"
                            sys.exit()
                        wait_exit(False, tc_operator.scene_operation("PUT", body=new_body), 2)

                    elif action is OpName.RS:
                        print "\nRecall Scene\n"
                        wait_exit(True, tc_operator.recall_scene(group_number), 5)

                    elif action is OpName.GS:
                        print "\nGet Scene details\n"
                        wait_exit(True, tc_operator.scene_operation("GET"))

                    elif action is OpName.DS:
                        print "\nDelete Scene\n"
                        wait_exit(False, tc_operator.scene_operation("DELETE"), 2)

                    elif action is OpName.CG:
                        print "\nCreate a new Group\n"
                        lights_list = None
                        group_number = None
                        group_name = raw_input("Please enter the group name: ")
                        all_lights = raw_input("Please enter the light list(eg:1,2,3): ")
                        light_list = all_lights.split(",")
                        group_no = tc_operator.create_item("group", group_name, light_list)

                    elif action is OpName.UG:
                        print "\nUpdate the exist Group\n"
                        option = raw_input("What do you want to update, name(n), lights(l) or both(b): ")
                        group_no = raw_input("Please enter the group number: ")
                        group_number = None
                        url_append = "/groups/%s" % group_no
                        if option == "n":
                            new_name = raw_input("Enter the new name: ")
                            new_body = '{"name":"%s"}' % new_name
                            response = tc_operator.command("GET", url_append)
                            if '"lights":' in response:
                                id_start = response.find("[")
                                id_end = response.find("]")
                                lights_list = json.loads(response[id_start: id_end+1])
                        elif option == "l":
                            lights_list = None
                            lights = raw_input("Enter the new lights list(eg:1,2): ")
                            light_list = lights.split(",")
                            new_body = '{"lights": %s}' % json.dumps(light_list)
                        elif option == "b":
                            lights_list = None
                            new_name = raw_input("Enter the new name: ")
                            lights = raw_input("Enter the new lights list(eg:1,2): ")
                            light_list = lights.split(",")
                            new_body = '{"name":"%s", "lights": %s}' % (new_name, json.dumps(light_list))
                        else:
                            print "\nEnter the wrong command"
                            sys.exit()
                        wait_exit(False, tc_operator.command("PUT", url_append, body=new_body), 2)

                    elif action is OpName.DG:
                        print "\nDelete Group\n"
                        groups_number = raw_input("Please enter the groups number(1,2): ")
                        group_list = groups_number.split(",")
                        for group_number in group_list:
                            url_append = "/groups/%s" % group_number
                            wait_exit(False, tc_operator.command("DELETE", url_append), 2)

                    elif action is OpName.RA:
                        print "\nRead attributes values"
                        sleep(10)
                        wait_exit(True, tc_operator.read_value(attribute_list, lights_list))

                    elif action is OpName.MSG:
                        print "\n\033[1;34;0m%s\033[0m\n" % tc_body_set
                        wait_exit(True)
            tc_operator.msg_list.append("\n" + "*" * 120 + "\n")
            if "colorloop" in tc_body_set:
                tc_operator.effect_none(group_number)
