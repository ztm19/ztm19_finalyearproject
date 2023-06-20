# A Unifying Framework for Learning Argumentation Semantics

This is my final year project for the MEng Mathematics and Computer Science degree at Imperial College London. It is about constructing a unifying framework for learning argumentation semantics for the Abstract Argumentation Framework (AAF), the Assumption-Based Argumentation Framework (ABA), the Bipolar Argumentation Framework (BAF) and the Value-Based Argumentation Framework (VAF). For each framework, Learning from Answer Sets (LAS) task encodings are designed, to be used for learning with ILASP, developed by Mark Law ([ILASP website](https://doc.ilasp.com/)). For ABA, there is a 2-step process designed to translate it to an AAF representation.

## LAS Task Encodings for AAF

You need ILASP4 installed to be able to run the learning tasks.
The learning supports the stable, the complete, the admissible, the preferred and the grounded semantics. For learning tasks for the stable, the complete and the admissible semantics (.las extension files), run the command

```bash
ILASP --version=2 {semantics}.las
```
where the name of the semantics should be put in the place of {semantics} to learn the hypothesis that together with the background knowledge covers all the examples. You can use the --debug flag to track the learning progress.

For the learning tasks for the preferred and the grounded semantics, run the command
```bash
ILASP --version=4 {semantics}.las --learn-heuristics
```
to learn the hypothesis with heuristics, since they are needed for the preferred and the
grounded semantics. 

## LAS Task Encodings for BAF and VAF
The learning supports the stable, the complete and the admissible semantics. To learn the
hypothesis, run the command
```bash
ILASP --version=2 {semantics}.las
```

## Translating ABA to AAF
We designed a 2-step process to translate an ABA framework to an AAF one, by first constructing the arguments and then generating the attacks between them. The two files construct_args.lp and generate_attacks.lp are currently working with an example of ABA framework. To construct the arguments, you will need to have Clingo installed and run
```bash
clingo 0 construct_args.lp --heuristic=domain --enum=domrec
```
To generate the attacks, you will need to run
```bash
clingo generate_attacks.lp
```

## Unifiying LAS Task
This is a unifying LAS task encoding that works for all frameworks (the encodings all have
the same background knowledge and mode declarations). To learn, run the command
```bash
ILASP --version=2 {semantics}.las
```

## Experimental Enviroment
There are two types of experiments - accuracy and time experiments. The experiments are done in Python. They contain folders with example files - generated example frameworks to
use for testing. They also have files with constants - the programs learned by ILASP for 
each semantics and the encodings done by ASPARTIX ([ASPARTIX website](https://www.dbai.tuwien.ac.at/research/argumentation/aspartix/)). 

To test the accuracy of labeling extensions according to given semantics, against the 
ASPARTIX labeling, run  
```bash
python test_semantics.py
```
in the accuracy_experiment folder.

To test the time it takes for finding one extension of frameworks of different sizes, according to given semantics, comparing our learned encodings with the ASPARTIX encodings run 
```bash
python test_semantics_ASP.py
```
in the time_experiment folder.

To compare with the time it takes $\mu$-toksia ([$\mu$-toksia website](https://bitbucket.org/andreasniskanen/mu-toksia/src/master/)) to find one extension, you have to install $\mu$-toksia and put the file test_semantics_mu_toksia.py from the time_experiment folder into the mu-toksia folder, which you will have after installing. Then run the command:
```bash
python test_semantics_mu_toksia.py
```

The file dl_requirements.txt is a Python environment file with the version of the packages we are using in the comparison with a Deep Learning algorithm (which is not included into this repository) ([Link to DL algorithm repo](https://github.com/DennisCraandijk/DL-abstract-argumentation))

## BAF Applications - Label Accepted Arguments
This is an application, in which we take a JSON file, containing arguments and the relationships between them, extracted from a 2-person dialogue. We parse the JSON file and represent the framework that it contains in ASP. We then label the accepted arguments in this framework, based on a chosen semantics. There are several experimental settings - for example 1,2,3,4,5,6,7, containing a different argumentation framework. In the file compute_extensions.py, you can choose which example file to work with. To find the extensions for all semantics (or some of them, which can be chosen from the same file), run the command
```bash
python compute_extensions.py
```

## BAF Applications - Learn Custom Semantics
We use the LAS Task constructed to learn the unique semantics that people use to reason about which arguments should be accepted as valid. The data we use for the positive and the negative examples is taken from a survey, where people are provided with 5 argumentation frameworks and they have to say which of all possible labellings of accepted arguments they consider as valid, separately for each of the frameworks. To learn the program for the semantics for an example, run the command
```bash
ILASP --version=4 {semantics}.las --learn-heuristics
```

## License

[MIT](https://choosealicense.com/licenses/mit/)