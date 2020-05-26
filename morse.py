class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    # takes a string like "dash-dot" and creates an instance with the correct pattern (['_', '.']).
    @classmethod
    def from_string(cls, string):
        newlist = []
        splits = string.split('-')
        for word in splits:
            if word == 'dash':
                newlist.append('_')
            elif word == 'dot':
                newlist.append('.')
        return cls(newlist)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

words = 'dash-dot'
a = Letter()
print(a.from_string(words))
