import json
import time
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def received_sys_info(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        hostname = received_json_data["hostname"]
        received_json_data['timestamp'] = int(time.time())
        client = GetSysData.connect_db()
        db = client[GetSysData.collection]
        collection = db[hostname]
        collection.insert_one(received_json_data)
        return HttpResponse("Post the system Monitor Data successfully!")
    else:
        return HttpResponse("Your push have errors, Please Check your data!")