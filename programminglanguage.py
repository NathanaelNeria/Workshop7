class Language:
    def __init__(self, name="", typing="",  reflection="", year=""):
        self.name=name
        self.reflection=reflection
        self.typing=typing
        self.year=year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return '{}, {} Typing, Reflection ={}, First appeared in {}'.format(self.name, self.typing, self.reflection, self.year)