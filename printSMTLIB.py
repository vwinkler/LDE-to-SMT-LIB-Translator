from LinearDiophanticEquation import LinearDiophanticEquation

class SMTLIBDiophanticEquationSystemPrinter:
    def __init__(self, outstream):
        self.outstream = outstream
        
    def printPreamble(self):
        self.outstream.write("(set-option :produce-models true)\n")
        self.outstream.write("(set-logic QF_LIA)\n")
        
    def printConstDeclarations(self, names):
        for name in names:
            self.printConstDeclaration(name)
        
    def printConstDeclaration(self, name):
        self.outstream.write("(declare-const {} Int)\n".format(name))
        
    def printEquationAssertions(self, equations):
        self.printBeginEquations()
        self.printEquations(equations)
        self.printEndEquations()
        
    def printBeginEquations(self):
        self.outstream.write("(assert\n")
        self.outstream.write("\t(and\n")
        
    def printEquations(self, equations):
        for equation in equations:
            self.printEquation(equation)

    def printEquation(self, equation):
        self.outstream.write("\t\t(= ")
        self.printLeftEquationSide(equation)
        self.outstream.write(" ")
        self.printRightEquationSide(equation)
        self.outstream.write(")\n")
    
    def printLeftEquationSide(self, equation):
        if len(equation.coefficients) == 0:
            self.outstream.write("0")
        else:
            self.outstream.write("(+ ")
            self.printTerms(equation.coefficients)
            self.outstream.write(")")
    
    def printTerms(self, coefficients):
        skipWhitespace = True
        for variableName in coefficients:
            if skipWhitespace:
                skipWhitespace = False
            else:
                self.outstream.write(" ")
            self.printTerm(variableName, coefficients[variableName])
    
    def printTerm(self, variableName, coefficient):
        self.outstream.write("(* {} {})".format(coefficient, variableName))
        
    def printRightEquationSide(self, equation):
        self.outstream.write("{}".format(equation.getConstant()))
    
    def printEndEquations(self):
        self.outstream.write("\t)\n")
        self.outstream.write(")\n")
    
    def printEpilogue(self):
        self.outstream.write("(check-sat)\n")
        self.outstream.write("(get-model)\n")
