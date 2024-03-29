# File Analysis and Word Search

name_of_file = input("Enter file name:")
def analyze_file(name):
    # file = open(name, 'w') 
    # file.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    # file.close()
    readfile = open(name,'r')
    read = readfile.read()
    
    char = len(read)
    words = len(read.split()) # this will return an array containing each word seperately then len will give its words 
    lines = read.count("\n")+1
    dict = {
    'Charcaters' : char,
    'no_of_words': words,
    'no_of_lines': lines
        }
    print(dict)

analyze_file(name_of_file)


# Search a specified word

name_of_file = input("Enter file name:")
word = input('Word to be search:')
def search_word(name,word):
    readfile = open(name,'r')
    read = readfile.read()
    word_count = read.count(word)
    print(word_count)
    

search_word(name_of_file,word)