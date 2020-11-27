import re
string = "hello? there A-Z-R_T(,**), world, 'welcome' to python."
string = re.sub(r'\W+', ' ', string)
print(string)
