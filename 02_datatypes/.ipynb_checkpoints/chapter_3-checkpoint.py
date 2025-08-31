'''Operations with strings'''

boy = "Souvik"
current_company = "Standard Chartered Bank"
previous_company = "HSBC"

print(f"Souvik has moved from {previous_company} to {current_company}")

print(f"Standard chartered bank is also called {current_company[0:18]}")

print(f"Testing step: {current_company[0:18:1]}")
print(f"Testing step: {current_company[0:18:2]}")

print(f"Don't mention starting index: {current_company[:18]}")
print(f"Don't mention ending index while using step: {current_company[0::2]}")
print(f"Reverse current company: {current_company[::-1]}")

normal_text = "Jé mé pel"
encoded_text = normal_text.encode("utf-8")
decoded_text = encoded_text.decode("utf-8")

print(f"Normal text: {normal_text}")
print(f"Encoded text: {encoded_text}")
print(f"Decoded text: {decoded_text}")