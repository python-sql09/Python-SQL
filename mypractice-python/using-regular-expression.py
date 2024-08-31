# 8. Using a regular expression
import re
text = "Hello, Sean! - How are you?"
print(text)
text_clean = re.sub("[^\w]", " ",text)
print(text_clean)
words = text_clean.split()
print(words)