# ─── Part (a): Australia ──────────────────────────────────────────────────────

AUSTRALIA_REGIONS = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']
AUSTRALIA_NEIGHBOURS = {
    'WA':  ['NT', 'SA'],
    'NT':  ['WA', 'SA', 'Q'],
    'SA':  ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':   ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':   ['SA', 'NSW'],
}
COLOURS_3 = ['Red', 'Green', 'Blue']

# ─── Part (b): Nairobi sub-counties ──────────────────────────────────────────

NAIROBI_REGIONS = [
    'Westlands', 'Dagoretti North', 'Dagoretti South', 'Langata',
    'Kibra', 'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi South',
    'Embakasi North', 'Embakasi Central', 'Embakasi East', 'Embakasi West',
    'Makadara', 'Kamukunji', 'Starehe', 'Mathare'
]
NAIROBI_NEIGHBOURS = {
    'Westlands':       ['Dagoretti North', 'Roysambu', 'Kasarani'],
    'Dagoretti North': ['Westlands', 'Dagoretti South', 'Kibra'],
    'Dagoretti South': ['Dagoretti North', 'Kibra', 'Langata'],
    'Langata':         ['Dagoretti South', 'Kibra', 'Embakasi West'],
    'Kibra':           ['Dagoretti North', 'Dagoretti South', 'Langata', 'Starehe', 'Kamukunji'],
    'Roysambu':        ['Westlands', 'Kasarani', 'Ruaraka'],
    'Kasarani':        ['Westlands', 'Roysambu', 'Ruaraka', 'Embakasi North'],
    'Ruaraka':         ['Roysambu', 'Kasarani', 'Embakasi North', 'Mathare'],
    'Embakasi South':  ['Embakasi Central', 'Embakasi East'],
    'Embakasi North':  ['Kasarani', 'Ruaraka', 'Embakasi Central'],
    'Embakasi Central':['Embakasi North', 'Embakasi South', 'Embakasi East', 'Makadara'],
    'Embakasi East':   ['Embakasi South', 'Embakasi Central'],
    'Embakasi West':   ['Langata', 'Starehe', 'Makadara'],
    'Makadara':        ['Embakasi Central', 'Embakasi West', 'Kamukunji', 'Starehe'],
    'Kamukunji':       ['Kibra', 'Makadara', 'Starehe', 'Mathare'],
    'Starehe':         ['Kibra', 'Embakasi West', 'Makadara', 'Kamukunji', 'Mathare'],
    'Mathare':         ['Ruaraka', 'Kamukunji', 'Starehe'],
}

# ─── Backtracking CSP Solver ──────────────────────────────────────────────────

def is_valid(region, colour, assignment, neighbours):
    """Check if assigning colour to region violates any constraint."""
    for neighbour in neighbours[region]:
        if neighbour in assignment and assignment[neighbour] == colour:
            return False
    return True

def backtrack(regions, neighbours, colours, assignment={}):
    """Recursively assign colours; return solution or None."""
    if len(assignment) == len(regions):
        return assignment  # All regions assigned — solution found

    # Pick next unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for colour in colours:
        if is_valid(region, colour, assignment, neighbours):
            assignment[region] = colour
            result = backtrack(regions, neighbours, colours, assignment)
            if result:
                return result
            del assignment[region]  # Backtrack

    return None  # No solution with current colours

def solve_map(name, regions, neighbours, colours):
    """Try to colour the map with the given colours."""
    print(f"\n── {name} ──")
    solution = backtrack(regions, neighbours, colours, {})
    if solution:
        print(f"Solution found using {len(colours)} colours:")
        for region, colour in solution.items():
            print(f"  {region:20s} → {colour}")
    else:
        print(f"No solution found with {len(colours)} colours.")
    return solution

# Part (a)
solve_map("Australia (3 colours)", AUSTRALIA_REGIONS, AUSTRALIA_NEIGHBOURS, COLOURS_3)

# Part (b) — find the MINIMUM number of colours for Nairobi
print("\n── Nairobi Sub-Counties (minimum colours) ──")
for num_colours in range(2, 6):
    colours = ['Red', 'Green', 'Blue', 'Yellow', 'Orange'][:num_colours]
    sol = backtrack(NAIROBI_REGIONS, NAIROBI_NEIGHBOURS, colours, {})
    if sol:
        print(f"Minimum colours needed: {num_colours}")
        for region, colour in sol.items():
            print(f"  {region:22s} → {colour}")
        break