import os
import platform
import sys


def get_cpu_info():
    cpu_info = {}
    try:
        if sys.platform.startswith('linux'):
            with open('/proc/cpuinfo', 'r') as f:
                for line in f:
                    if ':' in line:
                        key, value = [s.strip() for s in line.split(':', 1)]
                        if key in ['model name', 'cpu cores', 'architecture', 'Hardware', 'processor']:
                            cpu_info[key] = value
                        if key == 'model name' and 'Model' not in cpu_info:
                            cpu_info['Model'] = value
        else:
            cpu_info['Processor'] = platform.processor()
    except Exception as e:
        cpu_info['error'] = str(e)
    return cpu_info


def get_memory_info():
    mem_info = {}
    try:
        if 'SC_PAGE_SIZE' in os.sysconf_names and 'SC_PHYS_PAGES' in os.sysconf_names:
            pagesize = os.sysconf('SC_PAGE_SIZE')
            pages = os.sysconf('SC_PHYS_PAGES')
            mem_info['Total'] = pages * pagesize
    except Exception as e:
        mem_info['error'] = str(e)
    return mem_info


if __name__ == '__main__':
    print('System:', platform.system())
    print('Node name:', platform.node())
    print('Release:', platform.release())
    print('Version:', platform.version())
    print('Machine:', platform.machine())
    print('Processor:', platform.processor())
    print('\nCPU Info:')
    for k, v in get_cpu_info().items():
        print(f'  {k}: {v}')
    print('\nMemory Info:')
    for k, v in get_memory_info().items():
        print(f'  {k}: {v}')

