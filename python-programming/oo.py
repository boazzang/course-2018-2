import re

data = """
kim,fail,fail
shin,pass,fail
"""

p = re.compile("(\w{3}[,]\w{4})[,]\w{4}")
print(p.sub("\g<1>,pass", data))



