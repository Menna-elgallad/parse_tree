# grammer :
# statment >> type ident = num |identifer |
# type >> num ,bool , char
# identifier >> ['a' , 'b' , 'c']
# numerics >> [0 : 9]

import re

datatype = ""
identefier = ""
value = ""
grammer = {'ids': ['a', 'b', 'c'], 'number': [str(num) for num in [x for x in range(10)]], 'type': [
    "Num", "Bool", 'Char'], 'opt': [';', '"', "="]}

print("grammer>>", grammer)


def lexical_analyzer(name):
    # opening file
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        yield line


tokens = []
data = lexical_analyzer("my  programming language .txt")
for line in data:
    tokens.append(line.split())
print(tokens)


def create_node(value, children=None):
    if children is None:
        children = []
    return {"value": value, "children": children}


# # create the tree
# root = create_node(1, [
#     create_node(2, [
#         create_node(5)
#     ]),
#     create_node(3, [
#         create_node(6),
#         create_node(7)
#     ]),
#     create_node(4)
# ])


def print_tree_as_dict(node):
    print(node)
    # for child in node["children"]:
    #     print_tree_as_dict(child)


# print_tree_as_dict(root)

# statment regular expression

# Define the statement pattern using regular expression


def checkStatment(input_string):
    pattern = r'^\s*(Num|Char|Bool)\s+([abc])\s*=\s*(\d+|[abc]|"[a-z]")\s*;\s*$'

    # Define the input string

    # Match the input string with the statement pattern
    match = re.match(pattern, input_string)

    if match:
        # Extract the data type, identifier, and value from the matched string
        datatype = match.group(1)
        identefier = match.group(2)
        value = match.group(3)

        # Do something with the extracted values
        print('Data Type:', datatype)
        print('Identifier:', identefier)
        print('Value:', value)
        return True
    else:
        print('Input does not match the statement format')
        return False


# print the tree as a dictionary


def _checkTerminals(val, input):
    terminals = []
    if input in grammer[val]:
        terminals.append(input)
        if input in list(grammer.keys()):
            _checkTerminals(input)
    return terminals


def traverseInput(tokens):
    statments = []
    statment = []
    val = ''
    for i in tokens:
        state = []

        statment = " ".join(i)
        stamtmentmatch = checkStatment(statment)
        print("statment", statment)
        if (stamtmentmatch):
            for x in i:
                if x in grammer['ids']:
                    val = "ids"
                elif x in grammer['type']:
                    val = 'type'
                elif x in grammer['opt']:
                    val = "opt"
                elif x in grammer['number']:
                    val = 'number'
                print(x, val)
                state.append([val, _checkTerminals(val, x)])
                # root = create_node(
                #     val, [create_node(x)]if x in grammer[val] else None)
                # print(print_tree_as_dict(root))
            statments.append(state)
    return statments


statments = traverseInput(tokens)
# print(statments)

parse_tree = []


def generateSubtrees(statmentss):
    program = []
    for i, st in enumerate(statmentss):
        statment = []
        for i2, st2 in enumerate(st):
            root = create_node(st2[0], create_node(st2[1][0]))
            statment.append(root)
        program.append({'statment': statment})
    return program


print(generateSubtrees(statments))
