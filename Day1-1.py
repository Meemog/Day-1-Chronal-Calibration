file = open("Callibration_input.txt", "r")

AllChanges = file.readlines()

file.close

Frequency = 0

for FrequencyChange in AllChanges:

    FrequencyChange = list(FrequencyChange)
    if FrequencyChange[len(FrequencyChange)-1] == '\n':
        FrequencyChange = FrequencyChange[:-1]

    Oper = FrequencyChange.pop(0)
    FrequencyChange = int(''.join(FrequencyChange))

    if Oper == "+":
        Frequency += FrequencyChange

    else:
        Frequency -= FrequencyChange

print(str(Frequency))