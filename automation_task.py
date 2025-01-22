import datetime
import os
import shutil

def create_backup(source_directory):
    if not os.path.exists(source_directory):
        print(f"error: the directory '{source_directory}'doesnot exist")
        return
    # generate a timestamped backup name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"

    #create a zip archieve of the source directory
    shutil.make_archive(backup_name, "zip", source_directory)
    print(f"Backup created: {backup_name}.zip")

#example usage
create_backup("./example_directory")