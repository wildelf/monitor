

import psutil

# p_name = 'pycharm64.exe'
#
# def get_process_pids(p_name):
#     pid_list = []
#     pids = psutil.pids()
#     processes=[]
#     for pid in pids:
#         try:
#             p = psutil.Process(pid)
#             name = p.name()
#             processes.append([pid,name])
#         except:
#             continue
#
#     for p in processes:
#         if p[1] == p_name:
#             pid_list.append(p[0])
#
#     return pid_list
#
#
#
# def get_process_mem_info():
#     pid_list = get_process_pids(p_name)
#     process_data = {}
#     percent = 0
#     for pid in pid_list:
#         p = psutil.Process(pid)
#         percent += p.memory_percent()
#     process_data[p_name] = percent
#     return process_data
#
# data = get_process_mem_info()
# print(data)


# p = psutil.Process(1372)
#
# percent = p.memory_percent()
# print(percent)


import time

times = time.localtime(int(time.time()))
dt = time.strftime("%m-%d %H:%M", times)
print(dt)