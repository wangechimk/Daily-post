import unittest
from models import Sources

class SourcesTest(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.new_source = Sources('bbc-news','BBC News', 'for up-to the minute news', 'https://www.bbc.com')

    def test_source(self):
        """
        test for creation of a new instance
        """
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init(self):
        """
        """
        self.new_source.id = 'bbc-news'
        self.new_source.name='BBC News'
        self.new_source.description = 'for up-to the minute news'
        self.new_source.url='https://www.bbc.com'

if __name__ == '__main__':
    unittest.main() 