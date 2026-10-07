LOG_ENDPOINT = ("192.168.1.10", 514)

try:
    LOG_ENDPOINT[0] = "10.0.0.1"
except TypeError:
    print("Modification blocked: tuple is immutable.")

print(LOG_ENDPOINT)
