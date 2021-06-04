from hashlib import sha256
MAX_NONCE = 100000000000
print(sha256("PRAANK".encode("ascii")).hexdigest())

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeroes):
    prefix_str = prefix_zeroes * '0'
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Congratulations!!! You have won bitcoins with nonce value: {nonce}")
            return new_hash
    return BaseException(f"Couldn't mine even after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions='''
    Prashant->Prateek->100,
    Ashit->Prateek->50,
    '''
    difficulty = 20
    import time
    start = time.time()
    print('Start Mining')
    new_hash = mine(5, transactions, 'af676f369f293fbe8700fd67f75498ad2478815e97db1dbb6bfbb08c1a839995', difficulty)
    total_time = str(time.time() - start)
    print(f"End of mining. It took: {total_time} seconds")
    print(new_hash)