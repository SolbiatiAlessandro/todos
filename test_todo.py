import unittest
import todo

class testTODO( unittest.TestCase ):

    def test_readElems( self ):
        self.assertIsNotNone( todo.readElems() )

    def test_todoDone( self ):

        with open('/Users/alex/Desktop/Coding/PY/TODOT/todos','a') as f:
            f.write('"[test elem]" 0')
           
        #import pdb;pdb.set_trace() 
        elems = todo.readElems()
        self.assertEqual( "[test elem]", elems[0][1] )

        todo.todoDone()

        elems = todo.readElems()
        self.assertNotEqual( "[test elem]", elems[0][1] )

if __name__ == '__main__':
    unittest.main()
