import argparse
import socket


def scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))

        if result == 0:
            print("Port " + ip + ":" + str(port) + " is open")
        else:
            print("Port " + ip + ":" + str(port) + " is closed")

        s.close()
    except Exception:
        pass


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", required=True, help="host or ip")
    ap.add_argument(
        "-p", "--port", required=True, help="one or more ports with ',' separator"
    )

    args = vars(ap.parse_args())
    ports = args["port"].split(",")
    for p in ports:
        scan(args["ip"], int(p))
