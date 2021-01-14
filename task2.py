string1='a(b(x)d)efghijkl'
string2='(123).)(qw(e)'

def match(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0



def match2(input_string):
    s = []
    balanced = True
    index = 0
    while index < len(input_string) and balanced:
        token = input_string[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1
    return balanced and len(s) == 0


# Prima functie verifica daca numarul de paranteze deschise si inchise este egal
print(match(string1))


# A doua functie verifica daca parantezele daca parantezele au corespondent unele cu altele
print(match2(string2))