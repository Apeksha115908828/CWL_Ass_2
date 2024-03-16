% Generate

{ cycle(X,Y) : cost(X,Y, _) } = 1 :- node(X).
{ cycle(X,Y) : cost(X,Y, _) } = 1 :- node(Y).
% Define

reached(Y) :- cycle(1,Y).
reached(Y) :- cycle(X,Y), reached(X).

% Test
:- node(Y), not reached(Y).

% Display
#show cycle/2.

% Optimize
#minimize { C,X,Y : cycle(X,Y), cost(X,Y,C) }.







