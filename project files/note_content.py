class NoteContent(object):

    """
    This class will be used for keeping information about a note
    at runtime to generate reports. Changes will be made as needed
    to reflect new features.
    """

    _ids_in_use = set()

    def __init__(self, unique_id):
        """create a new NoteContent object using a note's unique_id"""
        if unique_id in self._ids_in_use:
            print("WARNING: duplicate id.")
        self._ids_in_use.add(unique_id)
        self.unique_id = unique_id
        self.mentions = set()
        self.topics = set()
        self.references = set()
        self.urls = set()

    def add_mentions(self, *items):
        """add a collection of mentions to this NoteContent"""
        self.mentions.update(items)

    def has_mention(self, item):
        """returns boolean for presence of a specified mention"""
        return item in self.mentions

    def mention_count(self):
        """returns number of mentions"""
        return len(self.mentions)

    def add_topics(self, *items):
        """add a collection of topics to this NoteContent"""
        self.topics.update(items)

    def has_topic(self, item):
        """returns boolean for presence of a specified topic"""
        return item in self.topics

    def add_references(self, *ref_id):
        """add a collection of references to this NoteContent"""
        self.references.update(ref_id)

    def has_reference(self, ref_id):
        """returns boolean for presence of a specified reference"""
        return ref_id in self.references

    def add_urls(self, *items):
        """add a collection of urls to this NoteContent"""
        self.urls.update(items)

    def __eq__(self, other):
        return self.unique_id == other.unique_id

    def __str__(self):
        return self.unique_id

    def __hash__(self):
        return hash(str(self))
