class Function:
    def __init__(self, function):
        self.fn = function

    def __call__(self, *args):
        return self.fn(*args)


class FunctionList:
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
