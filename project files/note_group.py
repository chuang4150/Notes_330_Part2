from note_content import NoteContent
from collections import deque

class NoteGroup(object):

    """
    This class deals with handling groups of notes and provides
    useful methods for generating data for the reports. Currently
    this is identical to Team J's project 1. Changes will be made
    to reflect new features.
    """

    def __init__(self, *notes):
        self.notes = list(*notes)
        self.mentions = set()
        self.topics = set()
        for note in self.notes:
            self.mentions.update(note.mentions)
            self.topics.update(note.topics)

    def with_mentions(self):
        return list(filter(lambda x: x.mention_count() > 0, self.notes))

    def with_mention(self, mention):
        return list(filter(lambda x: x.has_mention(mention), self.notes))

    def with_topic(self, topic):
        return list(filter(lambda x: x.has_topic(topic), self.notes))

    def topo_sort(self):
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

        #https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf
        while(len(in_degree_zero) > 0):
            note_index = in_degree_zero.popleft()
            t_sorted.append(self.notes[note_index])
            for adjacent in graph[note_index]:
                in_degree[ids.index(adjacent)] -= 1
                if in_degree[ids.index(adjacent)] == 0:
                    in_degree_zero.append(ids.index(adjacent))

        return t_sorted
