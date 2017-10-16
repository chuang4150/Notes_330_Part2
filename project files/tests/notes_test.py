#https://stackoverflow.com/questions/16780014/import-file-from-parent-directory
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from note_content import NoteContent
import unittest

class TestNote(unittest.TestCase):

    body = "@mentiontest @anothermention #topic ^abc ^def"
    test_note = NoteContent("xyz", body)
    
    def test_has_mention(self):
        self.assertTrue(self.test_note.has_mention("mentiontest"))
        self.assertFalse(self.test_note.has_mention("should be false"))

    def test_mention_count(self):
        self.assertEqual(self.test_note.mention_count(), 2)

    def test_has_topic(self):
        self.assertTrue(self.test_note.has_topic("topic"))
        self.assertFalse(self.test_note.has_topic("should be false"))

    def test_references(self):
        self.assertTrue(self.test_note.has_reference("abc"))
        self.assertFalse(self.test_note.has_reference("false"))

    def test_eq(self):
        self.second_test_note = NoteContent("xyz", "note body")
        self.third_test_note = NoteContent("abc", "note body")
        self.assertEqual(self.test_note, self.second_test_note)
        self.assertNotEqual(self.test_note, self.third_test_note)

if __name__ == '__main__':
    unittest.main()
