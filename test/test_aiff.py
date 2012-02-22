import unittest
import aifc

class TestAiff(unittest.TestCase):

    def setUp(self):
        self.file = aifc.open('aiff_01.aif')

    def test_metaData(self):
        self.assertEqual(self.file.getnchannels(), 2)
        self.assertEqual(self.file.getsampwidth(), 2)
        self.assertEqual(self.file.getframerate(), 8000)
        self.assertEqual(self.file.getnframes(), 23493)
        self.assertEqual(self.file.getcomptype(), 'NONE')

    def test_move(self):
        self.assertEqual(self.file.tell(), 0)
        self.file.setpos(1)
        self.assertEqual(self.file.tell(), 1)
        # self.assertRaises('Error', self.file.setpos, -1)

    def tearDown(self):
        self.file.close()

suite = unittest.TestLoader().loadTestsFromTestCase(TestAiff)
unittest.TextTestRunner(verbosity=2).run(suite)
