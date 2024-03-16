m(8).
d(5).
task(1, 2).
task(2, 5).
task(3, 3).
task(4, 5).
task(5, 2).
task(6, 1).
task(7, 3).
task(8, 3).
task(9, 5).
task(10, 2).


% Define a predicate for the range
range(Min, Min, Max) :- Min =< Max.
range(Val, Min, Max) :- Min < Max, NewMin is Min + 1, range(Val, NewMin, Max).

% Start rule
start(T, P, S, L) :- task(T, L), m(M), d(D), range(P, 0, M1), range(S, 0, D1),  D1 #= D - L, M1 #= M - 1.

% Constraint rules
:- start(T1, P, S1, _), start(T2, P, S2, _), T1 \= T2, S1 = S2.
:- start(T1, P, S1, L1), start(T2, P, S2, L2), S1 > S2, S1 < E2, E2 #= S2 + L2.

?- start(T, P, S, L).

#show start/4.