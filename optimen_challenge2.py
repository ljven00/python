import sys

# list of data of type BIDGROUPS
bidgrps = []
index = -1

class BIDGROUP:
    """Holds data with type BIDGROUP"""
    def __init__(self, temp: list):
        self.values = temp
        self.crew_id, self.status, self.stype, \
            self.bid_grp, self.line, self.subline, \
            self.int1, self.str1, *self.remaining = self.values
        self.int1 = int(self.int1)
        self.group = []

    def trip_indexes(self):
        """returns indexes of data under the BIDGROUP that has type TRIP_ID"""
        indexes = []
        for i in range(len(self.group)):
            index = self.group[i].find("TRIP_ID")
            if index != -1:
                indexes.append(i)
        return indexes

    def parse(self):
        """parses a BIDGROUP data and sets the line column accordingly for type TRIP_ID"""
        indexes = self.trip_indexes()
        if len(indexes) > 0:
            first_line = int(self.group[indexes[0]].split(", ")[4])
            for i in range(len(indexes)):
                temp = self.group[indexes[i]].split(", ")
                temp[4] = str(first_line)
                self.group[indexes[i]] = ", ".join(temp)
                first_line += 1


    def __str__(self):
        self.values[6] = str(self.int1)
        val = ", ".join(self.values)
        val += "\n"
        for s in self.group:
            val += f"{s}\n"
        return val.strip("\n")

    def add_to_group(self, data: str):
        """adds group under BIDGROUP to BIDGROUP group"""
        self.group.append(data)


# takes input from standard input
for line in sys.stdin:
    # discards blank lines
    if line.isspace():
        break
    new_line = line.strip("\n")
    temp = new_line.split(", ")
    # parse input to create BIDGROUP Object and appends groups under the same category
    if temp[2].strip() == '"BIDGROUP"':
        index += 1
        bid = BIDGROUP(temp)
        bidgrps.append(bid)
    else:
        if temp[2].strip() == '"ADVANCED_TRIP"':
            temp_str1 = temp[7].strip('"').split(",")
            bidgrps[index].int1 += len(temp_str1) - 1
            bid_line = int(temp[4])
            for trip in temp_str1:
                temp[2] = '"TRIP_ID"'
                temp[4] = str(bid_line)
                temp[7] = f'"{trip[:4]}"'
                temp[10] = trip[4:]
                bidgrps[index].add_to_group(", ".join(temp))
                bid_line += 1
        else:
            bidgrps[index].add_to_group(new_line)



print("-" * 10)
for g in bidgrps:
    g.parse()
    print(g)















# def solveMeFirst(a: int, b: int):
#     """return sum of a in b"""
#     return a + b
#
# def getInput():
#     """returns two integers in the range 1 - 1000 inclusive"""
#     while True:
#         try:
#             a = int(input("Enter first integer (1 - 1000):"))
#             b = int(input("Enter second integer (1 - 1000):"))
#             assert 1 <= a <= 1000 and 1 <= b <= 1000
#             break
#         except ValueError:
#             print("Integer only integer value like 1, 4, 8")
#         except AssertionError:
#             print("Value must be in range 1 <= a <= 1000")
#     return a, b
#
# a, b = getInput()
# res = solveMeFirst(a, b)
# print(res)