import time
from netlogopy.netlogopy import *

if __name__ == "__main__" :
    # Change netlogo_home
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n=run_netlogo(netlogo_home)
    # Resize world
    resize_world(n,0,60,0,60)
    # Change path fo image
    # path_image ="path/to/image/netlogopy.png"
    path_image= "C:/Nouveau dossier (2)/netlogopy/Examples/netlogopy.png"
    set_background(n,path_image)
    car01=pyturtle(n,x=20,y=20,shape="car",size_shape=4,color=15,name="car01",labelcolor=15)
    
    for i in range(0,10):
        time.sleep(1)
        print("***********  ",i,"  ********")  
    n.close_model()