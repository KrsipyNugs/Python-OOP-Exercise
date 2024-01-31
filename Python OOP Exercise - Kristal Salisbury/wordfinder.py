import random

class WordFinder:
    def __init__(self, path)
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    def parse(self, dict_file):
        return [w.strip() for w in dict_file]
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    

wf = WordFinder("simple.txt")
wf.random() in ["cat", "dog", "porcupine"]

swf = SpecialWordFinder("complex.txt")
swf.random() in ["pear", "carrot", "kale"]