"""
    File: abundance.py
    Author: Anna Rowena Waldron
    Purpose: Using two files of national parks and species in the
        national park, calculate the  density of different kinds
        of plant and/or animal life for each park, and print out the
        heighest averages.
    Class: CSC 120, Spring 2018
    Section: 1G
"""
def main():
    """ Main function which calls all other functions. Has
    no paramters of its' own, or returns. Catches return values
    and holds parameters passed into other two functions,species.
    """
    species = data()
    output(species)
    
def data():
    """ Function using user input as a file to create a dictionary
    using the file's information on different species in different
    parks.
    Parameters: none
    Returns: species as a dictionary with species names and
        the number of parks it can be found in.
    Pre-Condition: species is an empty dictionary.
    Post-Condition: species is a dictionary keyed by species
        name and valued at a list containing an number integer."""
    file = open(input())
    species = {}
    check = 0
    for line in file.readlines():
        lock = [0]
        if line[0] == '#':
            ### INVARIANT: if a comment line, header.
            continue
        line = line.lower().strip().split(',')
        assert len(line) >= 3
        if line[2] not in species:
            ### INVARIANT: line[2] is scientific name
            check += 1
            lock[0] += 1
            species[line[2]] = lock
        elif line[2] in species:
            species[line[2]][0] += 1
    file.close()
    assert check == len(species)
    return species

def output(species):
    """Last function which finds the maximum number of parks a species
    is found and all the species with the same number and prints them out.
    Parameters: species variable contains all species and the number
        of parks their in.
    Returns: none, uses print.
    Pre-Condition: species is a dictionary keyed by species names
        and valued by a list of a number of parks.
    Post-Condition: none just prints out species with the same max
        value of parks."""
    maxi = 0
    assert type(species) == dict
    for val in species.values():
        assert type(val) == list
        maxi = max(maxi, int(val[0]))
        ### INVARIANT: maxi is the largest number in dictionary.
    for name, val in species.items():
        assert type(name) == str
        if val[0] == maxi:
            print("{} -- {:d} parks".format(name, val[0]))

"""Calls main function. """        
main()
