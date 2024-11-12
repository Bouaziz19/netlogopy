import subprocess
import sys
import os

python_executable = sys.executable
current_dir = os.path.dirname(os.path.abspath(__file__))
fire_model_script = os.path.join(current_dir, 'run_fire_model.py')
wolf_sheep_script = os.path.join(current_dir, 'run_wolf_sheep_model.py')

print(f"Running {fire_model_script}")
print(f"Running {wolf_sheep_script}")


p2 = subprocess.Popen(
    [python_executable, wolf_sheep_script],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
p1 = subprocess.Popen(
    [python_executable, fire_model_script],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
stdout2, stderr2 = p2.communicate()
stdout1, stderr1 = p1.communicate()

print("Output from run_fire_model.py:")
print(stdout1)
print("Errors from run_fire_model.py:")
print(stderr1)

print("Output from run_wolf_sheep_model.py:")
print(stdout2)
print("Errors from run_wolf_sheep_model.py:")
print(stderr2)
