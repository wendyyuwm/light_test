# -*- coding: utf-8 -*-
# !/usr/bin/python2.7

import os
import requests
import time
import json
import ConfigParser

__author__ = 'WendyYu'


class LampTest:

    def __init__(self, bridge_ip=None, username=None):
        """
        Version: v1.0.0
        :param bridge_ip and username: default is None, get them from bridge.cfg file
        :return: None
        """
        if bridge_ip is not None and username is not None:
            self._ip = bridge_ip
            self._user = username
        else:
            cf = ConfigParser.ConfigParser()
            cf.read("bridge.cfg")
            self._ip = cf.get('Config', 'BridgeIp')
            self._user = cf.get('Config', 'ValidUser')
        self._pre_url = "http://" + self._ip + "/api/" + self._user
        self._sceneID = ''
        self._scene_body = ''
        self.msg_list = []
        information = '='*120 + '\n'*2 + '\t'*3+"BridgeIp: "+self._ip+'\n'+'\t'*3+"UserName: "+self._user \
                      + '\n'*2 + '=' * 120
        self.msg_list.append(information)
        self._day = time.strftime("%Y-%m-%d", time.localtime())
        self._day = time.strftime("%Y-%m-%d", time.localtime())

    def command(self, method, suffix_url=None, body=None):
        """
        :param method: "get", "put","post","delete"(upper or lower case are all Ok)
        :param suffix_url: it is like "/groups/0/action"
        :param body: The format for body is just like {"on":True}
                 => Attention: if use true or false for on, please capitalize the first letter
        :return: "Error" if not successful else return None
        """
        if suffix_url is not None:
            url = self._pre_url + suffix_url
        else:
            url = self._pre_url
        # print url + '\t' + method
        real_time = time.strftime("%H:%M:%S", time.localtime())
        self.msg_list.append('\n' * 2 + self._day + '\t' + real_time + '\n' + '\t' * 2 + suffix_url + '\t' + method.upper() +
                             '\n')
        if method.lower() == "get":
            response = requests.get(url)
        elif method.lower() == "post":
            if body is not None:
                # print json.dumps(body)
                self.msg_list.append('\t' * 2 + body + '\n')
                response = requests.post(url, body)
            else:
                response = requests.post(url)
        elif method.lower() == "delete":
            response = requests.delete(url)
        elif method.lower() == 'put':
            if body is None:
                response = requests.put(url)
            else:
                # print json.dumps(body)
                self.msg_list.append('\t' * 2 + body + '\n')
                response = requests.put(url, body)
        else:
            print "Error: Input wrong method\n"
            return None
        return response.text

    def write_log_all(self, file_name, path, msg_list=None):
        """
        :param file_name: file name for log
        :param path: Path for log
        :param msg_list: Default is none, the mes_lisg generate by this class
        :return: "Error" if not successful else return None
        """
        random_num = time.strftime("%H%M%S", time.localtime())
        if path:
            if os.path.exists(path) == 0:
                os.makedirs(path)
            file_path = os.path.join(path, file_name)
            logfile = open("%s_%s_%s.log" % (file_path, self._day, random_num), 'w')
        if msg_list is None:
            msg_list = self.msg_list
        for msg in msg_list:
            logfile.write(msg)
            logfile.flush()
        logfile.write('\n'*2+"Finished Test")
        logfile.close()

    def uni_cast(self, method, lights_list, body=None):
        """
        :param method: 'put','delete','get','post'(Upper or lower case are all Ok)
        :param lights_list: it is just like [1,2,3]
        :param body: The format for body is just like {"on":True}
                 => Attention: if use true or false for on, please capitalize the first letter
        :return: "Error" if not successful else return None
        """
        if lights_list:
            err_flag = 0
            for light in lights_list:
                append_url = '/lights/' + str(light)
                if method.lower() == 'put' and body is not None:
                    put_suffix_url = append_url + '/state'
                    response = self.command(method, put_suffix_url, body)
                else:
                    response = self.command(method, append_url)
                real_time = time.strftime("%H:%M:%S", time.localtime())
                self.msg_list.append('\t' + real_time + '\n' + '\t' * 2 + response + '\n')
                time.sleep(3)
                if "error" in response:
                    err_flag += 1
                    print response + '\n'
            if err_flag != 0:
                return "ERROR!!!"

    def group_cast(self, method, group_num=None, body=None):
        """
        :param method: 'put','delete','get','post'(Upper or lower case are all Ok)
        :param group_num: group number
        :param body: The format for body is just like {"on":True}
                 => Attention: if use true or false for on, please capitalize the first letter
        :return: "Error" if not successful else return None
        """
        if group_num is None:
            append_url = '/groups'
        else:
            append_url = '/groups/'+str(group_num)
        if method.lower() == 'put' and body is not None:
            put_suffix_url = append_url + '/action'
            response = self.command(method, put_suffix_url, body)
        else:
            response = self.command(method)
        real_time = time.strftime("%H:%M:%S", time.localtime())
        # print response+'\n'
        self.msg_list.append('\t' + real_time + '\n' + '\t' * 2 + response + '\n')
        if "error" in response.lower():
            return "ERROR!!!"

    def create_item(self, item_name, name, lights_list, recycle=None):
        """
        :param item_name: The item want to know the id (eg:group, scene and so on)
        :param name: Name for this item (eg: group1)
        :param lights_list: lights for create items
        :param recycle: used for create scenes
        :return: id for this item, type is string
        """
        str_lights_list = []
        for light in lights_list:
            str_lights_list.append(str(light))
        append_url = '/%ss' % item_name
        if recycle is None:
            body = '{"name":"%s","lights":%s}' % (name, json.dumps(str_lights_list))
        else:
            body = '{"name":"%s","lights":%s, "recycle":%s}' % (name, json.dumps(str_lights_list), json.dumps(recycle))
        print body
        item_response = self.command("post", append_url, body)
        real_time = time.strftime("%H:%M:%S", time.localtime())
        print item_response + '\n'
        self.msg_list.append('\t' + real_time + '\n' + '\t' * 2 + item_response + '\n')
        if "success" in item_response.lower():
            index_id_begin = item_response.find('id')
            index_id_begin += 5
            index_id_end = item_response.find('"}')
            id_number = item_response[index_id_begin: index_id_end]
            return id_number
        else:
            return "ERROR!!!"

    def create_scene(self, scene_name, lights_list, light_body=None, recycle=True, set_in_background=True):
        """
        :param scene_name: The name for the scene
        :param lights_list: it is just like [1,2,3]
        :param light_body:  The format for body is just like {"on":True}
                        => Attention: if use true or false for on, please capitalize the first letter
        :param set_in_background: True or False, default is True
        :param recycle: True or False, default is True
        :return:"Error" if not successful else return None
        """
        err_flag = 0
        real_time = time.strftime("%H:%M:%S", time.localtime())
        self._sceneID = self.create_item("scene", scene_name, lights_list, recycle)
        time.sleep(2)
        if set_in_background is True and light_body is not None:
            for light in lights_list:
                suffix_url = "/scenes/%s/lightstates/%s" % (self._sceneID, str(light))
                response = self.command("PUT", suffix_url, light_body)
                # print response
                self.msg_list.append('\t' + real_time + '\n' + '\t' * 2 + response + '\n')
                if "error" in response.lower():
                    print response + '\n'
                    err_flag += 1
                time.sleep(1)
        elif set_in_background is False:
            return None
        else:
            return "ERROR!!!"
        if "error" in self._sceneID.lower() or err_flag != 0:
            return "ERROR!!!"

    def recall_scene(self, group_num, scene_id=None):
        """
        Recall the existed scene
        :param group_num: group number for the recalled scene
        :param scene_id: if not set it, using scene Id in create_scene operation
                        set the scene_id for the one recalled (scene_id must exist)
        :return: "Error" if not successful else return None
        """
        if scene_id is None:
            body = '{"scene":"%s"}' % self._sceneID
        else:
            body = '{"scene":"%s"}' % scene_id
        suffix_url = '/groups/%s/action' % str(group_num)
        recall_response = self.command("PUT", suffix_url, body)
        real_time = time.strftime("%H:%M:%S", time.localtime())
        # print recall_response + '\n'
        self.msg_list.append('\t' + real_time + '\n' + '\t' * 2 + recall_response + '\n')
        if "error" in recall_response.lower():
            return "ERROR!!!"

    def scene_operation(self, operate, body=None, scene_id=None):
        """
        scene_operation include get scene details, delete scene and modify scene
        :param operate: "get" and "delete", others are invalid
        :param body: The format for body is just like {"on":True}
                 => Attention: if use true or false for on, please capitalize the first letter
        :param scene_id: if not set it, using scene Id in create_scene operation
                        set the scene_id for the one delete or Get details (scene_id must exist)
        :return: "Error" if not successful else return None
        """
        if scene_id is None:
            scene_suffix_url = "/scenes/%s" % self._sceneID
        else:
            scene_suffix_url = "/scenes/%s" % scene_id
        if body is None:
            operate_response = self.command(operate, scene_suffix_url)
        else:
            operate_response = self.command(operate, scene_suffix_url, body)
        print operate_response + "\n"
        self.msg_list.append("\t"*2 + operate_response + "\n")
        if "error" in operate_response:
            return "ERROR!!!"

    def read_value(self, attribute_list, lights_list):
        """
        :param attribute_list: "on","bri","ct","xy","hue","sat","effect","alert","colormode","reachable"...
        :param lights_list: All the light which need to know the value
        :return: The value for the light
        """
        for attribute in attribute_list:
            real_time = time.strftime("%H:%M:%S", time.localtime())
            self.msg_list.append('\n' * 2 + self._day + '\t' + real_time + "\n\t\tLight\t\t|\t\t%s\n" % attribute)
            for light in lights_list:
                response = requests.get(self._pre_url + "/lights/%s" % light).text
                if attribute in response:
                    response_list = response.split(",")
                    l = len(response_list)
                    for i in range(l):
                        find_string = json.dumps(attribute) + ":"
                        length = len(find_string)
                        if find_string in response_list[i]:
                            s_id = response_list[i].index(find_string) + length
                            read_value = response_list[i][s_id:]
                            if attribute is "xy":
                                read_value = response_list[i][s_id:] + ", " + response_list[i+1]
                            print "Light %s %s" % (light, find_string + read_value)
                            self.msg_list.append("\t\t%5s\t\t|\t\t%s\n" % (light, read_value))

    def init_lamp(self, group_num):
        initialize_body = {"on": True, "bri": 254, "ct": 333}
        url = self._pre_url + "/groups/%s/action" % str(group_num)
        requests.put(url, json.dumps(initialize_body))

    def effect_none(self, group_num):
        effect_body = {"effect": "none"}
        url = self._pre_url + "/groups/%s/action" % str(group_num)
        requests.put(url, json.dumps(effect_body))
