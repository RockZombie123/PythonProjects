import psutil
import time
import os


list = ['---', 'python3', 'idle']

print('This simulator does not contain any databases, and thus data will NOT be saved.')

ter = input('bash@user: ')
#strter = ter.split()[1]


if ter == 'cpu':
    print('Collecting cpu data...')
    print('cpu percentage:',psutil.cpu_percent())
    print('RAM:',psutil.virtual_memory())
    print('RAM (dict):',dict(psutil.virtual_memory()._asdict()))
    print('RAM (percent):',psutil.virtual_memory().percent)
    print('total percentage of available memory:',psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    
elif ter == 'pip installed':
    print('running setup...')
    time.sleep(0.1)
    print('loading list...')
    time.sleep(0.1)
    print('Warning: This feature will only work on a terminal.')
    print('pip installed modules:')
    os.system('pip list')


elif ter == 'pip3 installed':
    print('Fetching new data...')
    time.sleep(0.1)
    print('Warning: This feature will only work on a terminal.')
    print('pip3 installed modules:')
    os.system('pip3 list')
    
elif ter == 'install ' + list[1]:
    os.system('sudo apt-get install python3')

elif ter == 'install ' + list[2]:
    os.system('sudo apt-get install idle')
    
elif ter == 'delete' + list[1]:
    os.system('sudo apt-get remove python3')
    
elif ter == 'delete' + list[2]:
    os.system('sudo apt-get remove idle')

elif ter == 'open':
	filename = input('File to open: ')
	try:
		os.system(f"nano {filename}")

	except:
		class bcolors:
    			HEADER = '\033[95m'
    			OKBLUE = '\033[94m'
    			OKCYAN = '\033[96m'
    			OKGREEN = '\033[92m'
	    		WARNING = '\033[93m'
	    		FAIL = '\033[91m'
	    		ENDC = '\033[0m'
	    		BOLD = '\033[1m'
	    		UNDERLINE = '\033[4m'

		print(f"{bcolors.FAIL}Failed to open file, contact rockzombie005@gmail.com for crash report.{bcolors.ENDC}")


elif ter == 'install':
	print("""

install [APPLICATION]
delete [APPLICATION]


""")

elif ter == 'delete':
	print("""

delete [APPLICATION]
install [APPLICATION]


""")


elif ter == 'ver' or ter == 'version':
	print("""

BARREL OS VER: v1.0

THIS IS A FREE SIMULATION OF SOFTWARE.
JUST GIVE CREDIT TO ORIGINAL CREATOR, AND YOU ARE FREE TO MAKE DIFFERENT DISTRIBUTIONS.
CONTACT: rockzombie005@gmail.com FOR MORE INFORMATION.
""")

elif ter == 'help':
	print('''

cpu - prints cpu data
allinfo - prints all hardware and software data (stats for nerds)
pip installed - prints a list of all the installed modules using pip
pip3 installed - prints a list of all the installed modules using pip3
install - installs the application
delete - deletes the application
open - opens a file
echo - the 'print' function in python
shutdown - shuts down linux/raspbian
ver - prints version of this simulator
help - displays this help message

''')

elif ter == 'allinfo':
	print(psutil.cpu_times())
	print(psutil.cpu_percent(1))
	print("Number of cores in system", psutil.cpu_count())
	print("\nNumber of physical cores in system",)
	print("CPU Statistics", psutil.cpu_stats())
	print(psutil.cpu_freq())
	print(psutil.getloadavg())
	print(psutil.virtual_memory())
	print(psutil.swap_memory())
	print(psutil.disk_partitions())
	print(psutil.disk_usage('/'))
	print(psutil.net_io_counters())
	print(psutil.net_connections())
	print(psutil.net_if_addrs())
	print(psutil.sensors_temperatures())
	print(psutil.sensors_fans())
	class bcolors:
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

	print(f"{bcolors.WARNING}WARNING: BATTERY CHECK MAY NOT WORK ON SOME DEVICES.{bcolors.ENDC}")
	print(psutil.sensors_battery())
	print(psutil.boot_time())
	print(psutil.users())
	
elif ter == 'shutdown':
	print("Shutdown begins in 3 seconds")
	time.sleep(3)
	os.system("sudo shutdown -h now")

elif ter == 'echo':
	echo = input("What would you like to print? ")
	print(echo)

elif ter == 'update':
	os.system("git clone https://github.com/RockZombie123/PythonProjects/edit/main/simulator.py")
	print("Cloned into working directory.")

else:
    print("-bash: '" + ter + "': command not found")
