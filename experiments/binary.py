# led_status = [0, 0, 0, 0, 0, 0, 0]
led_status = [0b000, 0b111, 0b011]


# val = 0b011
# print(bin(val))
# print("{0:b} ttt {1:b}".format(val, 8))


def display_bin_list(lst):
    for elem in lst:
        print(format(elem, "#05b"))


def invert(lst):
    for n in range(len(lst)):
        lst[n] = lst[n] ^ 0b001


display_bin_list(led_status)
invert(led_status)
print("---")
display_bin_list(led_status)


################


def change_status(g_stat):
    g_stat["tt"] = 123
    g_stat["leds"].append(44)

game_status = {
    "status": [0b000, 0b110, 0b001]
}
game_status["leds"] = [1, 2, 3]
print(game_status)
change_status(game_status)
print(game_status)

display_bin_list(game_status["status"])
for i, element in enumerate(game_status["status"]):
    print(i, element)
    if element & 0b001 > 0:
        print("set red")
    if element & 0b010 > 0:
        print("set blue")
    if element & 0b100 > 0:
        print("blink")