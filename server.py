import socket
import time 

# HOST = socket.gethostbyname('server')
HOST = 'localhost'
PORT = 12341


print("Starting up...")
# t1 = time.perf_counter()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        # if time.perf_counter() - t1 > 10:
        #     s.close()
        #     print("Timeout reached")
        #     break
        print("Listen...")
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}...")
            while True:
                try:
                    data = conn.recv(1024)
                except ConnectionResetError:
                    print("An existing connection was forcibly closed by the remote host")
                    break
                if not data:
                    break
                print(data.decode())
                conn.send("received".encode())
