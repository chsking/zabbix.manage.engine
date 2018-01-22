#!/usr/bin/env python# -*- coding: utf-8 -*-# Author: Yuanbin# Datetime: 20180110from __init__ import *class Item:    def __init__(self, zbx_base=None):        self.zb = zbx_base        self.url = self.zb.url        self.header = self.zb.header        self.authID = self.zb.auth    def create(self, **kwargs):        '''        type: (如下表所示)            0 - Zabbix agent;1 - SNMPv1 agent;2 - Zabbix trapper;3 - simple check;4 - SNMPv2 agent;5 - Zabbix internal;            6 - SNMPv3 agent;7 - Zabbix agent (active);8 - Zabbix aggregate;9 - web item;10 - external check;            11 - database monitor;12 - IPMI agent;13 - SSH agent;14 - TELNET agent;15 - calculated;            16 - JMX agent;17 - SNMP trap.        value_type：            0 - numeric float; 1 - character; 2 - log; 3 - numeric unsigned; 4 - text.        :param kwargs:        :return:        '''        json_data = {            "jsonrpc": "2.0",            "method": "item.create",            "params": {},            "auth": self.authID,            "id": 1        }        # 解析参数kwargs        for k, v in kwargs.items():            json_data['params'][k] = v        data = json.dumps(json_data)        try:            result = requests.post(self.url, data=data, headers=self.header)            response = json.loads(result.content)            res = response['result']            if (res != 0) and (len(res) != 0):                item_res = response['result']            print "创建监控项成功:\t%s" % item_res        except Exception, e:            message = u'创建监控项（Create Item failure）失败!'            print message, e            traceback.print_exc()            return False        return item_res    def delete(self, *args):        json_data = {            "jsonrpc": "2.0",            "method": "item.delete",            "params": [],            "auth": self.authID,            "id": 1        }        json_data['params'].extend(args)        data = json.dumps(json_data)        try:            result = requests.post(self.url, data=data, headers=self.header)            response = json.loads(result.content)            res = response['result']            if (res != 0) and (len(res) != 0):                item_res = response['result']            print "删除监控项成功:\t%s" % item_res        except Exception, e:            message = u'删除监控项（Delete Item failure）失败!'            print message, e            traceback.print_exc()            return False        return item_res    def get(self, **kwargs):        json_data = {            "jsonrpc": "2.0",            "method": "item.get",            "params": {},            "auth": self.authID,            "id": 1        }        for k, v in kwargs.items():            json_data['params'][k] = v        data = json.dumps(json_data)        try:            result = requests.post(self.url, data=data, headers=self.header)            response = json.loads(result.content)            res = response['result']            if (res != 0) and (len(res) != 0):                item_res = response['result']            print "获取监控项成功:\t%s" % item_res        except Exception, e:            message = u"获取监控项(Get Item failure)失败!"            print message, e            return False        return item_res    def update(self, **kwargs):        json_data = {            "jsonrpc": "2.0",            "method": "item.update",            "params": {},            "auth": self.authID,            "id": 1        }        for k, v in kwargs.items():            json_data['params'][k] = v        data = json.dumps(json_data)        try:            result = requests.post(self.url, data=data, headers=self.header)            response = json.loads(result.content)            res = response['result']            if (res != 0) and (len(res) != 0):                item_res = response['result']            print "更新监控项成功:\t%s" % item_res        except Exception, e:            message = u"更新监控项(Update Item failure)失败!"            print message, e            return False        return item_res