words = {
    'noun': ['Mountain', 'Ocean', 'Building', 'Playground', 'Animal'],
    'adjective': ['Running', 'Walking', 'Cycling', 'Sleeping', 'Eating'],
    'person': ['Mother', 'Father', 'Sister', 'Brother', 'Friend', 'Husband'],
    'place': ['Farm', 'Beach', 'Work', 'School', 'City'],
    'weather': ['Sunny', 'Raining', 'Sleat', 'Windy', 'Snow', 'Stormy'],
    'animal': ['Dog', 'Cat', 'Goldfish', 'Hamster'],
    'color': ['red', 'green', 'blue', 'orange', 'purple'],
    'bird': ['Robin', 'Blackbird', 'Crow', 'Goldfinch'],
    'proverb': ["Every cloud has a silver lining", "No news is good news"],
}

stories = {
    'cinema': "{person}, {animals} and i went to drive in cinema at {places}. we could see {noun} in the distance and the {weather} there. A {bird} spend the entire film flying in front of {Color} screen. when film was over proverb appearered on screen and i woke up.",
    'zoo': "I went to the zoo with {person} and animals. we were {adjective} by tiger habitat in the {color} {weather}. {bird} were flying around our heads.it was an enjoyable day.the announcer on intercom said {proverb} then i woke up.",
    'flower': "I was {adjective} by flowers in the {place}. the flowers were {color} and had a lovely scent. a bird flew past  in the direction of the {noun} singing {proverb} and i woke up.",
    'chocolate': "i was {adjective} and had chilli flavoured chocolate bar with {person}. We were at {place} and overlooking {noun}. The {color}{weather} was amazing. the chocolate wrapper had {proverb} written on it and i woke up.",
    'kite': "myself and{animal} were flying a {color} kite at beach when a {bird} flew into it causing it to fall to ground next to {person} writing proverb in the sand it was all a dream.",
}


def welcome():
    print(" \\            //            |                              ")
    print("  \\          //             |                              ")
    print("   \\        //     ____     |     ___    ___          ___  ")
    print("    \\  /\  //     |    |    |    |      |   |  |\/|  |   | ")
    print("     \\//\\//      |____|    |    |      |   |  |  |  |___| ")
    print("      \/  \/       |____     |    |___   |___|  |  |  |___  ")


def cinema():
    print(' ======                                                    ')
    print('||                                                         ')
    print('||       .                                                 ')
    print('||             _____    ___    __ __                       ')
    print('||       |    |     |  |___|  |  |  |   / \|               ')
    print('||       |    |     |  |      |  |  |  |   |               ')
    print(' ======  |    |     |  |___   |  |  |   \ /|               ')


def zoo():
    print('======                                                      ')
    print('    //                                                      ')
    print('   //                                                       ')
    print('  //      ___     ___                                       ')
    print(' //      |   |   |   |                                      ')
    print('//       |   |   |   |                                      ')
    print('======   |___|   |___|                                      ')


def flower():
    print('  ______                                                   ')
    print(' |         |                                               ')
    print(' |______   |                                               ')
    print(' |         |    ___                   ___                  ')
    print(' |         |   |   |   \          /  |___|   |/\           ')
    print(' |         |   |   |     \   /\  /   |       |             ')
    print(' |         |   |___|       \/  \/    |___    |            ')


def chocolate():
    print(' _____                                                     ')
    print('|       |                           |         |            ')
    print('|       |                           |       __|__          ')
    print('|       |___    ___    ___    ___   |         |     ___    ')
    print('|       |   |  |   |  |      |   |  |   /\|   |    |___|   ')
    print('|       |   |  |   |  |      |   |  |  |  |   |    |       ')
    print('|_____  |   |  |___|  |___   |___|  |   \/|   |    |___    ')


def kite():
    print('                       /|\                     ')
    print('                      /_|_\                    ')
    print('                \     \ | /                    ')
    print('                 \     \|/                     ')
    print('                  \     |                      ')
    print('                   \ ___/                      ')


def goodbye():
    print('_____                                                            ')
    print('|                            |   |                               ')
    print('|                            |   |                               ')
    print('|   ___   ___     ___     ___|   | _            ___              ')
    print('|    |   |   |   |   |  /    |   |/ \    \ /   |___|             ')
    print('|    |   |   |   |   |  |    |   |   |    |    |                 ')
    print('|____|   |___|   |___|   \__/|   |\__/    |    |___              ')


configuration = {
    'story': ['cinema', 'zoo', 'flower', 'chocolate', 'kite'],
    'titles': {
        'cinema': cinema,
        'zoo': zoo,
        'flower': flower,
        'chocolate': chocolate,
        'kite': kite
    }
}


class StoryManager:
    def __init__(self):
        self.selection = {}

    def select_story(self):
        return self.select_values('story', configuration)

    def print_story_title(self, story):
        configuration['titles'][story]()

    def select_values(self, key, dict_of_values=words):
        items = dict_of_values[key]

        for count, value in enumerate(items):
            print("{}: {}".format(count+1, value))

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

    def start(self):
        story = self.select_story()
        print(story)
        self.print_story_title(story)

        self.selection = {}
        for k, _ in words.items():
            value = self.select_values(k)
            self.selection[k] = value

        self.print_story(story)

    def print_story(self, story):
        story_string = stories[story]
        print(f"{story_string}".format(**self.selection))


def main():
    story_manager = StoryManager()
    story_manager.start()


main()
