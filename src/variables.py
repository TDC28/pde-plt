class Variable:
    def __init__(self, symbol, highest_order, stepsize, value_range):
        self.symbol = symbol
        self.highest_order = highest_order
        self.stepsize = stepsize
        self.value_range = value_range

    def __str__(self):
        return self.symbol

    def __eq__(self, other):
        return isinstance(other, Variable) and other.symbol == self.symbol


class VariableList:
    def __init__(self):
        self.variables = []
        self.symbols = []

    def __getitem__(self, i):
        return self.variables[i]

    def __len__(self):
        return len(self.variables)

    def __itr__(self):
        return iter(self.variables)

    def __contains__(self, other):
        if isinstance(other, Variable):
            return any(var == other for var in self.variables)

        if isinstance(other, str):
            return any(symbol == other for symbol in self.symbols)

        return False

    def append(self, variable):
        self.variables.append(variable)
        self.symbols.append(variable.symbol)

    def list_variables(self):
        return ", ".join(self.symbols)
