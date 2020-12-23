import os
import time
import re
import math

if __name__=="__main__":
    now=time.localtime()
    y,M,d,h,m=now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min
    nowstr= "%4d%2d%2d_%2dh%2d" % (y,M,d,h,m)
    # print(nowstr)
    session_name="" # Changed by >na
    session_start=time.time() # Changed by >go
    last_time=time.time()
    next_observation_num=1
    next_algorithm_num=1

    def stamp (): # Return #mins passed
        global last_time, now
        now=time.time()
        passed=now-last_time
        last_time=now
        return math.ceil(passed/60)
    log_queue=[]
    def log (msg, isFirstRow=False): #set isFirstRow=True for not printing passed time
        passed=stamp()
        if isFirstRow==False:
            log_queue.append("(%d min passed)" % passed)
        tm=time.localtime(now)
        h,m=tm.tm_hour, tm.tm_min
        log_queue.append(("%2d:%2d "% (h,m)) + msg)
        return None
    def flush ():
        try:
            cout=open(nowstr+"_"+session_name, "a")
        except (OSError, IOError):
            cout=open(nowstr+"_"+session_name, "w")
        global log_queue
        for msg in log_queue:
            cout.write(msg+"\n")
        cout.write("\n")
        cout.close()
        log_queue=[]

    while True:
        ln=input().strip()
        suf=""
        if len(ln.split(maxsplit=1)) > 1:
            suf=ln.split(maxsplit=1)[1]
        if re.match("^na .+",ln):
            session_name=ln.split(maxsplit=1)[1]
        elif re.match("^go$",ln):
            session_start=time.time()
            next_observation_num=1
            next_algorithm_num=1
            log ("Start session "+session_name,True)
        elif re.match("^done$",ln):
            log ("Finish session "+session_name)
            flush()
            next_observation_num=1
            next_algorithm_num=1
        elif re.match("^exit$",ln):
            flush()
            break
        elif re.match("^rd$",ln):
            log ("Read problem statement")
        elif re.match("^st$",ln) or re.match("^st ",ln):
            
            try:    #st 3, st 2
                num_test = int(suf)
                log("Trace sample test, +%d custom test" % (num_test))
            except ValueError:
                log("Trace sample test. "+suf)
        elif re.match("^ob$",ln) or re.match("^ob ",ln):
            
            log(("Observation %d. "%next_observation_num) + suf)
            next_observation_num += 1
        elif re.match("^al$",ln) or re.match("^al ",ln):
            
            log(("Algorithm %d. "%next_algorithm_num) + suf)
            next_algorithm_num += 1
        elif re.match("^im$",ln) or re.match("^im ",ln):
            
            log("Implementation. " + suf)
        elif re.match("^db$",ln) or re.match("^db ",ln):
            
            log("Debug " + suf)
        elif re.match("^gg$",ln) or re.match("^gg ",ln):
            
            log("Google " + suf)
            pass
        elif re.match("^wa$",ln) or re.match("^wa ",ln):
            
            try:
                num_test = int(suf)
                log("Wrong answer test %d" % (num_test))
            except ValueError:
                log("Wrong answer "+suf)
        elif re.match("^tle$",ln) or re.match("^tle ",ln):
            
            try:
                num_test = int(suf)
                log("Time limit exceeded test %d" % (num_test))
            except ValueError:
                log("Time limit exceeded "+suf)
            pass
        elif re.match("^mle$",ln) or re.match("^mle ",ln):
            
            try:
                num_test = int(suf)
                log("Memory limit exceeded test %d" % (num_test))
            except ValueError:
                log("Memory limit exceeded "+suf)
            pass
        elif re.match("^rte$",ln) or re.match("^rte ",ln):
            
            try:
                num_test = int(suf)
                log("Run time error test %d" % (num_test))
            except ValueError:
                log("Run time error "+suf)
            pass
        elif re.match("^ac$",ln) or re.match("^ac ",ln):
            
            log("Accepted "+suf)
            pass
        elif re.match("^fu+$",ln) or re.match("^fu+ ",ln):
            
            log("fuck up "+suf)
            pass
        elif re.match("^tc$",ln) or re.match("^tc ",ln):
            
            try:
                num_test = int(suf)
                log("Lookup test case %d" % (num_test))
            except ValueError:
                log("Lookup test case "+suf)
            pass
        elif re.match("^afk$",ln) or re.match("^afk ",ln):
            
            log("Away from keyboard. "+suf)
            pass
        elif re.match("^bck$",ln) or re.match("^bck ",ln):
            
            log("Back to session. "+suf)
            pass
        elif re.match("^ed$",ln) or re.match("^ed ",ln):
            
            log("Editorial "+suf)
            pass
        elif re.match("^dm",ln):
            print("Dit me may")
            log(ln) # In case dm is good
            pass
        else:   # Not special command, just log it
            log(ln)

        
          
