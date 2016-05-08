import unittest
import numpy as np
from ephys import ums2k

class UMS2KTest(unittest.TestCase):

    def test_poissfit(self):
        r = [[ 7, 5],
             [ 3, 3],
             [ 5, 7],
             [10, 2],
             [ 9, 3],
             [ 5, 4],
             [ 8, 4],
             [ 4, 5],
             [ 6, 9],
             [ 6, 3]]
        l,lci = ums2k.poissfit(r)
        assert np.allclose(l,[6.3,4.5]), l
        assert np.allclose(lci,[[4.8411,3.2823],[8.0604,6.0214]]), lci

def main():
    unittest.main()

if __name__ == '__main__':
    main()