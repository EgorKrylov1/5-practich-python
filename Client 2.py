import socket
import threading

Host = '127.0.0.1'
Port = 12345

def rec_messages(Client_soc):
    while True:
        try:
            message = Client_soc.recv(1024).decode('utf-8')
            if not message:
                Client_soc.close()
                break
            print(message)
        except:
            Client_soc.close()
            break

def start_client():
    Client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Client_soc.connect((Host, Port))
    threading.Thread(target=rec_messages, args=(Client_soc,)).start()
    while True:
        message = input()
        if message.lower() == 'exit':
            Client_soc.close()
            break
        Client_soc.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()