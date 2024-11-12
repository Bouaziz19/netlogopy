import nl4py
import os
import time

netlogo_home = "C:/Program Files/NetLogo 6.2.2"
model_path = os.path.join(os.path.dirname(__file__), "Fire.nlogo")
output_file_path = os.path.join(os.path.dirname(__file__), "output_fire.txt")

# Initialize NetLogo
nl4py.initialize(netlogo_home)
netlogo_app = nl4py.netlogo_app()
netlogo_app.open_model(model_path)
netlogo_app.command("setup")

for i in range(10):
    netlogo_app.command("go")
    data_to_write = f"{model_path} iteration {i}\n"
    with open(output_file_path, 'a') as f:
        f.write(data_to_write)
    print(f"{model_path}  {i}")
    time.sleep(1)

netlogo_app.command("quit")
