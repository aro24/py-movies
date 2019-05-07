from media import Media
from movies import Movie
import unittest

class TestMovies(unittest.TestCase):
  def setUp(self):
    pass

  def test_slug_delete(self):
    testmed = Media('!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')
    self.assertEqual(testmed.slug(), "")

  def test_slug_replace(self):
    testmed2 = Media("good to go")
    self.assertEqual(testmed2.slug(), "good-to-go")

  def test_slug_lower(self):
    testmed3 = Media("HOW")
    self.assertEqual(testmed3.slug(), "how")

  def test_abbreviation(self):
    testmov = Movie("H-h-here we go", 1999, "George Andreas", 5.28)
    self.assertEqual(testmov.abbreviation(), "hhh")
if __name__ == '__main__':
    unittest.main()