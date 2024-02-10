from os import path


class Book:
    def __init__(self, name):
        self.name = name
        self.content = self.__retrieve_book_content()
        
    def __retrieve_book_content(self):
        book_path = self.__get_book_path()
        with open(book_path) as f:
            return f.read()

    def __get_book_path(self):
        here = path.dirname(path.abspath(__file__))
        return path.join(here, "books", f"{self.name.lower()}.txt")

    def __str__(self):
        return self.content


class Stats:
    def __init__(self, target: Book):
        self.target_book = target
        self.target_book_content = str(target)
        self.words_count = self.__count_words()
        self.letters_count = self.__count_letters()
        self.sorted_letters_count = self.__get_characters_count_sorted_list()

    def __count_words(self):
        words = self.target_book_content.split()
        return len(words)

    def __get_characters_count_sorted_list(self):
        characters_list = [{'character': letter, 'count': self.letters_count.get(letter)} for letter in self.letters_count]
        sort_on = lambda x: x['count']
        characters_list.sort(reverse=True, key=sort_on)
        return characters_list

    def __count_letters(self):
        lowered = self.target_book_content.lower()
        letter_dict = {}
        letters = set([x for x in "abcdefghijklmnopqrstuvwxyz"])
        for letter in lowered:
            if letter in letters:
                if letter in letter_dict:
                    letter_dict[letter] += 1
                else:
                    letter_dict[letter] = 1
        return letter_dict

    def generate_report(self):
        print(f"--- Begin report of books/{self.target_book.name}.txt ---")
        print(f"{self.words_count} words found in the document")
        print()
        for counted_letter in self.sorted_letters_count:
            letter = counted_letter['character']
            count = counted_letter['count']
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")

def main():
    try:
        fk = Book("Frankenstein")
    except FileNotFoundError:
        print("File does not exist!")
        return
    sts = Stats(fk)
    sts.generate_report()

main()
