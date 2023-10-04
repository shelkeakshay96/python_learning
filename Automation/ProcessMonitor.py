import psutil

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['username', 'name', 'pid'])
            
            listprocess.append(pinfo);
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Process Monitor")
    
    listprocess = ProcessDisplay()

    cnt = 0
    for elem in listprocess:
        cnt+= 1
        print(elem)
    
    print('Total running processes are :',len(listprocess))

if __name__=="__main__":
    main()






