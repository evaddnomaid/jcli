import sys
print("Hello world!")
print(" ".join(sys.argv))
with open("log.txt", "a") as file:
    file.write(" ".join(sys.argv))
    file.write("\n")
    # Comments - what do they mean?
