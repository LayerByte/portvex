# portvex

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TCP](https://img.shields.io/badge/TCP-Scanner-0A66C2?style=for-the-badge)
![Education](https://img.shields.io/badge/Purpose-Education-2EA44F?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**portvex** is a simple, clean Python TCP port scanner built for learning how network sockets, hostname resolution, port ranges, timeouts, and terminal output work.

School Purpose Only.

> Only scan systems you own or have explicit permission to test.

## 🧭 Overview

portvex lets a user enter a hostname or IP address, choose a TCP port range, and see which ports are open. It is intentionally beginner-friendly and educational, with readable functions, useful comments, clean output, and safe error handling.

The scanner uses Python's built-in `socket` module and performs basic TCP connection checks. It does not include exploitation, brute forcing, persistence, credential theft, malware, stealth behavior, or destructive functionality.

## ✨ Features

| Feature | Description |
| --- | --- |
| 🎯 Target input | Enter a hostname or IP address |
| 🔢 Custom range | Choose the start port and end port |
| 🔎 TCP detection | Detect open ports with `socket.connect_ex()` |
| 📊 Progress display | See scan progress while ports are checked |
| ⏱️ Sensible timeout | Avoid long waits on closed or filtered ports |
| 🧯 Error handling | Handles invalid input, DNS errors, and interruptions |
| 🧑‍🏫 Beginner-friendly code | Organized with functions and useful comments |

## 🧰 Requirements

- Python 3.9 or newer
- A terminal or command prompt
- No third-party Python packages
- Authorization to scan the selected target

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/LayerByte/portvex.git
cd portvex
```

Or download the project files and open a terminal inside the `portvex` folder.

## ▶️ Usage

Run the scanner:

```bash
python main.py
```

On Windows, if `python` is not available, try:

```bash
py main.py
```

Then follow the prompts:

```text
Enter hostname or IP address: scanme.nmap.org
Enter start port: 20
Enter end port: 100
```

Use small port ranges while learning. Larger scans take longer because each closed or filtered port may wait for the configured timeout.

## 🖥️ Example Output

```text
====================================================
portvex
Educational TCP scanner for authorized testing only.
Only scan systems you own or have permission to test.
====================================================
Enter hostname or IP address: scanme.nmap.org
Enter start port: 20
Enter end port: 100

Resolved target: scanme.nmap.org -> 45.33.32.156
Scanning TCP ports 20 through 100...

Scanning port 100 | 81/81 (100.0%)

Scan complete.
----------------------------------------------------
Target: scanme.nmap.org
IP address: 45.33.32.156

Open TCP ports:
  - 22
  - 80
----------------------------------------------------
```

## 🧪 How It Works

1. The user enters a hostname or IP address.
2. portvex resolves the target to an IP address.
3. The user enters a start port and end port.
4. The scanner attempts a TCP connection to each port.
5. Ports that accept a connection are displayed as open.

The scanner is single-threaded on purpose so the source code stays easy to understand for students and beginners.

## 🛡️ Security / Authorization Notice

Port scanning can be considered suspicious or unauthorized when performed against systems you do not own or do not have permission to test.

Only scan:

- Your own computer
- Your own home network
- Your own lab machines
- Systems where you have explicit permission

Do not scan public systems, school networks, workplace networks, cloud assets, or third-party services unless you are specifically authorized.

## 🧯 Troubleshooting

| Problem | Possible Solution |
| --- | --- |
| `Could not resolve the hostname or IP address.` | Check the hostname spelling or use an IP address |
| Scan is slow | Choose a smaller range or adjust `SOCKET_TIMEOUT` in `main.py` |
| No open ports are found | The ports may be closed, filtered, or blocked by a firewall |
| `python` command not found | Install Python 3 or try `py main.py` on Windows |

## ⚠️ Disclaimer

This software is provided for educational purposes only. The author is not responsible for misuse, damage, service disruption, policy violations, or legal consequences caused by unauthorized scanning. You are responsible for following all applicable laws, rules, and policies.

## 📄 License

This project is released under the MIT License. You may use, modify, and share it according to the license terms.
