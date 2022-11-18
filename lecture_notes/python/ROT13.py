
class ROT13:

    @staticmethod
    def encrypt(string: str):
        lst = list(string)
        lst.reverse()
        return "".join(lst)

"""
import string # module
str()   # built in class
"""