class LinearDiophanticEquation:
    def __init__(self):
        self.coefficients = dict()
        self.constant = 0
    def addVariable(self, name, coefficient):
        assert type(coefficient) is int
        self.coefficients[name] = coefficient
    def getCoefficient(self, name):
        return self.coefficients[name]
    def setConstant(self, value):
        assert type(value) is int
        self.constant = value
    def getConstant(self):
        return self.constant
    
    def __eq__(self, other):
        if not isinstance(other, LinearDiophanticEquation):
            return NotImplemented
        return self.coefficients == other.coefficients and self.constant == other.constant
    
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        terms = []
        for name in self.coefficients:
            terms.append(str(self.coefficients[name]) + "*" + str(name))
        lhs = " + ".join(terms)
        if len(self.coefficients) == 0:
            lhs = "0"
        rhs = str(self.constant)
        return lhs + " = " + rhs
