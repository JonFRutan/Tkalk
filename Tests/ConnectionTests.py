import socket

def connection_test():
    test_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Host: ")
    port = int(input("Port: "))
    try:
        test_client.connect((host, port))
        return True
    except socket.error as e:
        print(f"Connection failed: {e}")
        return False
    finally:
        test_client.close()
        