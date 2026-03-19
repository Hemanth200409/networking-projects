import socket

target = input("Enter website or IP: ")

ports = [21, 22, 80, 443]

print("Scanning", target)

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED")

    s.close()
    