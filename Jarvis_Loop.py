import glob
import time
import os

"""servers = {"HOME":"SAMISH",
           "HP" : "DESKTOP-12OV957",
           "PRERAK":"DESKTOP-B3GC6VI",
           "SAM":"VKGLaptop",
           "DJ":"DESKTOP-7C1T3TI"}"""

cur_server = DESKTOP-7C1T3TI
os.chdir("Subfiles/")    
files = [ "Client.py","Jarvis.py", "Detect.py"]

for fl in files:
    file = open(fl)
    script = file.read()
    exec(script)
    file.close()

run = True
while run:
    start = time.clock()
    out, status = VoiceDetect(mic)
    if status == True:
        val, actions = Commands(out,)
        op = val
        if op =='assist':
            while True:
                send_txt(out)
                send_img()
                op = recv_txt()
                ex = VoiceDetect(mic,'hey jarvis',4)
                if 'exit assist' in ex:
                    break
        else:
            if func=='clf':
                send_txt(val)
                send_img()
                op = recv_txt()
            elif func=="":
                op=val
            elif func=="exit":
                op=val
                run = False
    print(op)
    Output(op)
    end  = time.clock()
    print('Time taken:',end - start)
    
    
            
                
            
                
                
