##
# intro of regular expressions
#
import re
log = "July 31 05 02:45:13 [d]mycomputer bad_process[12345]: erroe"
regex = r"\[(\d+)\]"
result = re.search(regex, log)

print(result[1])
