from os import path
dir_path = path.dirname(path.realpath(__file__))

def parseLine( line ):
    """ return (int) priority of the element, and (str) element """
    #TODO implement double digit priority number
    return int(line.split('"')[2][1:2]), line.split('"')[1] 

def printDay():
    ongoing = [
            "2 leetcode/day",
            "DAY GAME NIGHT GAME",
            "skincare",
            "meditation"
            ]
    for item in ongoing:
        print item

def readElems():
    """
    read elements from todos file using parseLine
    """
    elems = []
    with open(dir_path+'/todos','r+') as f:
        for line in f:
            priority, element = parseLine( line )
            elems.append( ( priority, element ) )
        #import pdb;pdb.set_trace()
        elems.sort( key = lambda x : x[0])
    return elems

def todoDone():
    elems = readElems()
    with open(dir_path+'/todos','w') as f:
        for i in xrange(1,len(elems)):
            f.write('"{}" {}\n'.format( elems[i][1], elems[i][0] ) )
    print("OK!")

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("done", 
                        help="did you finish this? [ 'done', 'day', '' ]")

    args = parser.parse_args()
    elems = readElems()
    #import pdb;pdb.set_trace()
    print ""
    if vars(args)['done'] == 'done':
        todoDone()
    if vars(args)['done'] == 'day':
        printDay()
    else:
        print elems[0][1]
    print ""

"""
ideas:
    compute priority by deadline
    make it run when I start bash
    set this thing up like a DAG with a top sort? Hardcore OOP
    use pickle module to make persisent data structure and put todos in a DAG
"""

