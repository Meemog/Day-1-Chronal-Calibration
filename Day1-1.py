file = open("Callibration_input.txt", "r")

AllChanges = file.readlines()

file.close

Frequency = 0

for FrequencyChange in AllChanges:

    FrequencyChange = list(FrequencyChange)
    FrequencyChange = FrequencyChange[:-1]
    print(FrequencyChange)
    Oper = FrequencyChange.pop(0)
    FrequencyChange = int(''.join(FrequencyChange))

    if Oper == "+":
        Frequency += FrequencyChange

    else:
        Frequency -= FrequencyChange

print(str(Frequency))