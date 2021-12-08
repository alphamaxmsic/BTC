# bitcoin

from hashlib import sha256
import time

# change this value
MAX_NONCE = 1000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    print("prefix_str : {}".format(prefix_str))
    for nonce in range(MAX_NONCE):
        #print("nonce: {}".format(nonce))
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Successfully mined bitcoins with nonce value : {}".format(nonce))
            return new_hash

if __name__ == "__main__":
    
    sample_transactions='''
    acc001->acc002->15,
    acc004->acc123->20'''
    
    # todays value
    difficulty = 20 # number of 0's in front
    
    start = time.time()
    new_hash = mine(5, sample_transactions, "88d4266fd4e6338d13b845fcf289579d209c897823b9217da3e161936f031589", difficulty)
    end = time.time()
    print("new_hash : {}".format(new_hash))
    print("time-taken : {}".format(end-start))
