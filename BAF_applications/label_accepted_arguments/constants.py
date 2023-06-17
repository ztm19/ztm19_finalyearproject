# Construct the ILASP solution for each semantics
STABLE = "out(X) :- defeated(X).\n\
in(X) :- arg(X), not out(X).\n"

ADMISSIBLE = " :- not_defended(X), not out(X).\n\
out(X) :- arg(X), not in(X).\n\
in(X) :- arg(X), not out(X), not defeated(X).\n"

COMPLETE = "out(X) :- not_defended(X).\n\
in(X) :- arg(X), not out(X), not defeated(X).\n"
