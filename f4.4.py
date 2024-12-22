# From Chapter 04

# Example 1 - findall Function
import re

text = "The price of the item is $20.99"
pattern = r"\d+"
matches = re.findall(pattern, text)
print(matches)

# Example 2 - findall Function
text = "The quick brown fox jumps over the lazy dog"
pattern = r"\bthe\b"
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)

# Example 3 - findall Function
text = "Please contact us at info@example.com or support@example.com"
pattern = r"\b\w+@\w+\.\w+\b"
matches = re.findall(pattern, text)
print(matches)

# Example 4 - search Function
text = "The quick brown fox jumps over the lazy dog"
pattern = r"\bfox\b"
match = re.search(pattern, text)
if match:
    print(f"Found '{match.group()}' starting at position {match.start()}")
else:
    print("No match found")

# Example 5 - search Function
text = "The price of the item is $20.99"
pattern = r"\d"
match = re.search(pattern, text)
if match:
    print(f"Found '{match.group()}' starting at position {match.start()}")
else:
    print("No match found")

# Example 6 - split
text = "The quick brown fox jumps over the lazy dog"
pattern = r"\s+"
words = re.split(pattern, text)
print(words)

# Example 7 - split
text = "apple,banana,cherry,orange"
pattern = r","
fruits = re.split(pattern, text)
print(fruits)

# Example 8 - split
text = "The quick brown fox. Jumps over the lazy dog. The end."
pattern = r"\."
sentences = re.split(pattern, text)
print(sentences)

# Example 9 - sub Function
text = "The quick brown fox jumps over the lazy dog"
pattern = r"\bfox\b"
new_text = re.sub(pattern, "cat", text)
print(new_text)

# Example 10 - sub Function
text = "The price of the item is $20.99"
pattern = r"\$"
new_text = re.sub(pattern, "€", text)
print(new_text)

# Example 11 - sub Function
text = "The quick brown fox jumps over the lazy dog"
pattern = r"\bthe\b"
new_text = re.sub(pattern, "a", text, count=2)
print(new_text)
