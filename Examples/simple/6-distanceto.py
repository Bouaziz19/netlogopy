import time
from netlogopy.netlogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    car02=pyturtle(n,x=5,y=5,shape="car",size_shape=4,color=55,name="car02",labelcolor=55)
    street( n,fromm=car01,too=car02,label="street",labelcolor=35,color=35,shape="aa",thickness=0.5)
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
        car01.fd(1)
        word=car01.distanceto(car02)
        print(word)
        netlogoshow(n,word)
    n.close_model()