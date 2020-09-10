# Python Network Command Library
 Network is a python library that contains a bunch of network related functions. It does not have any dependencies other then access to CMD. This Library contains mostly WiFi related functions. 
 
## Documentation

**currentNetworkName()** : Return the name of the WiFi network you computer is currently connected to in string format

**currentNetworkPassword()** : Return the password of the WiFi network you computer is currently connected to in string format

**getNetworkPassword()**: This does the same thing as currentNetworkPassword() but takes in a string argument containing a network name. It will return an error code if the network name or password could not be found. Both possible outputs will be retuned in string format.

**savedNetworkNames()** : This will return a list of every saved network name on the computer

**checkNetworkConnection()**: This will only return true if the computer is currently connected to the internet over WiFi. It is recommended that this is run first to prevent errors from occurring.

**DefaultGateway()** : This will get and return the first default gateway found in string format

**IPV4()**: This will get and return the first IPV4 address in string format

**IPV6()**: This does the same as IPV4() but for IPV6. 

**hostName()**: This will return the host name (The name of the computer) in string format. If your computer has a “:” in the name then the full name may not be reported

**getData()**: This will return a list containing all network data

**publicIP()**: This return the users public IP address in string format. Also it will most likely display “Non-authoritative answer:” You may wish to clear the screen after running this command. 

**seeListeningPorts()**: This will return a list of listing ports

**openPort()**: This takes in a port and returns True if it is open or False if it is closed. Make sure to enter the full port name as it would appear in CMD. Ex: [::]:135

**Note**: If you have more then one method of connecting to the internet or multiple adapters then the methods that return the first occurrence of a value may not display the information you are looking for.
In that case running getData() and manually extracting the information is recommended. This library does not have any python dependences, however you must be able to run CMD on your computer.
