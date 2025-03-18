class Solution(object):
    def removeComments(self, source):
        in_block = False
        result = []
        buffer = ""

        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if line[i:i+2] == "*/":
                        in_block = False
                        i += 1  
                elif line[i:i+2] == "/*":
                    in_block = True
                    i += 1  
                elif line[i:i+2] == "//":
                    break  
                else:
                    buffer += line[i]
                i += 1

            if not in_block and buffer:
                result.append(buffer)
                buffer = ""

        return result