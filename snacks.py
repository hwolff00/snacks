#!/usr/bin/env python3
import random

def snacks():
    options = [
        "Risotto", "Saag Paneer", "Sausage and Peppers",
        "Scallops with Corn and Chorizo", "Shakshuka", "Souvlaki",
        "Spicy Corn and Crab Chowder", "Steak", "Vegetable Curry",
        "Grilled, Whole Fish", "Gringo Tacos", "Jambalaya", "Korean Meatloaf",
        "Meatballs", "Miso Fish", "Pasta Aglio Elio", "Porchetta", "Quiche",
        "BBQ Chicken", "Beef Bourguignon", "BLTs", "Chana Masala",
        "Chicken Tortilla Soup", "Veggie Chili", "Beef Chili",
        "Chinese Roast Duck", "Enchiladas", "Gocujang Chicken", "Ribs",
        "Jammers Pasta"
        ]
    snack = (random.choice(options))
    print()
    print("Need a little inspiration for your snack time?")
    print("Have you thought about {}?".format(snack))
    print()
    feeling = input("Are you good with this option? Type yes or no: ")
    if feeling.lower() == "no":
        print()
        print("How about {} instead?".format(random.choice(options)))
        print()
        new_input = input("Satisfied now? Type yes or no: ")
        if new_input.lower() == "no":
            print()
            print("Okay, maybe {} will suit you...".format(random.choice(options)))
            print()
            final_input = input("Does that work for you? Type yes or no: ")
            if final_input == "no":
                print()
                print("Maybe you should just get takeout instead.")

    print("Happy snacking!")
snacks()
