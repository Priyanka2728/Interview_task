import platform
import psutil
import wmi
import re
import uuid
import subprocess
import speedtest

def mac_address():
    try: 
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        return mac_address
    except:
        return "Was unable to get Mac Address because not conected to network"
    
def public_ip():
    try: 
        public_ip = subprocess.check_output(['curl', 'ifconfig.me']).decode('utf-8').strip()
        return public_ip
    except:
            return "Was unable to get Public IP Address because not conected to network"
    
def check_internet_speed():
    try:
        speed_test = speedtest.Speedtest()
        download_speed = speed_test.download() // 1000000
        upload_speed = speed_test.upload() // 1000000

        return download_speed,upload_speed
    except:
        return "Was unable to get Internet speed"

# Installed software list
print("List of installed software:")
for software in psutil.process_iter(['name']):
    print(f"- {software.info['name']}")

# Internet speed
try:
        network_speed_upload,network_speed_download = check_internet_speed()
        print(f'The upload speed of internet on this device is {network_speed_upload} MB \n and download speed is {network_speed_download} MB')
except:
        print("Was unable to get Internet speed")

# Screen resolution
print(f"\nScreen resolution: {str(wmi.WMI().Win32_VideoController()[0].CurrentHorizontalResolution)}x{str(wmi.WMI().Win32_VideoController()[0].CurrentVerticalResolution)}")

# CPU model
print(f"\nCPU model: {platform.processor()}")

# No of core and threads of CPU
print(f"\nNo of cores: {psutil.cpu_count(logical=False)}")
print(f"No of threads: {psutil.cpu_count(logical=True)}")

# GPU model ( If exist )
try:
    print(f"\nGPU model: {wmi.WMI().Win32_VideoController()[0].Name}")
except:
    print("\nGPU model: Not found")

# RAM Size ( In GB )
print(f"\nRAM size: {round(psutil.virtual_memory().total / (1024.0 ** 3), 2)} GB")

# Screen size ( like, 15 inch, 21 inch)
print(f"\nScreen size: Not found")

# Wifi/Ethernet mac address
# MAC address 
mac_add = mac_address()
print(f"Mac Address of device is : {mac_add}")

# Public IP address
ip = public_ip()
print(f"Public IP Address of device is : {ip}")


# Windows version
print(f"\nWindows version: {platform.platform()}")