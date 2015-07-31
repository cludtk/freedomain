__author__ = 'cvl'


class CSC(dict):

    def __init__(self, alphabet):
        return numbering_system(alphabet)

    def numbering_system(self, base_system):
        result = {}
        for csc_n in base_system:
            result[csc_n] = base_system.find(csc_n)
        return result
