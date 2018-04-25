import json
import time
from server.models import Host
from server.config import *
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import pymongo

TIME_SECTOR = (
            3600,
            3600*3,
            3600*5,
            86400,
            86400*3,
            86400*7,
)

# 接受客户端数据
@csrf_exempt
def received_sys_info(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        machine_id = received_json_data["machine_id"]
        received_json_data['timestamp'] = int(time.time())
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        collection = db[machine_id]
        collection.insert_one(received_json_data)
        return HttpResponse("Post the system Monitor Data successfully!")
    else:
        return HttpResponse("Your push have errors, Please Check your data!")

def get_sys_data(request):
    # client = pymongo.MongoClient(MONGO_URL)
    # db = client[MONGO_DB]
    # cursor = db['M-001'].find().sort([("timestamp", -1)]).limit(1)
    # for item in cursor:
    #     cpu_percent = item['cpu']['percent']

    all_host = Host.objects.all()
    return render(request,'monitor/index.html',locals())

def host_info(request,machine_id,timing):
    temp_name = "monitor/monitor-header.html"
    # 传递磁盘号给前端JS,用以迭代分区图表

    partitions_len = [1,2,3,4]

    # 传递网卡号给前端,用以迭代分区图表

    nic_len = [1,2,3,4]

    return render(request, "monitor/host_info_{}.html".format(timing), locals())

import random
def get_cpu(request, hostname, timing):
    data_time = ['26/04-01:22','26/04-01:24','26/04-01:26','26/04-01:28','26/04-01:30','26/04-01:32']
    cpu_percent = []
    for i in range(6):
        cpu_percent.append(random.random()*100)

    # range_time = TIME_SECTOR[int(timing)]
    # cpu = {"user": 42687.3125, "system": 57074.703125, "idle": 268005.28125, "percent": 24.9},
    # cpu_data = GetSysData(hostname, "cpu", range_time)
    # for doc in cpu_data.get_data():
    #     unix_time = doc['timestamp']
    #     times = time.localtime(unix_time)
    #     dt = time.strftime("%m%d-%H:%M", times)
    #     data_time.append(dt)
    #     c_percent = doc['cpu']['percent']
    #     cpu_percent.append(c_percent)
    data = {"data_time": data_time, "cpu_percent": cpu_percent}
    return HttpResponse(json.dumps(data))