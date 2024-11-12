

# netlogopy

`netlogopy` is a Python library that bridges NetLogo and Python, enabling advanced agent-based simulations by combining NetLogo’s simulation environment with Python’s powerful libraries for computation, optimization, and AI. `netlogopy` allows direct manipulation of NetLogo agents from Python.

## Developed by
- **Nourddine Bouaziz** - [@Bouaziz19](https://github.com/Bouaziz19)

## Installation

### Step 1: Install NetLogo
Download and install NetLogo from the official site.
[![NetLogo](https://ccl.northwestern.edu/netlogo/images/netlogo-title-wide-60.jpg)](https://ccl.northwestern.edu/netlogo/download.shtml)

### Step 2: Install `netlogopy`
```bash
conda install openjdk -y
pip install netlogopy
pip install netlogopy --upgrade
```
 </td>
    <td>


</td> </tr> </table> 

### Step 3: Configure IDE (Optional)
To set up your IDE (e.g., VS Code) for Command Line Interface (CLI) compatibility, check:
- [Set Default Terminal](https://www.w3schools.io/editor/vscode-change-default-terminal/)
- [Change Default Terminal in VS Code](https://stackoverflow.com/questions/44435697/change-the-default-terminal-in-visual-studio-code)

## Colors Reference
![Colors](https://ccl.northwestern.edu/netlogo/docs/images/colors.jpg)

## Example Test
The following example demonstrates a basic setup of `netlogopy`, initializing a NetLogo world and creating an agent named `car01` with simple movement in the simulation environment.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home="C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    resize_world(n, 0, 60, 0, 60)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15, name="car01", labelcolor=15)
    
    for i in range(10):
        time.sleep(1)
        print(f"***********  {i}  ********")  
    n.close_model()

```
 </td>
    <td>


</td> </tr> </table> 

## Usage Examples

### Example 1: `pyturtle`
This example shows how to create an agent (a "turtle") in NetLogo using Python. Here, we create a `car`-shaped agent named `car01` and move it within the world.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    resize_world(n, 0, 60, 0, 60)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15, name="car01", labelcolor=15)
    
    for i in range(10):
        time.sleep(1)
        print(f"***********  {i}  ********")  
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 2: `set_background`
In this example, we set a custom background image in the NetLogo world. The background can be any image file accessible from your system.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    resize_world(n, 0, 60, 0, 60)
    path_image = "path/to/image/nelogopy.png"
    set_background(n, path_image)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15, name="car01", labelcolor=15)
    
    for i in range(10):
        time.sleep(1)
        print(f"***********  {i}  ********")  
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 3: `street`
This example demonstrates creating a link between two agents in the NetLogo world. Here, a `street` link connects two car agents (`car01` and `car02`).

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    resize_world(n, 0, 60, 0, 60)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15, name="car01", labelcolor=15)
    car02 = pyturtle(n, x=5, y=5, shape="car", size_shape=4, color=55, name="car02", labelcolor=55)
    street(n, fromm=car01, too=car02, label="street", labelcolor=35, color=35, shape="aa", thickness=0.5)
    
    for i in range(10):
        time.sleep(1)
        print(f"***********  {i}  ********")  
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 4: `fd`
In this example, the `fd` function is used to move the agent forward by one unit with each loop iteration.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    resize_world(n, 0, 60, 0, 60)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15, name="car01", labelcolor=15)
    
    for i in range(10):
        time.sleep(1)
        print(f"***********  {i}  ********")  
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 5: `netlogoshow`
Here, `netlogoshow` displays text above the agent during simulation. Each iteration, we update the displayed text.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    resize_world(n, 0, 60, 0, 60)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15, name="car01", labelcolor=15)
    
    for i in range(10):
        time.sleep(1)
        word = f"{car01.id}  {i}"
        netlogoshow(n, word)
        print(word)
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 6: `distanceto`
This example shows how to calculate and print the distance between two agents in the world using the `distanceto` function.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    car02 = pyturtle(n, x=5, y=5, shape="car", size_shape=4, color=55)
    
    for i in range(10):
        time.sleep(1)
        distance = car01.distanceto(car02)
        print(f"Distance to car02: {distance}")
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 7: `face_to`
In this example, the `face_to` function directs `car01` to face towards `car02`.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    car02 = pyturtle(n, x=5, y=5, shape="car", size_shape=4, color=55)
    
    for i in range(10):
        if i == 5:
            car01.face_to(car02)
        time.sleep(1)
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 8: `move_to`
The `move_to` function moves `car01` directly to `car02`'s position when the loop reaches a specified iteration.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    car02 = pyturtle(n, x=5, y=5, shape="car", size_shape=4, color=55)
    
    for i in range(10):
        if i == 5:
            car01.move_to(car02)
        time.sleep(1)
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 9: `hideturtle`
This example demonstrates how to hide an agent in the simulation using `hideturtle`.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    
    for i in range(10):
        if i == 5:
            car01.hideturtle()
        time.sleep(1)
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 10: `set_shape`
In this example, `set_shape` changes the shape of `car01` to `default` at a specific iteration.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    
    for i in range(100):
        if i == 5:
            car01.set_shape('default')
        time.sleep(1)
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 11: `getxyturtle`
The `getxyturtle` function retrieves the current `x` and `y` coordinates of `car01`.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    
    for i in range(10):
        time.sleep(1)
        position = getxyturtle(n, car01)
        print(f"Position: {position}")
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 12: `setxy`
The `setxy` function sets the `x` and `y` coordinates of `car01` to new values during the simulation.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    
    for i in range(100):
        if i == 5:
            car01.setxy(10, 10)
        time.sleep(1)
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 
### Example 13: `distancebetween`
This example calculates and prints the distance between `car01` and `car02`.

<table>
  <tr>
    <td>

```python
import time
from netlogopy.nelogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    n = run_netlogo(netlogo_home)
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15)
    car02 = pyturtle(n, x=5, y=5, shape="car", size_shape=4, color=55)
    
    for i in range(10):
        time.sleep(1)
        distance = distancebetween(n, car01, car02)
        print(f"Distance between car01 and car02: {distance}")
        car01.fd(1)
    n.close_model()
```
 </td>
    <td>


</td> </tr> </table> 

## Usage Examples

### Integrating an Existing NetLogo Model with Python
We have added a feature that allows you to use older NetLogo simulators and modify them with Python, creating a dual-layered simulator. The first layer represents the original simulator, while the second layer is created in Python using `netlogopy`. This approach enables further development on older simulators without having to rebuild them entirely in `netlogopy`.

<table>
  <tr>
    <td>

```python
import time, os, sys

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)
from netlogopy.netlogopy import *

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"
    path_model = os.path.join(os.path.dirname(__file__), "Wolf Sheep Predation.nlogo")
    n = run_netlogo(netlogo_home, path_model)

    # Resize world
    resize_world(n, 0, 70, 0, 55)

    # Initialize the original NetLogo model
    run_command(n, "setup")
    
    # Add Python-controlled agents
    car01 = pyturtle(n, x=20, y=20, shape="car", size_shape=4, color=15, name="car01", labelcolor=15)
    car02 = pyturtle(n, x=5, y=5, shape="car", size_shape=4, color=55, name="car02", labelcolor=55)
    street(n, fromm=car01, too=car02, label="street", labelcolor=35, color=35, shape="default", thickness=0.5)

    for i in range(100):
        run_command(n, "go")  # Run the NetLogo model step
        time.sleep(0.1)
        print(f"***********  {i}  ********")
        car01.fd(1)
        if i % 20 == 0:
            car01.setxy(10, 10)
```
 </td>
    <td>


</td> </tr> </table> 

# Download Examples

You can download this examples files from git .
