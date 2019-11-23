class Sentence:
    def __init__(self, line):
        self.__line = line

    def get_line(self):
        return self.__line

    def __eq__(self, other):
        c1=0
        for character in self.__line:
            c1+=1
        c2=0
        for character in other.get_line():
            c2+=1
        if c1!=c2:
            return False

        for index in range(c1):
            if self.__line[index]!=other.get_line()[index]:
                return False
        return True

    def __str__(self):
        return str(self.__line)