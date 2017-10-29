"""
Author: John Nemeth
Sources: Class material, Previous projects
Description: Processor for data in markers file
"""

#to read in marker information for leaflet map on server
def readIn(inputFile):
    mapentries = []
    for line in inputFile:
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        parts = line.split(':')
        mapentries.append(parts[1].strip())
    return mapentries
