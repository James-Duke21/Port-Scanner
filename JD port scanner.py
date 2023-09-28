import socket
import pyfiglet
import datetime


scan_file = open ("Project B.txt", "w")
scan_file.write ("Results list\n")


welcome_banner = pyfiglet.figlet_format("JD PORT SCANNER ")
print (welcome_banner)

time_stamp_first = datetime.datetime.now()
print (time_stamp_first)

try:

     first_input = input("Enter a host to scan:")
     target = socket.gethostbyname(first_input)

     print (first_input)

     for prt in range (1, 1026):

          skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          socket.setdefaulttimeout(0.0000001)
          poker = skt.connect_ex((target, prt))
          print ("Results {}:{} - {}".format(target, prt, poker))
          if poker == 0:
               open_banner = pyfiglet.figlet_format("OPEN")
               print(target + ":" + str(prt) + open_banner )
               scan_file.write(str(prt) + " OPEN \n")

     time_stamp_last = datetime.datetime.now()
     print(time_stamp_last)

     scan_file.write(str(time_stamp_last) + "\n")

     tt = time_stamp_last - time_stamp_first
     print (tt)

except socket.gaierror:
 print("Host is not available")
