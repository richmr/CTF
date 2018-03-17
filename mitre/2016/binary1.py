obs_meme = "ogf&qs~GLY'+"

t1 = 1
t2 = 1
t3 = 0

clear_meme = ""

for letter in obs_meme:
    t2 = t2 + t1
    t1 = t1 + 1
    t4 = ord(letter)
    t4 = t4 ^ t2
    clear_meme += chr(t4)

print clear_meme

    
