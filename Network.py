import os.path

def getInfo(text, command):
	#This will use the run the command in CMD and output it to a file
	# The program then looks for the important information in the file, extracts it, and returns said information
	command = command + ">temp"
	os.system(command) # Runs the command and captures it in a "temp" file
	result = []
	file = open("temp")
	info = file.readlines()
	file.close()
	for i in range(len(info)): # Sorts for the keyword then extracts the corresponding data
		if text in info[i]:
			result.append(info[i].split(":")[1].strip())
	os.remove("temp") # Deletes the file to keep everything clean
	return result

def getRaw(command): # This retunes a list of the exact output of the command
	command = command + ">temp"
	os.system(command) 
	result = []
	file = open("temp")
	info = file.readlines()
	file.close()
	return info


def checkNetworkConnection(): 
   #This will only return true if the computer is currently connected to the internet over WiFi.
   # It is recommended that this is run first to prevent errors from occurring.
   # If computer if not connected to the internet over WiFi then this will cause an error that the program will detect
	try:
		currentNetworkName() # This will cause an error if the computer is not connected over WiFi
		return True
	except:
		return False

def currentNetworkName(): # Return the name of the WiFi network you computer is currently connected to in string format
	return str(getInfo("Profile","Netsh WLAN show interfaces")[1]) # "Profile" appears twice, but we only want it once

def currentNetworkPassword(): # eturn the password of the WiFi network you computer is currently connected to in string format
	return str(getInfo("Key Content","netsh wlan show profile \""+currentNetworkName()+"\" key=clear")[0])

def savedNetworkNames(): # This will return a list of every saved network name on the computer
	return getInfo("All User Profile","Netsh wlan show profiles")


def getNetworkPassword(name): # This does the same thing as currentNetworkPassword() but takes in a string argument containing a network name. 
	#It will return an error code if the network name or password could not be found. Both possible outputs will be retuned in string format.
	try:
		return str(getInfo("Key Content","netsh wlan show profile \""+name+"\" key=clear")[0])
	except:
		return "Ip address not found"


def DefaultGateway(): # This will get and return the first default gateway found 
	return str(getInfo("Default Gateway","ipconfig")[0])

def IPV4(): # This will get and return the first IPV4 address in string format
	return str(getInfo("IPv4 Address","ipconfig")[0])

def IPV6(): # This does the same as IPV4() but for IPV6
	info  = getRaw("ipconfig")
	result = []
	for i in range(len(info)): # Sorts for the keyword then extracts the corresponding data
		if "Link-local IPv6 Address" in info[i]:
			result.append(info[i].split(":",1)[1:][0]) # Searching for the first occurrence of an IPV6 address
	result = str(result[0]).strip()
	return result

def hostName(): # This will return the host name (The name of the computer) in string format.
   #If your computer has a “:” in the name then the full name may not be reported
	return str(getInfo("Host Name","ipconfig /all")[0])

def getData(): # This will return a list containing all network data
	data = getRaw("ipconfig /all")
	while "\n" in data: # Used to remove empty lines
		data.remove("\n")
	return data

def publicIP():# This return the users public IP address in string format
	return str(getInfo("Address","nslookup myip.opendns.com. resolver1.opendns.com")[1])

def seeListeningPorts(): # This will return a list of listing ports
	return getRaw("netstat -an |find /i \"listening\"")

def openPort(port): # This takes in a port and returns True if it is open or False if it is closed
	# Make sure to enter the full port name as it would appear in CMD. Ex: [::]:135
	temp = getRaw("netstat -an |find /i \""+port+"\"")
	if len(temp) == 1: return True
	else: return False
