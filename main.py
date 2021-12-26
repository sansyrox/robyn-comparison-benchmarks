import subprocess
import os
from pathlib import Path
import time


def run_tests():
    file_names = [( "test_bjoern.py", 5000 ), ( "test_fastapi.py", 5001 ), ( "test_robyn.py", 5002 ), ( "test_starlette.py", 5003 )]
    path = Path(__file__)
    directory_path = path.parent.absolute()

    for file_name, port in file_names:
        if file_name != "test_robyn.py":
            proc = subprocess.Popen(["python3", os.path.join(directory_path, file_name)])
        else:
            proc = subprocess.Popen(["python3", os.path.join(directory_path, file_name), "--workers=6", "--processes=2"])

        time.sleep(5)
        try:
            outs, errs = proc.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
        
        output = subprocess.run(["oha", "--no-tui", "--insecure", "-c", "100", "-n", "100000", f"http://127.0.0.1:{port}"], capture_output=True)
        print(file_name)
        print("---------------------------")
        print(output.stdout.decode("utf-8"))
        
        proc.kill()

    for _, port in file_names:
        subprocess.run(["npx", "kill-port", f"{port}"])

if __name__ == "__main__":
    run_tests()
