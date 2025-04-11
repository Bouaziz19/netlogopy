import copy
import nl4py,time,copy
import os
import shutil

global list_pyturtle
global list_street

list_pyturtle=[]
list_street=[]
def run_netlogo(netlogo_home="C:/Program Files/NetLogo 6.2.2",path_model=""):
    
    nl4py.initialize(netlogo_home)
    nl4py.startServer(netlogo_home)
    if path_model == "":
        model = os.path.dirname(__file__)+"\\netlogopy.nlogo"
    else :
        model = path_model
    n=nl4py.NetLogoApp()
    n.openModel(model)
    n.command("setup")
    return n

def run_netlogo_base(netlogo_home="C:/Program Files/NetLogo 6.2.2"):
    nl4py.initialize(netlogo_home)
    nl4py.startServer(netlogo_home)
    model = os.path.dirname(__file__)+"\\netlogopy.nlogo"
    n=nl4py.NetLogoApp()
    n.openModel(model)
    n.command("setup")
    return n
def reset_base_file(dest):
    model = os.path.dirname(__file__)+"/base.nls"
    src = model
    dest+"/base2.nls"
    shutil.copy2(src, dest)
def create_ntlg_file(dest):
    model = os.path.dirname(__file__)+"/base.nls"
    src = model
    dest+"/base2.nls"
    shutil.copy2(src, dest)
def netlogoshow(n,word):
        c = "netlogoshow "+list2nllist([word])
        c = n.report(c)
        return c
def nl_output_print (n , word) :
    """
    Affiche un message dans NetLogo en appelant la procédure 'netlogoshow'.
    """
    cmd = "outputprint " + list2nllist([word])
    return n.report(cmd)
def resize_world(n,x0,xf,y0,yf):
        c = "resize_world "+list2nllist([x0,xf,y0,yf])
        c = n.report(c)
        return c
def list2nllist(lis):
        s="["
        for i in lis:
            if type(i) == str:
                s+=' "'+i+'" '
            else :
                s+=' '+str(i)+' '
        s+="]"
        return s
def set_background(n,image):
        c = "set_background "+list2nllist([image])
        c = n.report(c)
        return c
def run_command(n,command ):
        c = n.command(command )
        return c
def de_copy(a):
    return copy.deepcopy(a)


def distancebetween(n,fromm=0,target=1):
        id_fromm=fromm.id
        id_target=target.id
        c = "distanceto "+list2nllist([id_fromm,id_target])
        c = n.report(c)
        return c

def getxyturtle(n,turtle):
        id_turtle=turtle.id
        c = "getxyturtle "+list2nllist([id_turtle])
        c = n.report(c)
        c=eval(c)
        return c

class n_model:
    def __init__(self,netlogo_home="C:/Program Files/NetLogo 6.2.2"):
        pass
    def gui(self,netlogo_home="C:/Program Files/NetLogo 6.2.2"):
            nl4py.initialize(netlogo_home)
            nl4py.startServer(netlogo_home)
            model = "./netlogopy.nlogo"
            self=nl4py.NetLogoApp()
            self.openModel(model)
            self.command("setup")
           
            return self
      
class turtle():
    def __init__(self,n):
        self.id= id
        self.n= n
    def distanceto(self,target=1):
        id_fromm=self.id
        id_target=target.id
        c = "distanceto "+list2nllist([id_fromm,id_target])
        c = self.n.report(c)
        # idd = int(c[:-2])
        return c
    
    def face_to(self,target=1):
        id_fromm=self.id
        id_target=target.id
        c="faceto "+list2nllist([id_fromm,id_target])
        c=self.n.report(c)
        idd= int(c[:-2])
        return idd
    def move_to(self,id_target):
        fr=self.id
        c="moveto "+list2nllist([fr,id_target.id])
        c=self.n.report(c)

    def hideturtle(self):
        turtleid=self.id
        c="hideturtle "+list2nllist([turtleid])
        self.n.report(c)
    def dieturtle(self):
        turtleid=self.id
        c="dieturtle "+list2nllist([turtleid])
        self.n.report(c)
    def set_shape(self,shape):
        turtleid=self.id
        c="set_shape "+list2nllist([turtleid,shape])
        self.n.report(c)
    def setxy(self,x,y):
        turtleid=self.id
        c="turtle_setxy "+list2nllist([turtleid,x,y])
        self.n.report(c)


    def fd(self,repeat=1):
        fr=self.id
        c="fdfd "+list2nllist([fr,repeat])
        self.n.report(c)

class street :
    def __init__(self, n,fromm=0,too=1,label="street",labelcolor=0,color=0,shape="aa",thickness=0.5):
        fromm=fromm.id
        too=too.id
        self.id = id
        self.create_street_ft(n,fromm,too,label,labelcolor,color,shape,thickness)
    def create_street_ft(self,n,fromm=20,too=10,label="street",labelcolor=0,color=0,shape="aa",thickness=0.5):
        c="create-street-ft "+list2nllist([fromm,too,label,labelcolor,color,shape,thickness])
        
        c=n.report(c)
        self.id= c
        list_street.append(self)
        return self

class pyturtle(turtle) :
    def __init__(self, n,x=0,y=0,shape="car",size_shape=4,color=0,name="zn",labelcolor=0,fields={}):

        super().__init__(n)
        self.__dict__.update(fields)
        self.create_pyturtle_xyid(n,x,y,shape,size_shape,color,name,labelcolor)
  
    def create_pyturtle_xyid(self,n,x,y,shape,size_shape,color,name,labelcolor,):
        c="create-pyturtle-xyid "+list2nllist([x,y,shape,size_shape,color,name,labelcolor])
        c=n.report(c)
        print("  *******************    ")
        print(c)
        print("  *******************    ")

        self.id= int(c[:-2])
        list_pyturtle.append(self)
        return self
    def set_label(self, text):
        """
        Définit le label de la turtle dans NetLogo.
        """
        # On construit une commande NetLogo du type:
        # ask turtle <id> [ set label "text" ]
        cmd = f'ask turtle {self.id} [ set label "{text}" ]'
        self.n.command(cmd)



