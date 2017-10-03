import sys
class NoteContent(object):

    """
    This class will be used for keeping information about a note
    at runtime to generate reports. Currently this is identical
    to Team J's project 1. Changes will be made to reflect
    new features.
    """

    _ids_in_use = set()

    def __init__(self, file_name):
        self.file_name = file_name
        self.unique_id = None
        self.mentions = set()
        self.topics = set()
        self.references = set()
        self.urls = set()

    def create_id(self, unique_id):
        self.unique_id = unique_id
        if unique_id in self._ids_in_use:
            print("WARNING: duplicate id. Program terminating.")
            sys.exit(1)
        self._ids_in_use.add(unique_id)

    def add_mentions(self, *items):
        self.mentions.update(items)

    def has_mention(self, item):
        return item in self.mentions

    def mention_count(self):
        return len(self.mentions)
    
    def add_topics(self, *items):
        self.topics.update(items)

    def has_topic(self, item):
        return item in self.topics

    def add_references(self, *ref_id):
        self.references.update(ref_id)

    def has_reference(self, ref_id):
        return ref_id in self.references

    def add_urls(self, *items):
        self.urls.update(items)

    def __eq__(self, other):
        return self.file_name == other.file_name

    def __str__(self):
        return self.file_name

    def __hash__(self):
        return hash(str(self))
