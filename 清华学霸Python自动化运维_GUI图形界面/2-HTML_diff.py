#coding:utf-8
import difflib

string1="""
In some circumstances you may wish to manually 
create your domain custom resource. If you have1
 created your own Docker image containing your 
 domain and the specific patches that you require,
  then this approach will probably be most suitable for your needs.
"""
string2="""
In some circumstances you may wish to manually 
create your domain custom resource. If you have
 created your own Docker image containing your 
 domain and the specific patches that you require,
  then this approach will probably be most suitable for your needs.
"""
text1_lines=string1.splitlines()
text2_lines=string2.splitlines()
d=difflib.HtmlDiff()
# print(d.make_file(text1_lines,text2_lines))
file=open("diff.html","w")
file.write(d.make_file(text1_lines,text2_lines))
file.close()

print(d.make_table(text2_lines,text1_lines))
filetable=open("difft.html","w")
filetable.write(d.make_table(text2_lines,text1_lines))
filetable.close()