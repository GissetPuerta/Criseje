tabla=("TRWAGMYPFDXBNUZSQVHLCKE")
NIF=("12345678")
nifu=tabla[int(NIF)%23]
print(f"su NIF es 12345678{nifu}")

for letter in sentence:
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] = 1

print(letter_counter)