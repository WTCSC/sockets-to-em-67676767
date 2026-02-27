# sockets-to-em-67676767

Simple demo: a PyQt5 GUI server that listens for a client sending two colors (text color and background color). The server updates the displayed "67" color and background and echoes a confirmation back.

## Files
- [server.py](server.py) — GUI server (contains `MainWindow`, `check_sockets`, `cleanup`)
- [client.py](client.py) — simple console client that sends color commands

## Requirements
- Python 3.7+
- PyQt5
- Network access between client and server (port 5000)

Install dependencies:
```sh
pip install PyQt5
```