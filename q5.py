#   Caeser_Cipher 
import string

# Encrypt function
word = (input('Enter word:').lower())
number = int(input('Enter number:'))
def encrypt_caesar(word,number):
    alphabets = list(string.ascii_lowercase)
    char = [x for x in word]
    code ='' 
    for i in char:
        for j in range(len(alphabets)):
            if  i == alphabets[j]:
                index = j + number 
                if index > 25:
                    mod = index-26
                    code += (alphabets[mod])   
                else:
                    code += (alphabets[index])
    return code 

encrypt_result = encrypt_caesar(word,number)
print('encrypt code : ', encrypt_result)


# Decrypt function
def decrypt_caesar(result,number):
    alphabets = list(string.ascii_lowercase)
    char = [x for x in result]
    decode = ''
    for i in char:
        for j in range(len(alphabets)):
            if i == alphabets[j]:
                index = j - number
                if index < 0:
                    mod = index + 26
                    decode += (alphabets[mod]) 
                else:
                    decode += (alphabets[index])
    return decode

decrypt_result = decrypt_caesar(encrypt_result,number)
print('decrypt code : ',decrypt_result)


# Second minimun and maximum

List = [100,200,800,1005]

def second_min_max(list):
    print(list)
    list.sort()
    print('second min : ',list[1])
    print('second maximum : ',list[-2])

second_min_max(List)


# Test cases
# Test case for encrypt_caesar() with valid inputs
# Input: word = "hello", shift_time = 3
# Expected Output: "Encrypted word: khoor"
# encrypt_caesar()

# Test case for encrypt_caesar() with non-integer shift value
# Input: word = "hello", shift_time = "abc"
# Expected Output: "Error: Shift value must be an integer."
# encrypt_caesar()

# Test case for second_min_max() with valid input list
# Input: listA = [4, 7, 1, 5, 3]
# Expected Output: "Sorted list: [1, 3, 4, 5, 7]", "Second Maximum: 5", "Second Minimum: 3"
# second_min_max(listA=[4, 7, 1, 5, 3])

# Test case for second_min_max() with empty input list
# Input: listA = []
# Expected Output: "Error: List must contain at least two elements."
# second_min_max(listA=[])

# Test case for second_min_max() with non-integer elements in input list
# Input: listA = [4, 7, "abc"]
# Expected Output: "Error: Input must be a list of integers."
# second_min_max(listA=[4, 7, "abc"])
