text = input()
zeroc = text.count("0")
text = text.replace("0","") + "0"*zeroc
print(text)
