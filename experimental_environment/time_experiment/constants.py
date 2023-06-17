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

# Construct the solution that ILASP learned with the heuristic
GROUNDED_ASP = "in(X) :- arg(X); not not_defended(X).\n\
out(X) :- not_defended(X).\n\
#heuristic in(X).[1@1, false]\n"

# Construct the solution that ILASP learned with the heuristic
PREFERRED_ASP = "in(X) :- arg(X); not defeated(X); not not_defended(X).\n\
out(X) :- not_defended(X).\n\
#heuristic out(X).[1@1, false]\n"

# Construct ASPARTIX solution for each semantics to use as baseline
STABLE_ASPARTIX = ":- out(X), not defeated(X).\n"

ADMISSIBLE_ASPARTIX = ":- in(X), not_defended(X).\n"

COMPLETE_ASPARTIX = ":- in(X), not_defended(X).\n\
:- out(X), not not_defended(X).\n"

# Construct ASPARTIX solution to use as baseline
GROUNDED_ASPARTIX = "lt(X,Y) :- arg(X),arg(Y), X<Y.\n\
nsucc(X,Z) :- lt(X,Y), lt(Y,Z).\n\
succ(X,Y) :- lt(X,Y), not nsucc(X,Y).\n\
ninf(X) :- lt(Y,X).\n\
nsup(X) :- lt(X,Y).\n\
inf(X) :- not ninf(X), arg(X).\n\
sup(X) :- not nsup(X), arg(X).\n\
defended_upto(X,Y) :- inf(Y), arg(X), not att(Y,X).\n\
defended_upto(X,Y) :- inf(Y), in(Z), att(Z,Y), att(Y,X).\n\
defended_upto(X,Y) :- succ(Z,Y), defended_upto(X,Z), not att(Y,X).\n\
defended_upto(X,Y) :- succ(Z,Y), defended_upto(X,Z), in(V), att(V,Y), att(Y,X).\n\
defended(X) :- sup(Y), defended_upto(X,Y).\n\
in(X) :- defended(X).\n"

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