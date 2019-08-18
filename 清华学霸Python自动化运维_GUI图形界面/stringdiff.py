#coding:utf-8
import difflib

string1="""
七巷一个漆匠，西巷一个锡匠。
七巷漆匠用了西巷锡匠的锡，
西巷锡匠拿了七巷漆匠的漆，
七巷漆匠气西巷锡匠用了漆，
西巷锡匠讥七巷漆匠拿了锡v1
"""
string2="""
七巷一个漆匠，西巷一个锡匠。
七巷漆匠用了西巷锡匠的锡，
西巷锡匠拿了七巷漆匠的漆，
七巷漆匠气西巷锡匠用了漆，
西巷锡匠讥七巷漆匠拿了锡v2
"""
text1_lines=string1.splitlines()
text2_lines=string2.splitlines()
d=difflib.Differ()
diff=d.compare(text1_lines,text2_lines)
print("\n".join(list(diff)))