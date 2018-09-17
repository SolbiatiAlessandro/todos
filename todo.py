def parseLine( line ):
    """ return (int) priority of the element, and (str) element """
    #TODO implement double digit priority number
    return int(line.split('"')[2][1:2]), line.split('"')[1] 

def readElems():
    """
    read elements from todos file using parseLine
    """
    elems = []
    with open('/Users/alex/Desktop/Coding/PY/TODOT/todos','r+') as f:
        for line in f:
            priority, element = parseLine( line )
            elems.append( ( priority, element ) )
        #import pdb;pdb.set_trace()
        elems.sort( key = lambda x : x[0])
    return elems

def todoDone():

    elems = readElems()
    with open('/Users/alex/Desktop/Coding/PY/TODOT/todos','w') as f:
        for i in xrange(1,len(elems)):
            f.write('"{}" {}\n'.format( elems[i][1], elems[i][0] ) )
    print("OK!")

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("done", 
                        help="did you finish this?")

    args = parser.parse_args()
    elems = readElems()
    #import pdb;pdb.set_trace()
    if vars(args)['done'] == 'done':
        todoDone()
    else:
        print elems[0][1]

"""
ideas:
    compute priority by deadline
    make it run when I start bash
"""

