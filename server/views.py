import json
import time
from server.config import *
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pymongo

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
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    cursor = db['M-001'].find().sort([("timestamp", -1)]).limit(1)
    for item in cursor:
        cpu_percent = item['cpu']['percent']
    return render(request,'index.html',{'cpu_percent':cpu_percent})