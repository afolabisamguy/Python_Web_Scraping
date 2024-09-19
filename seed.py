import secrets
import string

# Generate a random alphanumeric string for the client seed
new_client_seed = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))

print("New Client Seed:", new_client_seed)
