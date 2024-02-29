import random
import string
characters = string.ascii_letters + string.punctuation+ string.digits
length=10
password="".join(random.sample(characters,length))
print(f"the generated password is {password}")