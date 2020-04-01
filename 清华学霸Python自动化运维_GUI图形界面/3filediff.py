# coding:utf-8

import difflib


def readfile(filename):
    try:
        file = open(filename, "rb")
        text = file.read().splitlines()
        file.close()
        return text
    except IOError as e:
        print(e)


textfile1 = "install1.log"
textfile2 = "install2.log"
t1_lines = readfile(textfile1)
t2_lines = readfile(textfile2)
diff = difflib.HtmlDiff()
file = open("diffconf.html","w")
print(t1_lines)
print(t2_lines)
file.write(diff.make_file("\n".join(t1_lines),"\n".join(t2_lines)))
file.close
