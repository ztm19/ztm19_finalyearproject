% Examples

#pos({in(a), in(b), in(c)},
     {},{
arg(a).
arg(b).
arg(c).
}).

#pos({in(a), out(b)},
     {},{
arg(a).
arg(b).
att(a,b).
att(b,a).
}).

#pos({out(a), out(b)},
     {},{
arg(a).
arg(b).
att(a,b).
att(b,a).
}).

#pos({in(a),out(b),in(c)},
     {},{
arg(a).
arg(b).
arg(c).

att(a, b).
att(b, c).
}).

#pos({in(a),out(b),in(c),out(d)},
     {},{
arg(a).
arg(b).
arg(c).
arg(d).
att(a, b).
att(b, c).
att(a, d).
}).


#neg({in(a),in(b),in(c),in(d)},
     {},{
arg(a).
arg(b). 
arg(c). 
arg(d). 
att(a,b).
att(b,a).
att(b,c). 
att(a,c).
att(c,d).
}).


#neg({out(a),out(b),out(c),in(d)},
     {},{
arg(a).
arg(b). 
arg(c). 
arg(d). 
att(a,b).
att(b,a).
att(b,c). 
att(a,c).
att(c,d).
}).

 
#neg({in(a),out(b),out(c),out(d)},
     {},{
arg(a).
arg(b). 
arg(c). 
arg(d). 
att(a,b).
att(b,a).
att(b,c). 
att(a,c).
att(c,d).
}).


% Definitions
support(X,Z) :- support(X,Y), support(Y,Z).
supported(X) :- support(Y,X), in(Y).
valpref(X,Y) :- valpref(X,Z), valpref(Z,Y).
pref(X,Y) :- valpref(U,V), val(X,U), val(Y,V).
pref(X,Y) :- pref(X,Z), pref(Z,Y).
defeat(X,Y) :- att(Z,Y), support(X,Z). 
defeat(X,Y) :- att(X,Z), support(Z,Y). 
defeat(X,Y) :- att(X,Y), not pref(Y,X).
defeated(X) :- in(Y), defeat(Y,X).
not_defended(X) :- defeat(Y,X), not defeated(Y).

% Mode declarations
#modeh(in(var(arg))).
#modeh(out(var(arg))).

#modeb(in(var(arg))).
#modeb(out(var(arg))).
#modeb(arg(var(arg)), (positive)).
#modeb(att(var(arg), var(arg))).
#modeb(defeated(var(arg))).
#modeb(supported(var(arg))).
#modeb(not_defended(var(arg))).

#maxv(2). 
