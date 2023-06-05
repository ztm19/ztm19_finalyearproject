import os
from clyngor import ASP

# Directory containing the generated test frameworks
DIRECTORY = 'graphs_test_1'

# Add the definitions of defeated and not_defended as common for our program
ASP_BASE = "defeated(X) :- in(Y), att(Y,X).\n\
not_defended(X) :- att(Y,X), not defeated(Y).\n"

# Construct the solution that ILASP learned with the heuristic
PREFERRED_ASP = "in(X) :- arg(X); not defeated(X); not not_defended(X).\n\
out(X) :- not_defended(X).\n\
#heuristic out(X).[1@1, false]\n"

# Construct ASPARTIX solution to use as baseline
PREFERRED_ASPARTIX = "in(X) :- not out(X), arg(X).\n\
out(X) :- not in(X), arg(X).\n\
:- in(X), in(Y), att(X,Y).\n\
defeated(X) :- in(Y), att(Y,X).\n\
not_defended(X) :- att(Y,X), not defeated(Y).\n\
:- in(X), not_defended(X).\n\
lt(X,Y) :- arg(X),arg(Y), X<Y, not input_error.\n\
nsucc(X,Z) :- lt(X,Y), lt(Y,Z).\n\
succ(X,Y) :- lt(X,Y), not nsucc(X,Y).\n\
ninf(X) :- lt(Y,X).\n\
nsup(X) :- lt(X,Y).\n\
inf(X) :- not ninf(X), arg(X).\n\
sup(X) :- not nsup(X), arg(X).\n\
inN(X) :- in(X).\n\
inN(X) | outN(X) :- out(X).\n\
eq_upto(Y) :- inf(Y), in(Y), inN(Y).\n\
eq_upto(Y) :- inf(Y), out(Y), outN(Y).\n\
eq_upto(Y) :- succ(Z,Y), in(Y), inN(Y), eq_upto(Z).\n\
eq_upto(Y) :- succ(Z,Y), out(Y), outN(Y), eq_upto(Z).\n\
eq :- sup(Y), eq_upto(Y). \n\
undefeated_upto(X,Y) :- inf(Y), outN(X), outN(Y).\n\
undefeated_upto(X,Y) :- inf(Y), outN(X),  not att(Y,X).\n\
undefeated_upto(X,Y) :- succ(Z,Y), undefeated_upto(X,Z), outN(Y).\n\
undefeated_upto(X,Y) :- succ(Z,Y), undefeated_upto(X,Z), not att(Y,X).\n\
undefeated(X) :- sup(Y), undefeated_upto(X,Y).\n\
not_empty :- arg(X).\n\
spoil :- not not_empty.\n\
spoil :- eq.\n\
spoil :- inN(X), inN(Y), att(X,Y).\n\
spoil :- inN(X), outN(Y), att(Y,X), undefeated(Y).\n\
inN(X) :- spoil, arg(X).\n\
outN(X) :- spoil, arg(X).\n\
:- not spoil.\n"

def check_consistency(semantics_asp, semantics_aspartix, semantics_name):
    '''
    Prints the accepted arguments given the ASP encoding
    and the type of semantics.
    '''
    print(f"{semantics_name} semantics")
    count_equal = 0
    count_total = 0

    # Iterate over the files containing the test frameworks
    for filename in os.listdir(DIRECTORY):
        aspartix_encoding = ""
        asp_encoding = ""
        f = os.path.join(DIRECTORY, filename)

        if os.path.isfile(f):
            count_total = count_total + 1

            # Read the data about arguments and attacks from the file
            file = open(f, 'r')
            data = file.read()

            # Construct the full programs to find answer sets of
            aspartix_encoding = data + semantics_aspartix
            asp_encoding = ASP_BASE + data + semantics_asp

            file.close()

            aspartix_answers = ASP(aspartix_encoding)

            aspartix_all_ins = []
            asp_all_ins = []

            # For all answer sets of the ASPARTIX program, find just the
            # arguments that are in and sort them, so they are easy to compare
            for answer in aspartix_answers:
                aspartix_ins = []
                answer_set = set(answer)

                for element in answer_set:
                    if element[0] == 'in':
                        aspartix_ins.append(element[1][0])

                aspartix_ins.sort()
                aspartix_all_ins.append(aspartix_ins)

            # Sort the whole list of answer sets so we can compare
            aspartix_all_ins.sort()

            # The solving of our ASP program requires the use of Clingo with domain heuristic
            text_file = open("asp.lp", "w")
            n = text_file.write(asp_encoding)
            text_file.close()
            stream = os.popen('clingo 0 asp.lp --heuristic=domain --enum=domrec')
            output = stream.read()
            os.remove("asp.lp")
            splitted = output.split("Answer")[1:]

            # For all answer sets of our ASP program, find just the
            # arguments that are in and sort them, so they are easy to compare
            for answer in splitted:
                asp_ins = []
                answer_set = answer.split(" ")

                for element in answer_set:
                    if 'in(' in element:
                        argument = element.split("(", 1)[1]
                        argument = argument.split(")",1)[0]
                        asp_ins.append(argument)

                asp_ins.sort()
                asp_all_ins.append(asp_ins)

            # Sort the whole list of answer sets so we can compare
            asp_all_ins.sort()

            # If the final list of answer sets is not the same, we will
            # print the name of the file, we also return at the end the number
            # of results that were consistent with the ASPARTIX results
            if aspartix_all_ins == asp_all_ins:
                count_equal = count_equal + 1
            else:
                print(f)

    return count_equal, count_total


# Do the check for the preferred semantics encoding
preferred_result = check_consistency(
    PREFERRED_ASP, PREFERRED_ASPARTIX, "Preferred")
print(
    f"The number of consistent files is: {preferred_result[0]} out of {preferred_result[1]}")
print("---------------------------------------------")