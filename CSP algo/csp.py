
variables = ["A", "B", "C", "D"]
domains = {
    "A": ["Red", "Green", "Blue"],
    "B": ["Red", "Green", "Blue"],
    "C": ["Red", "Green", "Blue"],
    "D": ["Red", "Green", "Blue"]
}

# Neighbors (constraints grap     h)
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Constraint: no same color
def is_valid(var, value, assignment):
    for n in neighbors[var]:
        if n in assignment and assignment[n] == value:
            return False
    return True


# Forward checking
def forward_check(var, value, domains, assignment):
    new_domains = {v: list(domains[v]) for v in domains}

    for n in neighbors[var]:
        if n not in assignment:
            if value in new_domains[n]:
                new_domains[n].remove(value)
                if not new_domains[n]:
                    return None  # failure
    return new_domains


# Backtracking
def backtrack(assignment, domains):
    if len(assignment) == len(variables):
        return assignment

    # pick unassigned variable (simple)
    for var in variables:
        if var not in assignment:
            break

    for value in domains[var]:
        if is_valid(var, value, assignment):
            assignment[var] = value

            new_domains = forward_check(var, value, domains, assignment)
            if new_domains:
                result = backtrack(assignment, new_domains)
                if result:
                    return result

            del assignment[var]  # undo

    return None


# Run
solution = backtrack({}, domains)
print("Solution:", solution)