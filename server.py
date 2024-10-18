import socket
import threading

Host = '127.0.0.1'
Port = 12345
Clients = []

def Broadcast(message, sender):
    for client in Clients:
        if client != sender:
            try:
                client.send(message)
            except:
                Clients.remove(client)
                client.close()

def Handle_client(Client_soc):
    while True:
        try:
            message = Client_soc.recv(1024)
            if not message:
                Clients.remove(Client_soc)
                Client_soc.close()
                break
            Broadcast(message, Client_soc)
            print(f"Received: {message.decode('utf-8')}")
        except:
            Clients.remove(Client_soc)
            Client_soc.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((Host, Port))
    server.listen()
    print(f"Server listening on {Host}:{Port}")
    while True:
        Client_soc, _ = server.accept()
        Clients.append(Client_soc)
        threading.Thread(target=Handle_client, args=(Client_soc,)).start()

if __name__ == "__main__":
    start_server()