import serial
if __name__=='__main__':
  srl=serial.Serial("/dev/ttyACM0/",baudrate=9600,timeout=1)
  srl.flush()
  while(True):
    data=srl.readline().deode('utf-8').rstrip()
