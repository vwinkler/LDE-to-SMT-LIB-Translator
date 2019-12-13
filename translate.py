import sys
from read import read
from printSMTLIB import *
from LinearDiophanticEquation import LinearDiophanticEquation


makeVariableName = lambda n: "x{}".format(n)
equations, maxVariableIndex = read(makeVariableName)

printer = SMTLIBDiophanticEquationSystemPrinter(sys.stdout)

printer.printPreamble()
printer.printConstDeclarations([makeVariableName(n) for n in range(1, maxVariableIndex + 1)])
printer.printEquationAssertions(equations)
printer.printEpilogue()
