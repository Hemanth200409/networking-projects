import os

hosts = ["google.com", "github.com", "amazon.com"]

for host in hosts:
    print("Checking:", host)
    response = os.system("ping -n 1 " + host)

    if response == 0:
        print(host, "is reachable\n")
    else:
        print(host, "is not reachable\n")