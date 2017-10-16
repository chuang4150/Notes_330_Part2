#https://stackoverflow.com/questions/16780014/import-file-from-parent-directory
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from note_group import NoteGroup
from note_content import NoteContent
import unittest

class TestNoteGroup(unittest.TestCase):
    notes = (NoteContent("a", "^e ^f"),
             NoteContent("b", "#2 #3 #4 #5 @1 @2 @3 @4 ^a"),
             NoteContent("c", "#3 #4 #5 @2 @3 @4 ^d"),
             NoteContent("d", "#4 #5 @3 @4"),
             NoteContent("e", "#5 @4 ^c"),
             NoteContent("f", "^c ^e"))
    ng = NoteGroup(notes)

    #tests use set to verify that all elements are the same, order does not matter
    
    def test_with_id(self):
        self.assertEqual(self.ng.with_id("a"), self.notes[0])
        self.assertEqual(self.ng.with_id("b"), self.notes[1])
        self.assertEqual(self.ng.with_id("c"), self.notes[2])
        self.assertEqual(self.ng.with_id("d"), self.notes[3])
        self.assertEqual(self.ng.with_id("e"), self.notes[4])
        self.assertEqual(self.ng.with_id("f"), self.notes[5])

    def test_with_mentions(self):
        self.assertEqual(set(self.ng.with_mentions()), set(self.notes[1:5]))

    def test_with_mention(self):
        self.assertEqual(set(self.ng.with_mention("4")), set(self.notes[1:5]))
        self.assertEqual(set(self.ng.with_mention("3")), set(self.notes[1:4]))
        self.assertEqual(set(self.ng.with_mention("2")), set(self.notes[1:3]))
        self.assertEqual(set(self.ng.with_mention("1")), set(self.notes[1:2]))

    def test_with_topic(self):
        self.assertEqual(set(self.ng.with_topic("5")), set(self.notes[1:5]))
        self.assertEqual(set(self.ng.with_topic("4")), set(self.notes[1:4]))
        self.assertEqual(set(self.ng.with_topic("3")), set(self.notes[1:3]))
        self.assertEqual(set(self.ng.with_topic("2")), set(self.notes[1:2]))

    def test_mentions(self):
        self.assertEqual(self.ng.mentions, {"1", "2", "3", "4"})

    def test_topics(self):
        self.assertEqual(self.ng.topics, {"2", "3", "4", "5"})

    def test_topo_sort(self):
        expected_sort = ["b", "a", "f", "e", "c", "d"]
        ng_topo_sort = list(map(lambda x: x.unique_id, self.ng.topo_sort()))
        self.assertEqual(expected_sort, ng_topo_sort)

    def test_referenced_notes(self):
        self.assertEqual(set(self.ng.referenced_notes(self.notes[0])),
                         set(self.notes[4:6]))
        self.assertEqual(set(self.ng.referenced_notes(self.notes[1])),
                         set(self.notes[0:1]))
        self.assertEqual(set(self.ng.referenced_notes(self.notes[2])),
                         set(self.notes[3:4]))
        self.assertEqual(self.ng.referenced_notes(self.notes[3]), list())
        self.assertEqual(set(self.ng.referenced_notes(self.notes[4])),
                         set(self.notes[2:3]))
        self.assertEqual(set(self.ng.referenced_notes(self.notes[5])),
                         {self.ng.with_id("c"), self.ng.with_id("e")})
        
    def test_modifying_notes(self):
        #add
        noteG = NoteContent("g", "@mention #topic")
        self.ng.add_note(noteG)
        self.assertEqual(self.ng.with_id("g"), noteG)
        self.assertEqual(self.ng.mentions, {"1", "2", "3", "4", "mention"})
        self.assertEqual(self.ng.topics, {"2", "3", "4", "5", "topic"})

        #edit
        noteG = NoteContent("g", "@newmention #newtopic")
        self.ng.edit_note(noteG)
        self.assertEqual(self.ng.with_id("g"), noteG)
        self.assertEqual(self.ng.mentions, {"1", "2", "3", "4", "newmention"})
        self.assertEqual(self.ng.topics, {"2", "3", "4", "5", "newtopic"})

        #delete
        self.ng.delete_note(noteG)
        self.assertEqual(self.ng.with_id("g"), None)
        self.assertEqual(self.ng.mentions, {"1", "2", "3", "4"})
        self.assertEqual(self.ng.topics, {"2", "3", "4", "5"})

    def test_ids(self):
        self.assertEqual({"a", "b", "c", "d", "e", "f"}, set(self.ng.ids()))

if __name__ == '__main__':
    unittest.main()
