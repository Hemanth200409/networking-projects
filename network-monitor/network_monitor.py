import os
import time

host = input("Enter website or IP to monitor: ")

while True:
    print("Checking connectivity to", host)

    response = os.system("ping -n 1 " + host + " > nul")

    if response == 0:
        print("Server is UP")
    else:
        print("Server is DOWN")

    print("----------------------")

    time.sleep(5)