import time
from coincurve import PrivateKey
from sha3 import keccak_256

def generate_ethereum_address():
    private_key = PrivateKey()
    public_key = private_key.public_key.format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    address = addr.hex()
    # Uncomment the next line to print the address and private key
    # print(f'0x{address}, {private_key.to_hex()}')

    return address

def measure_generation_speed(duration_seconds):
    start_time = time.time()
    count = 0

    while time.time() - start_time < duration_seconds:
        generate_ethereum_address()
        count += 1

    return count

def main():
    # Measure generation over 1 minute
    addresses_in_60_sec = measure_generation_speed(60)

    # Measurement of generation over 1 minute (based on data from 1 second)
    addresses_in_1_min = addresses_in_60_sec
    print(f"Number of addresses generated in 1 minute: {addresses_in_1_min}")

    # Measurement of generation over 1 hour
    addresses_in_1_hour = addresses_in_1_min * 60
    print(f"Number of addresses generated in 1 hour: {addresses_in_1_hour}")

    # Measurement of generation over 1 week
    addresses_in_1_week = addresses_in_1_hour * 24 * 7
    print(f"Number of addresses generated in 1 week: {addresses_in_1_week}")

if __name__ == "__main__":
    main()
