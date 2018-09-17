import unittest
import todo
from os import path
dir_path = path.dirname(path.realpath(__file__))

class testTODO( unittest.TestCase ):

    def test_readElems( self ):
        self.assertIsNotNone( todo.readElems() )

    def test_todoDone( self ):

        with open(dir_path+'/todos','a') as f:
            f.write('"[test elem]" 0')
           
        #import pdb;pdb.set_trace() 
        elems = todo.readElems()
        self.assertEqual( "[test elem]", elems[0][1] )

        todo.todoDone()

        elems = todo.readElems()
        self.assertNotEqual( "[test elem]", elems[0][1] )

if __name__ == '__main__':
    unittest.main()
