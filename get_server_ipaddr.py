import csv
import socket

def get_ip_address(server_name):
    try:
        ip_address = socket.gethostbyname(server_name)
        return ip_address
    except socket.error:
        return None

def process_servers(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader)
        if "SERVER_NAME" in headers:
            writer.writerow(headers + ["IP_ADDRESS"])
        else:
            writer.writerow(headers)
            writer.writerow(headers + ["IP_ADDRESS"])
        
        for row in reader:
            server_name = row[0]
            ip_address = get_ip_address(server_name)
            if ip_address:
                writer.writerow(row + [ip_address])
            else:
                writer.writerow(row + ["N/A"])

# Specify your input and output file names
input_file = 'all_servers.csv'
output_file = 'all_servers_new.csv'

process_servers(input_file, output_file)
