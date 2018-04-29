#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import pymongo
from server.config import *
from server import models
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class GetSysData(object):

    def __init__(self, machine_id, monitor_item, timing, no=0):
        self.machine_id = machine_id
        self.monitor_item = monitor_item
        self.timing = timing
        self.no = no

    def get_data(self):
        client = pymongo.MongoClient(MONGO_URL,MONGO_PORT)
        db = client[MONGO_DB]
        collection = db[self.machine_id]
        now_time = int(time.time())
        find_time = now_time-self.timing
        cursor = collection.find({'timestamp': {'$gte': find_time}}, {self.monitor_item: 1, "timestamp": 1}).limit(self.no)
        return cursor


# 接受客户端数据
@csrf_exempt
def received_sys_info(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        machine_id = received_json_data["machine_id"]
        pro_mem = received_json_data['mem']['p_mem']
        ip = received_json_data['ip']
        obj = models.Host.objects.filter(machine_id=machine_id, ip=ip)
        if not obj:
            try:
                models.Host.objects.create(machine_id=machine_id, ip=ip)
            except Exception as e:
                return HttpResponse(e)
        insert_mysql(pro_mem,machine_id)#判断是否超过峰值
        received_json_data['timestamp'] = int(time.time())
        client = pymongo.MongoClient(MONGO_URL,MONGO_PORT)
        db = client[MONGO_DB]
        collection = db[machine_id]
        collection.insert_one(received_json_data)
        return HttpResponse("Post the system Monitor Data successfully!")
    else:
        return HttpResponse("Your push have errors, Please Check your data!")

# 超过设定峰值的插入数据库
def insert_mysql(pro_mem,machine_id):

    obj = models.Host.objects.filter(machine_id=machine_id)[0]
    host_id = obj.id
    name = pro_mem[0]
    percent = round(pro_mem[1],2)
    if percent > PROCESS_WARNING:
        try:
            models.ProcessData.objects.create(name=name,percent=percent,host_id=host_id)
        except Exception as e:
            return HttpResponse(e)

