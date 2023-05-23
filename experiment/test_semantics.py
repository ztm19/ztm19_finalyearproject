import os
from clyngor import ASP

# Directory containing the generated test frameworks
DIRECTORY = 'graphs_test_1'

# Construct ASPARTIX rules that are common for all programs
ASPARTIX_BASE = "in(X) :- not out(X), arg(X).\n\
out(X) :- not in(X), arg(X).\n\
:- in(X), in(Y), att(X,Y).\n\
defeated(X) :- in(Y), att(Y,X).\n\
not_defended(X) :- att(Y,X), not defeated(Y).\n"

# Add the definitions of defeated and not_defended as common for our program
ASP_BASE = "defeated(X) :- in(Y), att(Y,X).\n\
not_defended(X) :- att(Y,X), not defeated(Y).\n"

# Construct the ILASP solution for each semantics
STABLE_ASP = "out(X) :- defeated(X).\n\
in(X) :- arg(X), not out(X).\n"

ADMISSIBLE_ASP = "out(X) :- defeated(X).\n\
out(X) :- arg(X), not in(X).\n\
in(X) :- arg(X), not out(X), not not_defended(X).\n"

COMPLETE_ASP = "out(X) :- not_defended(X).\n\
in(X) :- arg(X), not out(X), not defeated(X).\n"

# Construct ASPARTIX solution for each semantics to use as baseline
STABLE_ASPARTIX = ":- out(X), not defeated(X).\n"

ADMISSIBLE_ASPARTIX = ":- in(X), not_defended(X).\n"

COMPLETE_ASPARTIX = ":- in(X), not_defended(X).\n\
:- out(X), not not_defended(X).\n"


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
            aspartix_encoding = ASPARTIX_BASE + data + semantics_aspartix
            asp_encoding = ASP_BASE + data + semantics_asp

            file.close()

            # Find the answer sets with clingo
            aspartix_answers = ASP(aspartix_encoding)
            asp_answers = ASP(asp_encoding)

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

            # For all answer sets of the ASPARTIX program, find just the
            # arguments that are in and sort them, so they are easy to compare
            for answer in asp_answers:
                asp_ins = []
                answer_set = set(answer)

                for element in answer_set:
                    if element[0] == 'in':
                        asp_ins.append(element[1][0])

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


# Do the check for the stable semantics encoding
stable_result = check_consistency(STABLE_ASP, STABLE_ASPARTIX, "Stable")
print(
    f"The number of consistent files is: {stable_result[0]} out of {stable_result[1]}")
print("---------------------------------------------")

# Do the check for the complete semantics encoding
complete_result = check_consistency(
    COMPLETE_ASP, COMPLETE_ASPARTIX, "Complete")
print(
    f"The number of consistent files is: {complete_result[0]} out of {complete_result[1]}")
print("---------------------------------------------")

# Do the check for the admissible semantics encoding
admissible_result = check_consistency(
    ADMISSIBLE_ASP, ADMISSIBLE_ASPARTIX, "Admissible")
print(
    f"The number of consistent files is: {admissible_result[0]} out of {admissible_result[1]}")
print("---------------------------------------------")
