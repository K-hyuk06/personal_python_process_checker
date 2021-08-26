import psutil


for proc in psutil.process_iter(attrs=['cmdline', 'pid', 'name', 'username', 'status']):

    if 'python' in proc.info['cmdline']:
        print(proc.info)

print('end')
