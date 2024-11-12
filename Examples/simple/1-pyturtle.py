import time
from netlogopy2.netlogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=9,color=15,name="car01",labelcolor=15)
    
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
    n.close_model()
