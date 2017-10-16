from note_content import NoteContent
from collections import deque

class NoteGroup(object):

    """
    This class deals with handling groups of notes and provides
    useful methods for generating data for the reports. Changes
    will be made as needed to reflect new features.
    """

    def __init__(self, *notes):
        """create a new NoteGroup from a collection of NoteContent objects
        
        A NoteGroup object can handle the addition, deletion, and
        modification of notes that may occur after initialization.
        """
        self.notes = list(*notes)
        self.mentions = set()
        self.topics = set()
        for note in self.notes:
            self.mentions.update(note.mentions)
            self.topics.update(note.topics)

    def add_note(self, note):
        """add a note to an existing NoteGroup
        
        useful for when a new note is created after initializing a NoteGroup
        """
        self.notes.append(note)
        self.mentions.update(note.mentions)
        self.topics.update(note.topics)

    def delete_note(self, note):
        """delete a note from an existing NoteGroup

        useful for when a note is deleted after initializing a NoteGroup
        """
        self.notes.remove(note)
        self.mentions.clear()
        self.topics.clear()
        for note in self.notes:
            self.mentions.update(note.mentions)
            self.topics.update(note.topics)

    def edit_note(self, note):
        """should be called on a NoteGroup immediately after a note is edited"""
        self.delete_note(note) #note still has same identity, but may have different information
        self.add_note(note)

    def with_mentions(self):
        """returns a list of NoteContent objects containing one or more mentions"""
        return list(filter(lambda x: x.mention_count() > 0, self.notes))

    def with_mention(self, mention):
        """returns a list of NoteContent objects containing a specified mention"""
        return list(filter(lambda x: x.has_mention(mention), self.notes))

    def with_topic(self, topic):
        """returns a list of NoteContent objects containing a specified topic"""
        return list(filter(lambda x: x.has_topic(topic), self.notes))

    def topo_sort(self):
        """returns a list of all NoteContent objects in topological order

        implementation of: https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf
        """
        
        ids = list(map(lambda x: x.unique_id, self.notes))
        
        in_degree = [0] * len(self.notes)
        #list of empty lists, one for each note
        graph = [[] for i in range(len(self.notes))]

        #construct graph and in_degree array
        for i, note in enumerate(self.notes):
            graph[i].extend(note.references)
            for ref in note.references:
                in_degree[ids.index(ref)] += 1

        #initialize queue with indices of notes not referenced
        in_degree_zero = deque(i for i, x in enumerate(in_degree) if x == 0)
        t_sorted = []

        while(len(in_degree_zero) > 0):
            note_index = in_degree_zero.popleft()
            t_sorted.append(self.notes[note_index])
            for adjacent in graph[note_index]:
                in_degree[ids.index(adjacent)] -= 1
                if in_degree[ids.index(adjacent)] == 0:
                    in_degree_zero.append(ids.index(adjacent))

        return t_sorted

    def referenced_notes(self, note_content):
        """returns a list of all NoteContent objects referenced from a specified NoteContent object"""
        return list(filter(lambda x: x.unique_id in note_content.references, self.notes))

    def with_id(self, unique_id):
        """reutrn the NoteContent object matching the specified id

        will return None if no note has this id
        """
        for note in self.notes:
            if note.unique_id == unique_id:
                return note
        return None

    def ids(self):
        return list(map(lambda x: x.unique_id, self.notes))
