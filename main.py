import draw
import random

selection_zone = input("Zone(a to i): ").lower()

zone_list = ['a','b','c','d','e','f','g','h','i']
computer = random.choice(zone_list)

draw.zone_selected(selection_zone, computer)




a