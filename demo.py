import numpy
import stackprinter


def dangerous_function(blub):
    return sorted(blub, key=lambda xs: sum(xs))

try:
    somelist = [[1,2], [3,4]]
    anotherlist = [['5', 6]]
    spam = numpy.zeros((3,3))
    supersecret = "you haven't seen this"
    dangerous_function(somelist + anotherlist)
except:
    stackprinter.show(style='plaintext', source_lines=4, suppressed_vars=[r".*secret.*"])

