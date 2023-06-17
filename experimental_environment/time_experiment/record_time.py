import os
from constants import ASP_BASE, ASPARTIX_BASE
import time

def record_time_no_aspartix_base(semantics_asp, semantics_aspartix, semantics_name, examples_directory):
    '''
    Prints the accepted arguments given the ASP encoding
    and the type of semantics.
    '''
    print(f"{semantics_name} semantics")

    # Iterate over the files containing the test frameworks
    for filename in os.listdir(examples_directory):
        asp_encoding = ""
        f = os.path.join(examples_directory, filename)

        if os.path.isfile(f):

            # Read the data about arguments and attacks from the file
            file = open(f, 'r')
            data = file.read()

            asp_encoding = ASP_BASE + data + semantics_asp
            aspartix_encoding = data + semantics_aspartix

            file.close()

            print(f"{filename[:-4]} arguments")
            text_file = open("asp.lp", "w")
            n = text_file.write(asp_encoding)
            text_file.close()
            start = time.time()
            stream = os.popen('clingo asp.lp --heuristic=domain --enum=domrec')
            output = stream.read()
            print(f"ASP: {time.time()-start}s")

            text_file = open("aspartix.lp", "w")
            n = text_file.write(aspartix_encoding)
            text_file.close()
            start = time.time()
            stream = os.popen('clingo aspartix.lp')
            output = stream.read()
            print(f"ASPARTIX: {time.time()-start}s")

            print("----------------------------------------")


def record_time(semantics_asp, semantics_aspartix, semantics_name, examples_directory):
    '''
    Prints the accepted arguments given the ASP encoding
    and the type of semantics.
    '''
    print(f"{semantics_name} semantics")

    # Iterate over the files containing the test frameworks
    for filename in os.listdir(examples_directory):
        asp_encoding = ""
        f = os.path.join(examples_directory, filename)

        if os.path.isfile(f):

            # Read the data about arguments and attacks from the file
            file = open(f, 'r')
            data = file.read()

            asp_encoding = ASP_BASE + data + semantics_asp
            aspartix_encoding = ASPARTIX_BASE + data + semantics_aspartix

            file.close()

            print(f"{filename[:-4]} arguments:")
            text_file = open("asp.lp", "w")
            n = text_file.write(asp_encoding)
            text_file.close()
            start = time.time()
            stream = os.popen('clingo asp.lp')
            output = stream.read()
            print(f"ASP: {time.time()-start}s")

            text_file = open("aspartix.lp", "w")
            n = text_file.write(aspartix_encoding)
            text_file.close()
            start = time.time()
            stream = os.popen('clingo aspartix.lp')
            output = stream.read()
            print(f"ASPARTIX: {time.time()-start}s")

            print("----------------------------------------")


def record_time_mu_toksia(semantics_name, semantics_short, examples_directory):
    '''
    Prints the accepted arguments given the ASP encoding
    and the type of semantics.
    '''
    print(f"{semantics_name} semantics")

    # Iterate over the files containing the test frameworks
    for filename in os.listdir(examples_directory):
        f = os.path.join(examples_directory, filename)
        if os.path.isfile(f):

            start = time.time()
            stream = os.popen(f'./build/release/bin/mu-toksia -p SE-{semantics_short} -f {f} -fo apx')
            output = stream.read()
            print(f"{filename}: {time.time()-start}")

    print("-----------------------------------------------")