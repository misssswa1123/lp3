text = input("Enter text: ")

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

codes = {}
items = []
for ch in freq:
    codes[ch] = ""
    items.append([freq[ch], [ch]])   

while len(items) > 1:
    items.sort()                     
    first = items.pop(0)           
    second = items.pop(0)           

    for ch in first[1]:
        codes[ch] = "0" + codes[ch] 
    for ch in second[1]:
        codes[ch] = "1" + codes[ch] 

   
    items.append([first[0] + second[0], first[1] + second[1]])


if len(codes) == 1:
    for ch in codes:
        codes[ch] = "0"


print("\nCharacter  Huffman Code")
for ch in codes:
    print("   ", ch, "      ", codes[ch])

encoded = ""
for ch in text:
    encoded += codes[ch]

print("\nEncoded text:", encoded)
print("Original size:", len(text) * 8, "bits")
print("Encoded size :", len(encoded), "bits")