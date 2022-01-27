class ClassDict:
    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

