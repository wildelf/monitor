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
        client = pymongo.MongoClient(MONGO_URL)
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
        print(received_json_data)
        machine_id = received_json_data["machine_id"]
        ip = received_json_data['ip']
        obj = models.Host.objects.filter(machine_id=machine_id, ip=ip)
        if not obj:
            try:
                models.Host.objects.create(machine_id=machine_id, ip=ip)
            except Exception as e:
                return HttpResponse(e)
        received_json_data['timestamp'] = int(time.time())
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        collection = db[machine_id]
        collection.insert_one(received_json_data)
        return HttpResponse("Post the system Monitor Data successfully!")
    else:
        return HttpResponse("Your push have errors, Please Check your data!")

