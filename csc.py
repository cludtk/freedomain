__author__ = 'cvl'


def numberic_system(base_system):
    result = {}
    for csc_n in base_system:
        result[csc_n] = base_system.find(csc_n)
    return result


class CSC(object):
    system = {}

    def __init__(self, alphabet):
        self.system = numberic_system(alphabet)

    def csc(self, sym):
        result = ''
        for s in sym:
            result += str(self.system[s])
        return result

    def r_csc(self, num):
        for key in self.system.keys():
            if self.system[key] == int(num):
                return key
        return 'out_of_range'

    def increment(self, csc_number):
        csc_len = len(csc_number)
        i = 0
        while 1:
            if i > csc_len:
                csc_number += '0'
            if i == csc_len:
                csc_number += '0'
                break

            num = csc_number[i]
            if num in self.system.keys():
                csc_result = self.r_csc(int(self.csc(num)) + 1)
                if csc_result != 'out_of_range':
                    csc_number = csc_number[:i] + csc_result + csc_number[i + 1:]
                    break
                else:
                    csc_number = csc_number[:i] + '0' + csc_number[i + 1:]
                    i += 1
            else:
                csc_number = csc_number[:i] + '0' + csc_number[i + 1:]
                i += 1
        return csc_number
