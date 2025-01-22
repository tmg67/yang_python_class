import subprocess
import os
def list_running_processes(output_file):
    try:
        #excute the system command list processes
        command = ['tasklist'] if os.name == 'nt' else ['ps', 'aux']
        result = subprocess.rum(command, capture_output=True, text=True)

        #save the output file
        with open(output_file,'w') as file:
            file.write(result.stdout)
        print(f"process list saved to '{output_file}'")
    except Exception as e:
        print(f"error: {e}")
    #example usage
list_running_processes("process_list.txt")