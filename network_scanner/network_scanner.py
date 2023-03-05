import socket

def scan_host(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        
        s.connect((ip, 8))
        s.send(b'SaySomething\r\n') 
        result = s.recv(512)
        print(result)


def main():
    scan_host('192.168.0.36')

if __name__ == '__main__':
    main()