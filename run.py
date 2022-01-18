# welcome class:
# insert name :


words = {
    'noun': ['Mountain', 'Ocean', 'Building', 'Playground', 'Animal'],
    'adjectives': ['Running', 'Walking', 'Cycling', 'Sleeping', 'Eating'],
    'people': ['Mother', 'Father', 'Sister', 'Brother', 'Friend', 'Husband'],
    'places': ['Farm', 'Beach', 'Work', 'School', 'City'],
    'weather': ['Sunny', 'Raining', 'Sleat', 'Windy', 'Snow', 'Stormy'],
    'animals': ['Dog', 'Cat', 'Goldfish', 'Hamster'],
    'birds': ['Robin', 'Blackbird', 'Crow', 'Goldfinch'],
    'proverb': ["Every cloud has a silver lining", "No news is good news"]
}


def welcome():
    print(" \\            //            |                              ")
    print("  \\          //             |                              ")
    print("   \\        //     ____     |     ___    ___          ___  ")
    print("    \\  /\  //     |    |    |    |      |   |  |\/|  |   | ")
    print("     \\//\\//      |____|    |    |      |   |  |  |  |___| ")
    print("      \/  \/       |____     |    |___   |___|  |  |  |___  ")

 # cinema class:
 # {people}, {animals} and i went to drive in cinema at {places}. we could see {noun} in the distance and the {WEATHER} there. A {bird} spend the entire film flying in front of {Color} screen. when film was over proverb appearered on screen and i woke up.
 # zoo class:
 # I went to the zoo with {people} and animals. we were {adjective} by tiger habitat in the {color}{weather}. {bird} were flying around our heads.it was an enjoyable day.the announcer on intercom said {proverb} then i woke up.
 # flower class:
 # I was {adjective} by flowers in the {place}. the flowers were {color} and had a lovely scent. a bird flew past  in the direction of the {noun} singing {proverb} and i woke up.
 # chocolate class:
 # i was {adjective} and had chilli flavoured chocolate bar with {people}. We were at {place} and overlooking {noun}. The {color}{weather} was amazing. the chocolate wrapper had {proverb} written on it and i woke up.
 # kite class:
 # myself and{animal} were flying a {color} kite at beach when a {bird} flew into it causing it to fall to ground next to {people} writing proverb in the sand it was all a dream.
 # goodbye class:


def select_set_of_words(key):
    items = words[key]

    for count, value in enumerate(items):
        print("{}: {}".format(count, value))

    selection = -1
    valid_input = False
    item = None
    while not valid_input:
        input_value = input("Select a '{}' form the list above: [1..{}]: "
                            .format(key, len(items)))
        try:
            selection = int(input_value)
            item = items[selection-1]
            valid_input = True
        except (ValueError, IndexError):
            valid_input = False
    return item


def main():
    select_set_of_words('noun')


main()

