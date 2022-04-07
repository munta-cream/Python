from ast import Lt
import time,os
from unittest import result

while True:
    Lt=time.localtime()
    result=time.strftime('%H:%M:%S',Lt)
    print(result)

    Lt=time.localtime()
    result=time.strftime('%I:%M:%S %p',Lt)
    print(result)
    

