import hashlib
n = 10

key = b"string"
key2 = "string".encode()

for i in range(n):
    print(hash(key))
    print(hashlib.sha256(key).hexdigest())

for i in range(n):
    print(hash(key))

for i in range(n):
    print(hash(key2))

