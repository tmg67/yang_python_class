import subprocess
import os
import shutil

def generate_system_report(output_file):
    try:
        #get current working directory
        cwd = os.getcwd()

        #get disk usage of the current directory
        disk_usage = shutil.disk_usage(cwd)
         #get system information, 
        system_info = subprocess.run(['uname','-a'], capture_output=True, text=True).stdout

        #write the report to a file
        with open(output_file, 'w') as file:
            file.write(f"currenet working directory: {cwd}\n")
            file.write(f"disk usage:\n")
            file.write(f" total: {disk_usage.total / (1024** 3):.2f}  GB\n")
            file.write(f" used: {disk_usage.used / (1024** 3):.2f}  GB\n")
            file.write(f" free: {disk_usage.free / (1024** 3):.2f}  GB\n")
            file.write(f"system information:\n{system_info}\n")
        print(f"syatem diagonostics report saved to '{output_file}'")
    except Exception as e:
        print(f"error: {e}")
#example usage
generate_system_report("system_report.txt")