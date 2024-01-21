import sys
import socket
from datetime import datetime
import argparse
import threading

# Thread lock for printing
print_lock = threading.Lock()

def scan_port(ip, port, verbose):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            with print_lock:
                if verbose:
                    print(f'Port {port} is open')
        s.close()
    except:
        pass  # Handle exceptions 
# Setup Argument Parser
parser = argparse.ArgumentParser(description="Jay Port Scanner 1.0")
parser.add_argument("IP", help="IP address of the target to scan")
parser.add_argument("--start_port", type=int, default=0, help="Start of the port range to scan (default: 0)")
parser.add_argument("--end_port", type=int, default=9000, help="End of the port range to scan (default: 9000)")
parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")

# Parse Arguments
args = parser.parse_args()

# Define our target
target = socket.gethostbyname(args.IP)

# Print Welcome Banner
print("_"*50)
print("WELCOME TO JAY PORT SCANNER 1.0")
print("_"*50)
print("")

# Add a pretty banner
print("-"*50)
print(f"Scanning Target: {target}")
print("Time started: " + str(datetime.now()))
print("-"*50)

# Scanning
try:
        # Threaded Scanning
        max_threads = 100  # Maximum number of threads to run concurrently
        threads = []

        for port in range(args.start_port, args.end_port + 1):
                t = threading.Thread(target=scan_port, args=(target, port, args.verbose))
                threads.append(t)
                t.start()

                # Limiting the number of concurrent threads
                while threading.active_count() > max_threads:
                        pass

        for thread in threads:
                thread.join()
        print("Time completed: " + str(datetime.now()))

        print("Scanning Complete exiting")

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server")
