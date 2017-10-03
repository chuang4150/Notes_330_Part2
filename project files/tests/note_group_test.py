#https://stackoverflow.com/questions/16780014/import-file-from-parent-directory
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from note_group import NoteGroup
from note_content import NoteContent
import unittest

class TestNoteGroup(unittest.TestCase):
    notes = (NoteContent("a"), NoteContent("b"), NoteContent("c"), NoteContent("d"), NoteContent("e"), NoteContent("f"))
    #add topics and mentions to notes b - e
    #note b has topics 2 - 5, c has 3 - 5 ... e just has 5
    #note b has mentions 1 - 4, c has 2 - 4 ... e just has 4
    for i in range(0, len(notes) - 1):
        for j in range(1, i+1):
            notes[j].add_mentions(i)
            notes[j].add_topics(i+1)
    #add ids and references
    notes[0].create_id("a")
    notes[2].create_id("c")
    notes[3].create_id("d")
    notes[4].create_id("e")
    notes[5].create_id("f")
    notes[0].add_references("e", "f")
    notes[1].add_references("a")
    notes[2].add_references("d")
    notes[4].add_references("c")
    notes[5].add_references("c", "e")
    ng = NoteGroup(notes)

    #tests use set to verify that all elements are the same, order does not matter
    
    def test_with_mentions(self):
        self.assertEqual(set(self.ng.with_mentions()), set(self.notes[1:5]))

    def test_with_mention(self):
        self.assertEqual(set(self.ng.with_mention(4)), set(self.notes[1:5]))
        self.assertEqual(set(self.ng.with_mention(3)), set(self.notes[1:4]))
        self.assertEqual(set(self.ng.with_mention(2)), set(self.notes[1:3]))
        self.assertEqual(self.ng.with_mention(1)[0], self.notes[1])

    def test_with_topic(self):
        self.assertEqual(set(self.ng.with_topic(5)), set(self.notes[1:5]))
        self.assertEqual(set(self.ng.with_topic(4)), set(self.notes[1:4]))
        self.assertEqual(set(self.ng.with_topic(3)), set(self.notes[1:3]))
        self.assertEqual(self.ng.with_topic(2)[0], self.notes[1])

    def test_mentions(self):
        self.assertEqual(self.ng.mentions, set([1, 2, 3, 4]))

    def test_topics(self):
        self.assertEqual(self.ng.topics, set([2, 3, 4, 5]))

    def test_topo_sort(self):
        expected_sort = ["b", "a", "f", "e", "c", "d"]
        ng_topo_sort = list(map(lambda x: x.file_name, self.ng.topo_sort()))
        self.assertEqual(expected_sort, ng_topo_sort)
        

if __name__ == '__main__':
    unittest.main()
