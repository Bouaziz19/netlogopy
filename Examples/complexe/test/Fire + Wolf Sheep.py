import time
import os
import multiprocessing
import nl4py

def run_model_in_process(netlogo_home, model_path, lock, output_file_path):
    try:
        # Initialize NetLogo within the process
        nl4py.initialize(netlogo_home)
        netlogo_app = nl4py.netlogo_app()
        netlogo_app.open_model(model_path)
        netlogo_app.command("setup")
        for i in range(10):
            # Simulate some model action
            netlogo_app.command("go")
            # Prepare the data to write
            data_to_write = f"{model_path} iteration {i}\n"
            # Acquire the lock before writing to the file
            with lock:
                with open(output_file_path, 'a') as f:
                    f.write(data_to_write)
            # Print to the console
            print(f"{model_path}  {i}")
            time.sleep(1)
        netlogo_app.command("quit")
        time.sleep(5)
    except Exception as e:
        # Capture any exceptions and write them to the output file
        error_message = f"Error in process for model {model_path}: {str(e)}\n"
        with lock:
            with open(output_file_path, 'a') as f:
                f.write(error_message)
        print(error_message)

if __name__ == "__main__":
    netlogo_home = "C:/Program Files/NetLogo 6.2.2"

    # Ensure that model paths are correct
    current_dir = os.path.dirname(__file__)
    path_model1 = os.path.join(current_dir, "Fire.nlogo")
    path_model2 = os.path.join(current_dir, "Wolf Sheep Predation.nlogo")

    # Print model paths to verify
    print(f"Model 1 path: {path_model1}")
    print(f"Model 2 path: {path_model2}")

    # Define the output file path
    output_file_path = os.path.join(current_dir, "output.txt")

    # Create a lock for synchronized file access
    lock = multiprocessing.Lock()

    # Create processes, passing the lock and output file path
    p1 = multiprocessing.Process(target=run_model_in_process, args=(netlogo_home, path_model1, lock, output_file_path))
    p2 = multiprocessing.Process(target=run_model_in_process, args=(netlogo_home, path_model2, lock, output_file_path))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()

    print("Both models have finished running.")
