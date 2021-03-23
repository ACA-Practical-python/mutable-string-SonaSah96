from collections.abc import MutableSequence


class MutableString(MutableSequence):
    def __init__(self, input_str):
        if not isinstance(input_str, str):
            raise Exception("String type is expected")
        self._input_str = list(input_str)

    def __str__(self):
        return "".join(self._input_str)

    def __repr__(self):
        return "".join(self._input_str)

    def __getitem__(self, key):
        return MutableString(self._input_str[key])

    def __setitem__(self, key, value):
        if not isinstance(value, (MutableString, str)):
            raise Exception("MutableString or str instance is expected")
        self._input_str[key] = value

    def __delitem__(self, key):
        del self._input_str[key]

    def __len__(self):
        return len(self._input_str)

    def __iter__(self):
        return iter(self._input_str)

    def __add__(self, other):
        if isinstance(other, MutableString):
            l_sum = self._input_str + other._input_str
            return MutableString("".join(l_sum))
        elif isinstance(other, str):
            l_sum = self._input_str + list(other)
            return MutableString("".join(l_sum))
        else:
            raise Exception("MutableString or str instance is expected")

    def insert(self, i, elem):
        self._input_str.insert(i, elem)
        return self

    def upper(self):
        self._input_str = list(str(self).upper())
        return self

    def lower(self):
        self._input_str = list(str(self).lower())
        return self

    def capitalize(self):
        self._input_str = list(str(self).capitalize())
        return self

    def title(self):
        self._input_str = list(str(self).title())
        return self

    def startswith(self, string):
        if isinstance(string, (str, tuple)):
            pair = zip(self._input_str, string)
        elif isinstance(string, MutableString):
            pair = zip(self._input_str, string._input_str)
        else:
            raise Exception("MutableString,str or tuple instance is expected")
        if all(item[0] == item[1] for item in pair):
            return True
        return False

    def endswith(self, string):
        if isinstance(string, (str, tuple)):
            pair = zip(self._input_str[::-1], string[::-1])
        elif isinstance(string, MutableString):
            pair = zip(self._input_str[::-1], string._input_str[::-1])
        else:
            raise Exception("MutableString,str or tuple instance is expected")
        if all(item[0] == item[1] for item in pair):
            return True
        return False

    def center(self, width, fill=None):
        self._input_str = list(str(self).center(width, fill))
        return self

    def find(self, string, start=None, end=None):
        if isinstance(string, MutableString):
            string = str(string)
        return str(self).find(string, start, end)

    def rfind(self, string, start=None, end=None):
        if isinstance(string, MutableString):
            string = str(string)
        return str(self).rfind(string, start, end)

    def index(self, string, start=None, end=None):
        if isinstance(string, MutableString):
            string = str(string)
        return str(self).index(string, start, end)

    def rindex(self, string, start=None, end=None):
        if isinstance(string, MutableString):
            string = str(string)
        return str(self).rindex(string, start, end)

    def split(self, symbol=None):
        if isinstance(symbol, MutableString):
            symbol = str(symbol)
        return str(self).split(symbol)

    def replace(self, old, new, count=None):
        if count is None:
            count = len(self)
        if isinstance(old, MutableString):
            old = str(old)
        if isinstance(new, MutableString):
            new = str(new)
        self._input_str = list(str(self).replace(old, new, count))
        return self

    def rreplace(self, old, new, count=None):
        if count is None:
            count = len(self)
        if isinstance(old, MutableString):
            old = str(old)
        if isinstance(new, MutableString):
            new = str(new)
        self._input_str = list((str(self)[::-1].replace(old[::-1], new[::-1], count)[::-1]))
        return self

    def isdigit(self):
        return str(self).isdigit()

    def isalpha(self):
        return str(self).isalpha()

    def isalnum(self):
        return str(self).isalnum()

    def islower(self):
        return str(self).islower()

    def isupper(self):
        return str(self).isupper()

    def isspace(self):
        return str(self).isspace()

    def istitle(self):
        return str(self).istitle()

    def join(self, array):
        self._input_str = list(str(self).join(array))
        return self

    def format(self, *args, **kwargs):
        self._input_str = list(str(self).format(*args, **kwargs))
        return self

    @staticmethod
    def ord(ch):
        if isinstance(ch, MutableString):
            ch = str(ch)
        return ord(ch)

    @staticmethod
    def chr(i):
        return MutableString(chr(i))

    def count(self, substring, start=None, end=None):
        if isinstance(substring, MutableString):
            substring = str(substring)
        return str(self).count(substring, start, end)

    def strip(self, c=None):
        self._input_str = list(str(self).strip(c))
        return self

    def lstrip(self, c=None):
        self._input_str = list(str(self).lstrip(c))
        return self

    def rstrip(self, c=None):
        self._input_str = list(str(self).rstrip(c))
        return self


