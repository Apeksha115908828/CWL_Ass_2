:- use_module(library(scasp)).

reachable(V) :- cycle(U, V), reachable(U).
reachable(A) :- cycle(V, A).

% Every node must be reachable.
:- node(U), not reachable(U).

% Choose exactly one edge from each node.
other(U, V) :-
    node(U), node(V), node(W),
    edge(U, W), V \= W, cycle(U, W).
cycle(U, V) :-
    edge(U, V), not other(U, V).

% You cannot choose two edges to the same node
:- cycle(U, W), cycle(V, W), U \= V.


travel_path(Start, Length, Cycle) :- path(Start, Start, Start, Length, [], Cycle).

path(_, X, Y, D, Prev, [X,[D],Y|Prev]) :-
    cycle_dist(X, Y, D).
path(Start, X, Y, D, Prev, Cycle) :-
    D #= D1 + D2,
    cycle_dist(Z, Y, D1), Z \= Start,
    path(Start, X, Z, D2, [([D1],Y)|Prev], Cycle).

edge(X,Y) :- cost(X,Y,D).
cycle_dist(U,V,D) :-
    cycle(U,V), cost(U,V,D).

?- travel_path(1, D, Cycle).

#show travel_path/3, cycle_dist/3.