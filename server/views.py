import json
import time
from server.models import Host
from django.shortcuts import render,HttpResponse
from server import models
from server.api import GetSysData

TIME_SECTOR = (
            3600,
            3600*3,
            3600*5,
            86400,
            86400*3,
            86400*7,
)


# 返回首页
def get_sys_data(request):
    # client = pymongo.MongoClient(MONGO_URL)
    # db = client[MONGO_DB]
    # cursor = db['M-001'].find().sort([("timestamp", -1)]).limit(1)
    # for item in cursor:
    #     cpu_percent = item['cpu']['percent']

    all_host = Host.objects.all()
    return render(request,'monitor/index.html',locals())

def host_info(request,machine_id,timing):


    # 传递磁盘号给前端JS,用以迭代分区图表
    disk = GetSysData(machine_id, "disk", 3600, 1)
    disk_data = disk.get_data()
    partitions_len = []
    for d in disk_data:
        p = len(d['disk']['id'])
        for x in range(p):
            partitions_len.append(x)

    # 传递网卡号给前端,用以迭代分区图表
    net = GetSysData(machine_id, "net", 3600, 1)
    nic_data = net.get_data()
    nic_len = []
    for n in nic_data:
        p = len(n["net"])
        for x in range(p):
            nic_len.append(x)

    return render(request, "monitor/host_info_{}.html".format(timing), locals())

# 从mongodb动态获取cpu数据
def get_cpu(request, machine_id, timing):
    data_time = []
    cpu_percent = []
    range_time = TIME_SECTOR[int(timing)]
    cpu_data = GetSysData(machine_id, "cpu", range_time)
    for doc in cpu_data.get_data():
        unix_time = doc['timestamp']
        times = time.localtime(unix_time)
        dt = time.strftime("%m-%d %H:%M", times)
        data_time.append(dt)
        c_percent = doc['cpu']['percent']
        cpu_percent.append(c_percent)
    data = {"data_time": data_time, "cpu_percent": cpu_percent}
    return HttpResponse(json.dumps(data))

# 从mongodb动态获取内存数据
def get_mem(request, machine_id, timing):
    data_time = []
    mem_percent = []
    range_time = TIME_SECTOR[int(timing)]
    mem_data = GetSysData(machine_id, "mem", range_time)
    for doc in mem_data.get_data():
        unix_time = doc['timestamp']
        times = time.localtime(unix_time)
        dt = time.strftime("%m-%d %H:%M", times)
        data_time.append(dt)
        m_percent = doc['mem']['percent']
        mem_percent.append(m_percent)
    data = {"data_time": data_time, "mem_percent": mem_percent}
    return HttpResponse(json.dumps(data))

# 从mongodb动态获取磁盘数据
def get_disk(request, machine_id, timing, partition):
    data_time = []
    disk_percent = []
    disk_name = ""
    range_time = TIME_SECTOR[int(timing)]
    disk = GetSysData(machine_id, "disk", range_time)
    for doc in disk.get_data():
        unix_time = doc['timestamp']
        times = time.localtime(unix_time)
        dt = time.strftime("%m-%d %H:%M", times)
        data_time.append(dt)
        d_percent = doc['disk']['percent'][int(partition)]
        disk_percent.append(d_percent)
        if not disk_name:
            disk_name = doc['disk']['id'][int(partition)]+'盘'
    data = {"data_time": data_time, "disk_name": disk_name, "disk_percent": disk_percent}
    return HttpResponse(json.dumps(data))

def get_net(request, machine_id, timing, net_id):
    data_time = []
    nic_in = []
    nic_out = []
    nic_name = ""
    range_time = TIME_SECTOR[int(timing)]
    net = GetSysData(machine_id, "net", range_time)
    for doc in net.get_data():
        unix_time = doc['timestamp']
        times = time.localtime(unix_time)
        dt = time.strftime("%m-%d %H:%M", times)
        data_time.append(dt)
        in_ = doc['net'][int(net_id)]['traffic_in']
        out_ = doc['net'][int(net_id)]['traffic_out']
        nic_in.append(in_)
        nic_out.append(out_)
        if not nic_name:
            nic_name = doc['net'][int(net_id)]['nic_name']
    data = {"data_time": data_time, "nic_name": nic_name, "traffic_in": nic_in, "traffic_out": nic_out}
    return HttpResponse(json.dumps(data))


# test
def run_db(request):

    obj = models.Host.objects.filter(machine_id='M-0087', hostname='wilde')
    if not obj:

        print(obj)

    return HttpResponse('OK')