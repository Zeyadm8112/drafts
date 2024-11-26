import pandas as pd
import subprocess
import sys
import os
from colorama import Fore, init

# Initialize colorama for colorful console messages
init(autoreset=True)

def ping_ip(ip_address):
    """
    Pings an IP address and returns 'Active' if reachable, otherwise 'Inactive'.
    """
    try:
        # Use 'ping -n 1' for Windows or 'ping -c 1' for Linux/macOS
        command = ["ping", "-n" if os.name == "nt" else "-c", "1", ip_address]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Active" if result.returncode == 0 else "Inactive"
    except Exception as e:
        print(Fore.RED + f"Error pinging IP {ip_address}: {e}")
        return "Inactive"

def main():
    # Check if an argument is passed
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python AP-Mapping.py <path_to_excel_file>")
        sys.exit(1)

    # Get the file path from the command-line argument
    file_path = sys.argv[1]

    # Check if the file exists
    if not os.path.exists(file_path):
        print(Fore.RED + f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)

    # Check if the file has an Excel-compatible extension
    if not (file_path.endswith('.xlsx') or file_path.endswith('.xls')):
        print(Fore.RED + "Error: The provided file is not an Excel file (.xlsx or .xls).")
        sys.exit(1)

    # Try to read the Excel file into a DataFrame
    try:
        df = pd.read_excel(file_path, engine='openpyxl') if file_path.endswith('.xlsx') else pd.read_excel(file_path)
        
        # Add the 'Status' column
        print(Fore.YELLOW + "\nPinging IP addresses. Please wait...")
        df['Status'] = df['IP address'].apply(ping_ip)

        # Print the DataFrame with the Status column
        for _, row in df.iterrows():
            status = row['Status']
            status_color = Fore.GREEN if status == 'Active' else Fore.RED
            print(f"{row['Name']} | {row['IP address']} | {row['Type']} | {row['Serial Number']} | {row['Location']} | {status_color}{status}")

    except Exception as e:
        print(Fore.RED + f"An error occurred while reading the Excel file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
