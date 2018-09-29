# 1. Initialize a hash map
hashmap = {0:0, 2:3}

# 2. Insert a new (key, value) pair or update the value of existing key
hashmap[1] = 1
hashmap[1] = 2

# 3. Get value of a key
print("The value of key 1 is: " + str(hashmap[1]))

# 4. Delete a key
del hashmap[2]

# 5. Check if a key is in the hash map
if (2 not in hashmap):
    print("Key 2 is not in the hash map.")

# 6. Both key and value can have different type in hash map
hashmap["pi"] = 3.1415

# 7. Get the size of the hash map
print("The size of the hash map is: " + str(len(hashmap)))

# 8. Iterate the hash map
for key in hashmap:
    print("(" + str(key) + "," + str(hashmap[key]) + ")", end = " ")
print("are in the hash map.")

# 9. Get all keys in the hash map
print(hashmap.keys())

# 10. Clear the hash map
hashmap.clear()
print("The size of hash map is: " + str(len(hashmap)))
