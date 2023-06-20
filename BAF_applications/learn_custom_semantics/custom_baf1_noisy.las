% Examples

% Experiment 1

#pos(e1@1, {out(1), out(2), out(3)},
     {in(1), in(2), in(3)},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#pos(e2@1, {in(1), out(2), out(3)},
     {out(1), in(2), in(3)},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#pos(e3@1, {out(1), in(2), out(3)},
     {in(1), out(2), in(3)},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#pos(e4@1, {out(1), out(2), in(3)},
     {in(1), in(2), out(3)},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg(e5@1, {in(1), in(2), out(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg(e6@1, {in(1), out(2), in(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg(e7@1, {out(1), in(2), in(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

#neg(e8@1, {in(1), in(2), in(3)},
     {},{
arg(1).
arg(2).
arg(3).
att(2,1).
att(3,1).
}).

% Experiment 2 
#pos(e9@1, {out(4), out(5), out(6)},
     {in(4), in(5), in(6)},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg(e10@1, {in(4), out(5), out(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#pos(e11@1, {out(4), in(5), out(6)},
     {in(4), out(5), in(6)},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#pos(e12@1, {out(4), out(5), in(6)},
     {in(4), in(5), out(6)},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg(e13@1, {in(4), in(5), out(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg(e14@1, {in(4), out(5), in(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg(e15@1, {out(4), in(5), in(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

#neg(e16@1, {in(4), in(5), in(6)},
     {},{
arg(4).
arg(5).
arg(6).
support(5,4).
support(6,4).
}).

% Experiment 3

#pos(e17@1, {out(7), out(8), out(9), out(10)},
     {in(7), in(8), in(9), in(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e18@1, {in(7), out(8), out(9), out(10)},
     {out(7), in(8), in(9), in(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e19@1, {out(7), in(8), out(9), out(10)},
     {in(7), out(8), in(9), in(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e20@1, {out(7), out(8), in(9), out(10)},
     {in(7), in(8), out(9), in(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e21@1, {out(7), out(8), out(9), in(10)},
     {in(7), in(8), in(9), out(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg(e22@1, {in(7), in(8), out(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e23@1, {in(7), out(8), in(9), out(10)},
     {out(7), in(8), out(9), in(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e24@1, {in(7), out(8), out(9), in(10)},
     {out(7), in(8), in(9), out(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg(e25@1, {out(7), in(8), in(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg(e26@1, {out(7), in(8), out(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e27@1, {out(7), out(8), in(9), in(10)},
     {in(7), in(8), out(9), out(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg(e28@1, {in(7), in(8), in(9), out(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg(e29@1, {in(7), in(8), out(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#pos(e30@1, {in(7), out(8), in(9), in(10)},
     {out(7), in(8), out(9), out(10)},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg(e31@1, {out(7), in(8), in(9), in(10)},
     {},{
arg(7).
arg(8).
arg(9).
arg(10).
att(8,7).
att(9,8).
att(10,8).
}).

#neg(e32@1, {in(7), in(8), in(9), in(10)},
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

#neg(e33@1, {out(11), out(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e34@1, {in(11), out(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e35@1, {out(11), in(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e36@1, {out(11), out(12), in(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos(e37@1, {out(11), out(12), out(13), in(14)},
     {in(11), in(12), in(13), out(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e38@1, {in(11), in(12), out(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e39@1, {in(11), out(12), in(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos(e40@1, {in(11), out(12), out(13), in(14)},
     {out(11), in(12), in(13), out(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos(e41@1, {out(11), in(12), in(13), out(14)},
     {in(11), out(12), out(13), in(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos(e42@1, {out(11), in(12), out(13), in(14)},
     {in(11), out(12), in(13), out(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e43@1, {out(11), out(12), in(13), in(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e44@1, {in(11), in(12), in(13), out(14)},
     {},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos(e45@1, {in(11), in(12), out(13), in(14)},
     {out(11), out(12), in(13), out(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos(e46@1, {in(11), out(12), in(13), in(14)},
     {out(11), in(12), out(13), out(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#pos(e47@1, {out(11), in(12), in(13), in(14)},
     {in(11), out(12), out(13), out(14)},{
arg(11).
arg(12).
arg(13).
arg(14).
att(12,11).
support(13,12).
att(14,13).
}).

#neg(e48@1, {in(11), in(12), in(13), in(14)},
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

#pos(e49@1, {out(15), out(16), out(17)},
     {in(15), in(16), in(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos(e50@1, {in(15), out(16), out(17)},
     {out(15), in(16), in(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos(e51@1, {out(15), in(16), out(17)},
     {in(15), out(16), in(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos(e52@1, {out(15), out(16), in(17)},
     {in(15), in(16), out(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos(e53@1, {in(15), in(16), out(17)},
     {out(15), out(16), in(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos(e54@1, {in(15), out(16), in(17)},
     {out(15), in(16), out(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos(e55@1, {out(15), in(16), in(17)},
     {in(15), out(16), out(17)},{
arg(15).
arg(16).
arg(17).
support(16,15).
att(17,15).
}).

#pos(e56@1, {in(15), in(16), in(17)},
     {out(15), out(16), out(17)},{
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
#modeb(supported(var(arg))).
#modeb(defeat(var(arg))).
#modeb(defeated(var(arg))).
#modeb(not_defended(var(arg))).

#maxv(2).

