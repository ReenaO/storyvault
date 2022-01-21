class welcome():
 def __init__(self, first_name):
     self.first_name = first_name



words = {
    'noun': ['Mountain', 'Ocean', 'Building', 'Playground', 'Animal'],
    'adjectives': ['Running', 'Walking', 'Cycling', 'Sleeping', 'Eating'],
    'people': ['Mother', 'Father', 'Sister', 'Brother', 'Friend', 'Husband'],
    'places': ['Farm', 'Beach', 'Work', 'School', 'City'],
    'weather': ['Sunny', 'Raining', 'Sleat', 'Windy', 'Snow', 'Stormy'],
    'animals': ['Dog', 'Cat', 'Goldfish', 'Hamster'],
    'color': ['red', 'green', 'blue', 'orange', 'purple'],
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

class story():
    def story():
        story = {
            2: { cinema,
            },
            3: { zoo,
            },
            4: { flower,
            },
            5: { chocolate,
            },
            6: { kite,
            }
        }    
        print(story[2])

class cinema():
    def cinema():

 # {people}, {animals} and i went to drive in cinema at {places}. we could see {noun} in the distance and the {WEATHER} there. A {bird} spend the entire film flying in front of {Color} screen. when film was over proverb appearered on screen and i woke up.
     class zoo():
      def zoo():
 # I went to the zoo with {people} and animals. we were {adjective} by tiger habitat in the {color}{weather}. {bird} were flying around our heads.it was an enjoyable day.the announcer on intercom said {proverb} then i woke up.

       class flower():
        def flower():
 # I was {adjective} by flowers in the {place}. the flowers were {color} and had a lovely scent. a bird flew past  in the direction of the {noun} singing {proverb} and i woke up.

         class chocolate():
           def chocolate():
 # i was {adjective} and had chilli flavoured chocolate bar with {people}. We were at {place} and overlooking {noun}. The {color}{weather} was amazing. the chocolate wrapper had {proverb} written on it and i woke up.

            class kite():
             def kite():
 # myself and{animal} were flying a {color} kite at beach when a {bird} flew into it causing it to fall to ground next to {people} writing proverb in the sand it was all a dream.

              class goodbye():
               def goodbye():



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
    print(' |         |   |___|       \/  \/    |___    |            ' )

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







def select_set_of_words(key):
    items = words[key]

    for count, value in enumerate(items):
        print("{}: {}".format(count, value))
print('')
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

