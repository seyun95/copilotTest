# copilot 이용한 코딩하기 - 메모리 사용량 구하기

# get current memeory usage of the process
def get_memory_usage():
    import resource
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024

# convert bytes to human readable format
def convert_bytes(num):
    for x in ['B','KB','MB','GB','TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
    return "%3.1f %s" % (num, 'TB')

# get the current memory usage of system in human readable format
def get_system_memory_usage():
    import subprocess
    return subprocess.check_output(['free','-m']).decode('utf-8').split('\n')[2].split()[3]

# get the current memory usage of process in human readable format
def get_process_memory_usage():
    return convert_bytes(get_memory_usage())

# print hello world
print("memeory usage - ", convert_bytes(get_memory_usage()))
# print("system memory usage - ", get_system_memory_usage())
print("process memory usage - ", get_process_memory_usage())