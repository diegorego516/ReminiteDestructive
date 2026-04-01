import subprocess

def trigger_system_analysis():
    print("Initializing System Analysis Mode...")
    # Ensure the command is a valid shell string or list
    command = "echo 'Activating UI Modules...'"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Higher privilleges may be required.")

def main_menu():
    print(" --- LinuxUI3 System Analyst --- ")
    target_ip = input("Enter Target IP: ")
    # Link to the scan function from SystemHack
    # Scan_Ports(target = 80, 443)
