'''
Created on 2021/07/01

@author: laurentmichel
'''
import unittest
from utils.file_utils import FileUtils
from utils.test_runner import TestRunner

mapping_sample = FileUtils.get_datadir()
 
# Expected results
expected = {
            '8.1': 'VALID',
            '8.2': 'every $child in ./dm-mapping:COLLECTION satisfies  $child/@dmid != \'\'',
            '8.3': 'every $child in ./dm-mapping:COLLECTION satisfies  $child/@dmid != \'\'',
            '8.4': 'VALID',
            '8.5': 'dm-mapping:COLLECTION[@dmrole != \'\']) eq 0',
            '8.6': 'VALID',
            '8.7': 'VALID',
            '8.8': 'every $child in ./dm-mapping:COLLECTION satisfies count($child/dm-mapping:ATTRIBUTE) = 0',
            '8.9': 'Unexpected child with tag \'dm-mapping:BOGUS\' at position 1.',
            '8.10': 'every $child in ./dm-mapping:COLLECTION satisfies not($child/@dmid) or $child/@dmid = \'\'',
            '8.11': 'if (@dmid) then ( @dmid != \'\')',
            '8.12': 'every $child in ./dm-mapping:COLLECTION satisfies  $child/@dmrole != \'\'',
            '8.13': 'every $child in ./dm-mapping:COLLECTION satisfies  $child/@dmrole != \'\'',
            '8.14': 'VALID',
            '8.15': 'VALID',
            '8.16': 'VALID',
            '8.17': 'VALID',
            '8.18': 'VALID',
            '8.19': 'VALID',
            '8.20': 'if (count(dm-mapping:JOIN) &gt; 0 ) then (count(dm-mapping:INSTANCE) = 0) else true()',
            '8.21': 'count(dm-mapping:ATTRIBUTE) gt 0 and',
            '8.22': 'count(dm-mapping:REFERENCE) gt 0 and',
            '8.23': 'count(dm-mapping:ATTRIBUTE) gt 0 and',
            '8.24': 'Unexpected child with tag \'dm-mapping:OTHER\' at position 1.',
            }

class Test(unittest.TestCase):

    def testOK(self):
        self.assertTrue(TestRunner.regarde_si_OK(mapping_sample, "test_8"), "file should be valid")

    def testKO(self):
        self.assertTrue(TestRunner.regarde_si_KO(mapping_sample, "test_8", expected), "invalid file test failed.")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
