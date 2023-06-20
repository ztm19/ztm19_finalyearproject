import os
from constants import ASP_BASE, ASPARTIX_BASE
from clyngor import ASP

def check_consistency(semantics_asp, semantics_aspartix, semantics_name, examples_directory):
    '''
    Checks for how many of the example files, the answer sets of our learned program
    are the same as the ASPARTIX answer sets. Also, prints the name of the files for
    which they are not the same (if such exist). For stable, complete and admissible semantics.
    '''
    print(f"{semantics_name} semantics")
    count_equal = 0
    count_total = 0

    # Iterate over the files containing the test frameworks
    for filename in os.listdir(examples_directory):
        aspartix_encoding = ""
        asp_encoding = ""
        f = os.path.join(examples_directory, filename)

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

            # For all answer sets of the our learned program, find just the
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


def check_consistency_no_aspartix_base(semantics_asp, semantics_aspartix, semantics_name, examples_directory):
    '''
    Checks for how many of the example files, the answer sets of our learned program
    are the same as the ASPARTIX answer sets. Also, prints the name of the files for
    which they are not the same (if such exist). For preferred and grounded semantics.
    '''
    print(f"{semantics_name} semantics")
    count_equal = 0
    count_total = 0

    # Iterate over the files containing the test frameworks
    for filename in os.listdir(examples_directory):
        aspartix_encoding = ""
        asp_encoding = ""
        f = os.path.join(examples_directory, filename)

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