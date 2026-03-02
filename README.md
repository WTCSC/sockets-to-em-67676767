# sockets-to-em-67676767

Simple demo: a PyQt5 GUI server that listens for a client sending two colors (text color and background color). The server updates the displayed "67" color and background and echoes a confirmation back.

## Files
- [server.py](server.py) — GUI server (contains `MainWindow`, `check_sockets`, `cleanup`)
- [client.py](client.py) — simple console client that sends color commands

## Requirements
- Python 3.7+
- PyQt5
- Network access between client and server (port 5000, is just used on localhost for now)

## Usage Guide
1. Run `git clone https://github.com/WTCSC/sockets-to-em-67676767.git`
2. (Optional) Create a virtual environment, activate it, and install dependencies
``` bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Run the server in one terminal: `python server.py`
4. Run the client in another: `python client.py`
5. Enjoy the 6️⃣7️⃣s