import os

# Function to execute a system command
def execute_command(command):
    os.system(command)

# Function to open a file
def open_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

# Function to divide two numbers
def divide(a, b):
    return a / b
    define( 'DISALLOW_UNFILTERED_HTML', false ); // sensitive


# Function with SQL Injection vulnerability
def sql_injection(username):
    query = "SELECT * FROM users WHERE username='%s'" % username
    execute_command("sql_execute " + query)

# Function with Command Injection vulnerability
def command_injection(ip):
    execute_command("ping " + ip)

# Function with Path Traversal vulnerability
def path_traversal(file_name):
    file_path = "/var/www/html/" + file_name
    open_file(file_path)

# Function with XSS vulnerability
def xss_attack():
    user_input = input("Enter your name: ")
    print("Hello, " + user_input + "!")

# Function with Unvalidated Redirect vulnerability
def redirect(url):
    print("Redirecting to:", url)

# Function with Insecure Deserialization vulnerability
def insecure_deserialization(data):
    execute_command("deserialize " + data)

# Function with Arbitrary File Write vulnerability
def arbitrary_file_write(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

# Main function
def main():
    # Vulnerable functions
    sql_injection("admin")
    command_injection("127.0.0.1")
    path_traversal("../../etc/passwd")
    xss_attack()
    redirect("https://example.com")
    insecure_deserialization("serialized_data_here")
    arbitrary_file_write("vulnerable_file.txt", "This file is vulnerable to arbitrary file write!")

if __name__ == "__main__":
from aws_cdk import aws_ec2 as ec2

instance = ec2.Instance(
    self,
    "my_instance",
    instance_type=nano_t2,
    machine_image=ec2.MachineImage.latest_amazon_linux(),
    vpc=vpc
)

instance.connections.allow_from(
    ec2.Peer.any_ipv4(), # Noncompliant
    ec2.Port.tcp(22),
    description="Allows SSH from all IPv4"
)
instance.connections.allow_from_any_ipv4( # Noncompliant
    ec2.Port.tcp(3389),
    description="Allows Terminal Server from all IPv4"
    main()
