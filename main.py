import socket
from typing import List


SOCKET_TIMEOUT = 0.5


# --- Shows the title and authorization reminder.
def print_banner() -> None:
    print("=" * 52)
    print("portvex")
    print("Educational TCP scanner for authorized testing only.")
    print("Only scan systems you own or have permission to test.")
    print("=" * 52)


# --- Gets the target from the user.
def get_target() -> str:
    while True:
        target = input("Enter hostname or IP address: ").strip()

        if target:
            return target

        print("Target cannot be empty. Please try again.")


# --- Converts a hostname into an IP address.
def resolve_target(target: str) -> str:
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        raise ValueError("Could not resolve the hostname or IP address.")


# --- Makes sure the port number is valid.
def get_port(prompt: str) -> int:
    while True:
        value = input(prompt).strip()

        try:
            port = int(value)
        except ValueError:
            print("Please enter a whole number between 1 and 65535.")
            continue

        if 1 <= port <= 65535:
            return port

        print("Port must be between 1 and 65535.")


# --- Gets the start and end ports for the scan.
def get_port_range() -> tuple[int, int]:
    while True:
        start_port = get_port("Enter start port: ")
        end_port = get_port("Enter end port: ")

        if start_port <= end_port:
            return start_port, end_port

        print("Start port must be less than or equal to end port.")


# --- Tests one TCP port.
def is_port_open(ip_address: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(SOCKET_TIMEOUT)
            result = sock.connect_ex((ip_address, port))
            return result == 0
    except OSError:
        return False


# --- Prints scan progress on one line.
def show_progress(current: int, total: int, port: int) -> None:
    percent = (current / total) * 100
    print(f"\rScanning port {port} | {current}/{total} ({percent:5.1f}%)", end="")


# --- Scans the selected port range.
def scan_ports(ip_address: str, start_port: int, end_port: int) -> List[int]:
    open_ports = []
    ports = range(start_port, end_port + 1)
    total_ports = end_port - start_port + 1

    for current, port in enumerate(ports, start=1):
        show_progress(current, total_ports, port)

        if is_port_open(ip_address, port):
            open_ports.append(port)

    print()
    return open_ports


# --- Shows the final results.
def print_results(target: str, ip_address: str, open_ports: List[int]) -> None:
    print("\nScan complete.")
    print("-" * 52)
    print(f"Target: {target}")
    print(f"IP address: {ip_address}")

    if open_ports:
        print("\nOpen TCP ports:")
        for port in open_ports:
            print(f"  - {port}")
    else:
        print("\nNo open TCP ports were detected in the selected range.")

    print("-" * 52)


# --- Runs the scanner.
def main() -> None:
    print_banner()

    try:
        target = get_target()
        ip_address = resolve_target(target)
        start_port, end_port = get_port_range()

        print(f"\nResolved target: {target} -> {ip_address}")
        print(f"Scanning TCP ports {start_port} through {end_port}...\n")

        open_ports = scan_ports(ip_address, start_port, end_port)
        print_results(target, ip_address, open_ports)
    except ValueError as error:
        print(f"\nInput error: {error}")
    except KeyboardInterrupt:
        print("\n\nScan cancelled by user.")
    except socket.error as error:
        print(f"\nNetwork error: {error}")


if __name__ == "__main__":
    main()
