import os
import subprocess
import sys


if __name__ == "__main__":
    target_script = sys.argv[0]
    target_dir = target_script.rsplit("/", 1)[0]
    if target_dir != target_script:
        os.chdir(target_dir)

    subcommand = 'python -m grpc.tools.protoc -I . --python_out . --grpc_python_out . *.protos'
    subprocess.call(subcommand, shell=True)
