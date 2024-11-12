import time,os,random
import sys
import os

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)
from netlogopy2.netlogopy import *

os.system('cls')



if __name__ == "__main__" :
    dest = os.path.dirname(__file__)

    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    path_model = os.path.dirname(__file__)+"\\Fire.nlogo"
    # n=run_netlogo(netlogo_home)
    n=run_netlogo(netlogo_home,path_model)

    # n=run_netlogo(netlogo_home)

    # Resize world
    resize_world(n,0,70,0,55)
    # Change path fo image
    # path_image= os.path.dirname(__file__)+"/netlogopy.png"

    path_image = "D:/cphs2024/netlogopy.png"
    run_command(n,"setup")  
    
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="default",thickness=0.5)
    for i in range(0,100):
        run_command(n,"go")  
        time.sleep(0.1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        if i%20== 0 :
            car01.setxy(10,10)
            