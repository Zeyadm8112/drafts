# AP-Mapping Script

This Python script reads an Excel file containing a list of Access Points (APs) with their associated information (e.g., Name, IP address, Type, Serial Number, Location), pings the IP addresses, and adds a "Status" column to indicate whether the AP is "Active" or "Inactive". The results are printed to the console with color-coded statuses.

## Requirements

Before using the script, ensure you have the following dependencies installed:

- **Python 3.x**
- **pandas**: Used to handle Excel files and manipulate data.
- **colorama**: Used to add colors to console output for better visibility.
- **openpyxl**: Required for reading `.xlsx` files.

You can install the required Python packages using pip:

```bash
pip install pandas colorama openpyxl

https://github.com/user-attachments/assets/69b2559a-3a5f-4412-9276-6dcece295898


