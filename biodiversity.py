"""
    File: biodiversity.py
    Author: Anna Rowena Waldron
    Purpose: Using two files of national parks and species in the
        national park, calculate the  density of different kinds
        of plant and/or animal life for each park, and print out the
        heighest averages.
    Class: CSC 120, Spring 2018
    Section: 1G
"""
def main():
    """ Calls all other functions, passes parameters, and catches
    return values. No parameters of its' own or returns."""
    d_info = park_data()
    d_info = specie_data(d_info)
    averages(d_info)
    
def park_data():
    """ Processing function which uses user input to open and read
    a file that is then sorted into a dictionary based on info
    of park names and the total acres of each park. Sets a tuple as
    the value of each key in the dictionary to store the acres and
    two other integer values to be used late.
    Parameters: N/A
    Returns: dictionary d_info
    Pre-Condition: N/A
    Post-Condition: d_info is a dictionary keyed by strings and valued
        as a tuple of lists. 
    """
    park = open(input())
    d_info = {}
    check = 0
    for line in park.readlines():
        rock = ([], [0], [0])
        if line[0] == '#':
            continue
        line = line.strip().split(',')
        ### INVARIANT: park name index 0, acres index 2
        assert len(line) == 5
        if line[0][-1] == 'k' or 'e' and line[0] not in d_info:
            check += 1
            rock[0].append(int(line[2]))
            d_info[line[0]] = rock
            assert check == len(d_info)
    park.close()
    return d_info

def specie_data(d_info):
    """ Second processing function that uses user input to open
    and read a file to then add values to the lists inside the tuples
    of the dictionary, based on number of differe flora or fauna species
    are in each national park.
    Parameters: d_info is a dictionary of tuples of lists.
    Returns: d_info with added values to the last two lists in each
        tuple in the dictionary.
    Pre-condition: the last two lists of each tuple in the dictionary
        are set as 0.
    Post-Condition: The last two lists of each tuple in the dictionary
        are integer numbers of species of flora in list index 1 and
        species of fauna in list index 2."""
    assert type(d_info) == dict
    specie = open(input())
    Cgory = {'Flora': ('Algae', 'Fungi', 'Nonvascular Plant', \
                       'Vascular Plant'),
             'Fauna': ('Amphibian', 'Bird', 'Crab/Lobster/Shrimp', 'Fish', \
                       'Insect', 'Invertebrate', 'Mammal', 'Reptile', \
                       'Slug/Snail', 'Spider/Scorpion')}
    for line in specie.readlines():
        line = line.strip().split(',')
        ### INVARIANT: park name index 0, category index 1.
        assert len(line) >= 2
        if line[0] in d_info and len(line[1]) > 0:
            if line[1] in Cgory['Flora']:
                d_info[line[0]][1][0] += 1
                assert type(d_info[line[0]][1][0]) == int
            if line[1] in Cgory['Fauna']:
                d_info[line[0]][2][0] += 1
                assert type(d_info[line[0]][2][0]) == int
        else:
            continue
    specie.close()      #closes 2nd file
    return d_info

def averages(d_info):
    """Last function to run which takes the park info dictionary and
    finds the averages of each park's flora and fauna numbers by
    dividing by acres, then prints out the results of each park's
    name and both flora/fauna per acre.
    Parameters: d_info containing the name of each park and
        numbers for acres, flora, and fauna.
    Returns: no returns only prints.
    Pre-Condition: averages of flora and fauna per acre still
        unknown.
    Post-Condition: finds the averages and prints them in a
        format to the user. """
    assert type(d_info) == dict
    for name, vals in d_info.items():
        assert type(name) == str and type(vals) == tuple
        if vals[1][0] > 0 and vals[2][0] > 0 and vals[0][0] > 0:
            score_flor = vals[1][0] / vals[0][0]
            score_fau = vals[2][0] / vals[0][0]
            print("{} -- flora: {:f} per acre; fauna: {:f} per acre"\
                  .format(name, score_flor, score_fau))
        else:
            ### INVARIANT: lacking info for park.
            print("{} -- no data available".format(name))
        
        
        

"""Calls the main function. """
main()
