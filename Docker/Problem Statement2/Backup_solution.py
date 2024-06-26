import os
import shutil
import datetime

# Set up the backup configuration
remote_server = "your_remote_server_ip"
remote_username = "your_remote_username"
remote_password = "your_remote_password"
remote_directory = "/path/to/remote/directory"

local_directory = "/path/to/local/directory"

# Define the backup function
def backup_directory(local_directory, remote_server, remote_username, remote_password, remote_directory):
    # Create the remote backup directory if it doesn't exist
    ssh_command = f"sshpass -p {remote_password} ssh {remote_username}@{remote_server} 'mkdir -p {remote_directory}'"
    os.system(ssh_command)

    # Copy the local directory to the remote server
    rsync_command = f"rsync -avz {local_directory} {remote_username}@{remote_server}:{remote_directory}"
    os.system(rsync_command)

    # Generate a backup report
    report = f"Backup report for {datetime.datetime.now()}\n"
    report += f"Backup directory: {local_directory}\n"
    report += f"Remote server: {remote_server}\n"
    report += f"Remote directory: {remote_directory}\n"
    report += "Backup successful."

    return report


backup_report = backup_directory(local_directory, remote_server, remote_username, remote_password, remote_directory)

print(backup_report)