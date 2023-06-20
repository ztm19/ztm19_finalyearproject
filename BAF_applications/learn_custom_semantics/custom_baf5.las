% Examples

% Experiment 1

#neg({out(1), out(2), out(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg({in(1), out(2), out(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg({out(1), in(2), out(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg({out(1), out(2), in(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg({in(1), in(2), out(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg({in(1), out(2), in(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#pos({out(1), in(2), in(3)},
     {in(1), out(2), out(3)},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg({in(1), in(2), in(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

% Experiment 2 
#neg({out(4), out(5), out(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg({in(4), out(5), out(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg({out(4), in(5), out(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg({out(4), out(5), in(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg({in(4), in(5), out(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg({in(4), out(5), in(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg({out(4), in(5), in(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#pos({in(4), in(5), in(6)},
     {out(4), out(5), out(6)},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

% Experiment 3

#neg({out(7), out(8), out(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), out(8), out(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({out(7), in(8), out(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({out(7), out(8), in(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({out(7), out(8), out(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), in(8), out(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), out(8), in(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), out(8), out(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({out(7), in(8), in(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({out(7), in(8), out(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos({out(7), out(8), in(9), in(10)},
     {in(7), in(8), out(9), out(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), in(8), in(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), in(8), out(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), out(8), in(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({out(7), in(8), in(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg({in(7), in(8), in(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

% Experiment 4

#neg({out(11), out(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), out(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({out(11), in(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({out(11), out(12), in(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({out(11), out(12), out(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), in(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), out(12), in(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), out(12), out(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({out(11), in(12), in(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos({out(11), in(12), out(13), in(14)},
     {in(11), out(12), in(13), out(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({out(11), out(12), in(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), in(12), in(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), in(12), out(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), out(12), in(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({out(11), in(12), in(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg({in(11), in(12), in(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

% Experiment 5

#neg({out(15), out(16), out(17)},
     {},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#neg({in(15), out(16), out(17)},
     {},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#neg({out(15), in(16), out(17)},
     {},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#neg({out(15), out(16), in(17)},
     {},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#neg({in(15), in(16), out(17)},
     {},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#neg({in(15), out(16), in(17)},
     {},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos({out(15), in(16), in(17)},
     {in(15), out(16), out(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#neg({in(15), in(16), in(17)},
     {},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

% Definitions

support(X,Z) :- support(X,Y), support(Y,Z).

supported(X) :- support(Y,X), in(Y).

defeat(X,Y) :- att(Z,Y), support(X,Z). 
defeat(X,Y) :- att(X,Z), support(Z,Y). 
defeat(X,Y) :- att(X,Y).

defeated(X) :- in(Y), defeat(Y,X).

not_defended(X) :- defeat(Y,X), not defeated(Y).

% Mode declarations

#modeh(in(var(arg))).
#modeh(out(var(arg))).

#modeb(in(var(arg))).
#modeb(out(var(arg))).
#modeb(arg(var(arg)), (positive)).
#modeb(att(var(arg), var(arg))).
#modeb(support(var(arg))).
#modeb(supported(var(arg))).
#modeb(defeat(var(arg))).
#modeb(defeated(var(arg))).
#modeb(not_defended(var(arg))).

#maxv(2).

