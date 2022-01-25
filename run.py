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
    print('||       |    |     |  |___|  |  |  |   /\|                ')
    print('||       |    |     |  |      |  |  |  |  |                ')
    print(' ======  |    |     |  |___   |  |  |   \/|                ')


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
    print(' |         |   |   |   \         /  |___|   |/\            ')
    print(' |         |   |   |    \   /\  /   |       |              ')
    print(' |         |   |___|      \/  \/    |___    |              ')


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


words = {
    'noun': ['Mountain', 'Ocean', 'Building', 'Playground', 'Animal'],
    'adjective': ['Running', 'Walking', 'Cycling', 'Sleeping', 'Eating'],
    'person': ['Mother', 'Father', 'Sister', 'Brother', 'Friend', 'Husband'],
    'place': ['Farm', 'Beach', 'Work', 'School', 'City'],
    'weather': ['Sun', 'Raining', 'Sleat', 'Wind', 'Snow', 'Storm'],
    'animal': ['Dog', 'Cat', 'Goldfish', 'Hamster'],
    'color': ['red', 'green', 'blue', 'orange', 'purple'],
    'bird': ['Robin', 'Blackbird', 'Crow', 'Goldfinch'],
    'proverb': ["Every cloud has a silver lining", "No news is good news"],
}

# Dictionary to hold the extended configurations
extended = {
    'animal': {
        'Dog': "Dog called Bluebell",
        'Cat': "Cat called Tinkerbell",
        'Goldfish': "Goldfish called Goldie",
        'Hamster': "Hanster called Hammie"
    },
    'color': {
        'red': "shiny red",
        'green': "bottle green",
        'blue': "bright blue",
        'orange': "burnt orange",
        'purple': "dark purple",
    },
}

# Dict for the stories
stories = {
    'cinema': "{person}, {animal} and I went to drive in cinema at {place}."
    "We could see the {noun} in the distance and the {weather} there."
    "A {bird} spend entire film flying in front of {color} screen."
    "When the film was over the {proverb} appearered on screen and I woke up.",
    'zoo': "I went to the zoo with my {person} and {animal}."
    "We were {adjective} near tiger habitat in the {color} {weather}."
    "A {bird} were flying around our heads.It was an enjoyable day."
    "The announcer on intercom said {proverb} then I woke up.",
    'flower': "I was {adjective} by flowers in the {place}."
    "The flowers were {color} and had a lovely scent."
    "A bird flew past in the direction of the {noun} singing {proverb}"
    "and I woke up.",
    'chocolate': "! was {adjective} and had chilli flavoured chocolate bar" 
    " that I shared with my {person}."
    "We were at {place} and over looking the {noun}."
    "The {color} {weather} was amazing."
    "The chocolate bar wrapper had {proverb} written on it and i woke up.",
    'kite': "Myself and {animal} were flying a {color} kite at beach."
    "When a {bird} flew into it causing it to fall to ground next"
    "to my {person} writing {proverb} in the sand it was all a dream.",
}

configuration = {
    'story': ['cinema', 'zoo', 'flower', 'chocolate', 'kite'],
    'options': ['extended', 'short'],
    'titles': {
        'cinema': cinema,
        'zoo': zoo,
        'flower': flower,
        'chocolate': chocolate,
        'kite': kite
    }
}


class StoryManager:
    def __init__(self, select_extended=False):
        self.selection = {}
        self.select_extended = select_extended
        self.extended = False

    def select_story(self):
        return self.select_values('story', configuration)

    def print_story_title(self, story):
        configuration['titles'][story]()

    def select_story_options(self):
        selection = self.select_values('options', configuration)
        self.extended = True if selection == 'extended' else False
        return self.extended

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
        if self.select_extended:
            self.select_story_options()

        self.selection = {}
        for k, _ in words.items():
            value = self.select_values(k)
            # If extended is True the current value gets replaced 
            # by its extended version if exists.
            if self.extended is True:
                for extended_key, _ in extended.items():
                    if k == extended_key and value in extended[k].keys():
                        value = extended[k][value]

            self.selection[k] = value

        self.print_story(story)

    def print_story(self, story):
        story_string = stories[story]
        print(f"{story_string}".format(**self.selection))
          
    def welcome(self):
        welcome()

    def goodbye(self):
        goodbye()


def main():
    story_manager = StoryManager(select_extended=True)
    story_manager.welcome()
    story_manager.start()
    story_manager.goodbye()


main()
