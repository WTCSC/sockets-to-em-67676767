import socket
import sys
import select
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
from PyQt5.QtCore import Qt, QSize, QTimer

# Create a socket object (IPv4 + TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow quick reuse when restarting
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to 0.0.0.0:5000 and listen
server.bind(("0.0.0.0", 5000))
server.listen(1)
server.setblocking(False)

print("Server listening on 0.0.0.0:5000")

client = None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("67!")
        self.setFixedSize(QSize(400, 300))

        self.label = QLabel("67")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(f"font-size: 48px;")
        self.setCentralWidget(self.label)

    def on_received_color(self, color, bgColor):
        self.label.setStyleSheet(f"color: {color}; font-size: 48px;")
        self.setStyleSheet(f"background-color: {bgColor};")


def check_sockets():
    """
    Called periodically from the Qt event loop to accept connections and
    read incoming data without blocking the GUI.
    """
    global client

    rlist, _, _ = select.select([server] if server else [], [], [], 0)
    if rlist and client is None:
        conn, addr = server.accept()
        conn.setblocking(False)
        client = conn
        print(f"Connected to {addr}")

    if client:
        rlist, _, _ = select.select([client], [], [], 0)
        if rlist:
            data = client.recv(1024)
            if not data:
                print("Client disconnected")
                try:
                    client.close()
                except Exception:
                    pass
                client = None
                return

            msg = data.decode()
            print(f"Received: {msg}")

            parts = msg.split()
            color = parts[0] if len(parts) > 0 else "white"
            bgColor = parts[1] if len(parts) > 1 else "black"

            window.on_received_color(color, bgColor)

            # Echo a response back to the client
            client.send(f"Server received: {msg}".encode())


def cleanup():
    """
    Closes both the server and the client if they exist.
    """

    global client, server
    if client:
        client.close()
        client = None
    if server:
        server.close()
        server = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Setup a QTimer to poll sockets regularly without blocking the GUI
timer = QTimer()
timer.timeout.connect(check_sockets)
timer.start(100)

app.aboutToQuit.connect(cleanup)

sys.exit(app.exec_())