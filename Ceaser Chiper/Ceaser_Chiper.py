from cesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(text,shift,direction):

    S2=""
    for _ in text:
        if _ not in alphabet:                                       #check if the character in the alphabet or not
                S2+=_
        else:
            dex=alphabet.index(_)
            if direction=='encode':
                position=dex+shift
                if position>len(alphabet)-1:                                 #not to go out of list bounds
                    S2+=alphabet[position-len(alphabet)]
                else:
                    S2+=alphabet[position]
            else:
                position=dex-shift                                          #avoid an index error
                if position<0:
                    S2+=alphabet[len(alphabet)+position]
                else:
                    S2+=alphabet[position]
    print(f"the {direction}d message is",S2)

print(logo)

again=True
while again==True:                                                                  # repeat as many times as requested
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%len(alphabet)
    cesar(text,shift,direction)
    choice=input("Do you want to continue (y/n)?").lower()
    if choice =='n':
        again=False
        print("GoodBye  :)")

