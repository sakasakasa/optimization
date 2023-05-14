from ortools.sat.python import cp_model


def main():
    # Creates model.
    model = cp_model.CpModel()

    # Defines variables, which will be optimized.
    num_vars = 3
    vars = [model.NewBoolVar("vars[%i]" % i) for i in range(num_vars)]

    # Defines negated forbidden combination of variables.
    # (Forbids the combination "vars[0]=1, vars[1]=0, vars[2]=0".)
    negated_forbidden_lits = \
        [vars[0].Not(), vars[1], vars[2]]
    
    # Adds constraints.
    model.AddBoolOr(negated_forbidden_lits)

    # Solves the problem.
    solver = cp_model.CpSolver()
    solution_printer = cp_model.VarArraySolutionPrinter(vars)

    # Writes all solutions and its statistics.
    print("< Solutions >")
    status = solver.SearchForAllSolutions(model, solution_printer)
    print()

    print("< Statistics >")
    print("Status : %s" % solver.StatusName(status))
    print("Number of solutions : %i" % solution_printer.solution_count())
    print()


if __name__ == "__main__":
    main()
