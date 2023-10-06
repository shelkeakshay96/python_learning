import psutil
import Logger


def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict()
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    # listprocess = ProcessDisplay()
    # Logger.log('Total running processes are : {}'. format(len(listprocess)))

    # cnt = 0
    # for elem in listprocess:
    #     cnt+= 1
    #     Logger.log(str(elem))


    for pId in psutil.pids():
        p = psutil.Process(pId)
        print(p.name())

if __name__=="__main__":
    main()






