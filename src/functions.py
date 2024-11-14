class CoefficientFunction:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        return self.function(*args)


class CFList:
    def __init__(self):
        self.functions = []

    def __getitem__(self, i):
        return self.functions[i]

    def __len__(self):
        return len(self.functions)

    def __itr__(self):
        return iter(self.functions)

    def append(self, variable):
        self.functions.append(variable)
