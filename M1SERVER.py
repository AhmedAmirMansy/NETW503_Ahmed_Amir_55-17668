import socket
import threading
PORT = 5605
ADDR = ('127.0.0.1', PORT)
def threaded(conn, addr):
    print("[NEW CONNECTION] " + str(addr) + " connected.")
    while True:
            received_data = conn.recv(1024)
            received_str = received_data.decode('utf-8')
            processed_str = received_str.upper()
            processed_data = processed_str.encode('utf-8')
            conn.send(processed_data)
def main():
    print("Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        threading.Lock().acquire()
        threading.Thread(target=threaded, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
if __name__ == "__main__":
    main()
