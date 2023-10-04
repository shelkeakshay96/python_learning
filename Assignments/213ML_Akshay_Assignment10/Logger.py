from datetime import datetime

def log(line):
    now = datetime.now()

    f = open("assignment.log", "a")
    line = line + "\n"
    log = '[{}] {}'. format(now, line)
    f.write(log)
    f.close()
