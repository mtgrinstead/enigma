class Wheel:
    def __init__(self, chars, notch):
        self.chars = chars
        self.notch = notch

    def spin(self):
        spun = self.chars[1:] + [self.chars[0]]
        self.chars = spun
        return spun


INPUT = Wheel(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], None)

# WHeel_I notch is set for "U"
WHEEL_I = Wheel(['P', 'U', 'E', 'O', 'I', 'D', 'K', 'F', 'T', 'R', 'B', 'A', 'S', 'W', 'L', 'Y', 'X', 'Q', 'C', 'J',
                 'V', 'H', 'G', 'N', 'Z', 'M'], "V")

# Wheel_II notch is set for "N"
WHEEL_II = Wheel(['N', 'H', 'L', 'J', 'G', 'W', 'F', 'R', 'S', 'D', 'P', 'Y', 'V', 'A', 'Q', 'E', 'X', 'T', 'I', 'O',
                  'C', 'B', 'M', 'U', 'Z', 'K'], "A")

# Wheel_II notch is set for "J"
WHEEL_III = Wheel(['K', 'R', 'W', 'X', 'F', 'L', 'P', 'S', 'J', 'D', 'O', 'Q', 'N', 'G', 'T', 'E', 'U', 'A', 'C', 'H',
                   'Y', 'Z', 'M', 'I', 'B', 'V'], "D")

# Wheel_II notch is set for "M"
WHEEL_IV = Wheel(['P', 'D', 'Z', 'Y', 'S', 'L', 'E', 'C', 'A', 'K', 'R', 'J', 'Q', 'B', 'G', 'N', 'M', 'W', 'H', 'O',
                  'V', 'X', 'T', 'U', 'F', 'I'], "Q")

# Wheel_II notch is set for "Y"
WHEEL_V = Wheel(['B', 'N', 'E', 'F', 'R', 'O', 'L', 'P', 'H', 'C', 'J', 'K', 'Y', 'Q', 'S', 'V', 'I', 'G', 'M', 'X',
                 'W', 'T', 'U', 'D', 'Z', 'A'], "Z")

REFLECTOR = Wheel(['Q', 'Y', 'H', 'O', 'G', 'N', 'E', 'C', 'V', 'P', 'U', 'Z', 'T', 'F', 'D', 'J', 'A', 'X', 'W', 'M',
                   'K', 'I', 'S', 'R', 'B', 'L'], None)

plug_list = []
plugs = ""

plugging = True
while plugging:
    if plugs != "Q":
        plugs = input(f"Enter plug pair (ex: AX) or 'q' to stop adding plugs.\n").upper()
        if plugs == "Q":
            break
        for pair in plug_list:
            for character in pair:
                if plugs[0] == character or plugs[1] == character:
                    print(f"Error: Character '{character}' already in use.")
                    plugs = input(f"Enter plug pair (ex: AX) or 'q' to stop adding plugs.\n").upper()
        else:
            plug_list.append((plugs[0], plugs[1]))
        print(plug_list)
    else:
        plugging = False


characters = input(f"Enter characters: \n")


def enigma(code, first_wheel, second_wheel, third_wheel):
    output = []
    count = 0

    def wheel_rotate(lst):
        return lst[1:] + [lst[0]]

    def wheel_2_rotate():
        pass
# Starting Index should take tuples to switch the alphabet then use this alphabet in trace

# input M will return F
    def trace():

        # need to add a count function
        index = INPUT.chars.index(letter)
        wheel_1_output = w1.chars[index]
        wheel_1_output_index = (INPUT.chars.index(wheel_1_output) - count)
        if wheel_1_output_index < 0:
            wheel_1_output_index += 26
        elif wheel_1_output_index > 25:
            wheel_1_output_index -= 26
        wheel_2_output = w2.chars[wheel_1_output_index]
        wheel_3_output = w3.chars[INPUT.chars.index(wheel_2_output)]
        reflector_output = REFLECTOR.chars[INPUT.chars.index(wheel_3_output)]
        wheel_3_return = INPUT.chars[w3.chars.index(reflector_output)]
        wheel_3_return_index = (w2.chars.index(wheel_3_return) + count)
        if wheel_3_return_index < 0:
            wheel_3_return_index += 26
        elif wheel_3_return_index > 25:
            wheel_3_return_index -= 26
        wheel_2_return = INPUT.chars[wheel_3_return_index]
        wheel_1_return = INPUT.chars[w1.chars.index(wheel_2_return)]
        final = wheel_1_return
        output.append(final)

    alpha = INPUT
    w1 = first_wheel
    w2 = second_wheel
    w3 = third_wheel
    for letter in code:
        w1.chars = wheel_rotate(w1.chars)
        # print("__--__")
        if w1.chars[-1] != w1.notch:
            count += 1
            trace()
            # print("A")
        elif w1.chars[-1] == w1.notch:
            count += 1
            w2.chars = wheel_rotate(w2.chars)
            trace()
            wheel_2_rotate()
            print("B")
        if w2.chars[-1] == w2.notch and w1.chars[-1] == w1.notch:
            w3.chars = wheel_rotate(w3.chars)
            print("C")
    return output


print(enigma(characters, WHEEL_I, WHEEL_II, WHEEL_III))