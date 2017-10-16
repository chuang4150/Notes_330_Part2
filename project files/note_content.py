import re

class NoteContent(object):

    """
    This class will be used for keeping information about a note
    at runtime to generate reports. Changes will be made as needed
    to reflect new features.
    """

    def __init__(self, unique_id, body):
        """create a new NoteContent object using a note's unique_id and body
        
        processes body of a note and stores mentions, topics, and references
        in sets for efficient lookup
        """
        self.unique_id = unique_id
        self.body = body
        self.mentions = set(e[1:] for e in self.__find_identifiers__("@"))
        self.topics = set(e[1:] for e in self.__find_identifiers__("#"))
        self.references = set(e[1:] for e in self.__find_identifiers__("^"))

    def __find_identifiers__(self, symbol):
        if(symbol!="^"):
            pattern = r'[' + symbol + ']\S*'
        else:
            pattern= r'[' '\^' + ']\S*'
        return re.findall(pattern, self.body)

    def has_mention(self, item):
        """returns boolean for presence of a specified mention"""
        return item in self.mentions

    def mention_count(self):
        """returns number of mentions"""
        return len(self.mentions)

    def has_topic(self, item):
        """returns boolean for presence of a specified topic"""
        return item in self.topics

    def has_reference(self, ref_id):
        """returns boolean for presence of a specified reference"""
        return ref_id in self.references

    def __eq__(self, other):
        return self.unique_id == other.unique_id

    def __str__(self):
        return self.unique_id

    def __hash__(self):
        return hash(str(self))
