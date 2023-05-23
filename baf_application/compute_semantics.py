import json
from clyngor import ASP

# Read the file with arguments and relationships
FILENAME = "participant1.json"
file = open(FILENAME)
dict = json.load(file)

# Add all nodes as arg(node). in the ASP encoding
nodes = dict["nodes"]
asp_encoding = ""

for node in nodes:
    asp_encoding += "arg(" + node["id"] + ").\n"

# Add supports and attacks as support(node,node). and
# att(node,node). to the ASP encoding
links = dict["links"]

for link in links:
    relationship = "support"
    if link["relationship"] == "attack":
        relationship = "att"

    asp_encoding += relationship + "(" + link["source"] + \
        "," + link["target"] + ").\n"

# Add the background knowledge definitions for support, defeat,
# supported, defeated and not_defended to the ASP encoding
asp_encoding += "support(X,Z) :- support(X,Y), support(Y,Z).\n\
supported(X) :- support(Y,X), in(Y).\n\
defeat(X,Y) :- att(Z,Y), support(X,Z).\n\
defeat(X,Y) :- att(X,Z), support(Z,Y). \n\
defeat(X,Y) :- att(X,Y).\n\
defeated(X) :- in(Y), defeat(Y,X).\n\
not_defended(X) :- defeat(Y,X), not defeated(Y).\n"

# Construct the ILASP solution for each semantics
STABLE = "out(X) :- defeated(X).\n\
in(X) :- arg(X), not defeated(X).\n"

ADMISSIBLE = " :- not_defended(X), not out(X).\n\
out(X) :- arg(X), not in(X).\n\
in(X) :- arg(X), not out(X), not defeated(X).\n"

COMPLETE = "out(X) :- not_defended(X).\n\
in(X) :- arg(X), not defeated(X), not not_defended(X)."

def print_answers(asp, semantics):
    '''
    Prints the accepted arguments given the ASP encoding
    and the type of semantics.
    '''
    print(f"{semantics} semantics")
    answers = ASP(asp)
    i = 1

    for answer in answers:
        print(f"Accepted arguments - possibility {i}:")
        print(f"-------------------------------")
        ins = []
        answer_set = set(answer)

        for element in answer_set:
            if element[0] == 'in':
                ins.append(element[1][0])

        for node in nodes:
            if node['id'] in ins:
                print(node["text"])

        print(f"-------------------------------")

        i += 1


print_answers(asp_encoding+STABLE, "Stable")
print_answers(asp_encoding+ADMISSIBLE, "Admissible")
print_answers(asp_encoding+COMPLETE, "Complete")