%task(1, 3).  % Task ID 1 with length 3
%task(2, 2).  % Task ID 2 with length 2
%task(3, 2).  % Task ID 3 with length 2s

% Parameters
%#const m = 2. % number of processors
%#const d = 5. % timeout

{start(T, 0..m-1, 0..(d-L), L)} = 1 :- task(T, L).  
:- start(T1, P, S1, _), start(T2, P, S2, _), T1 != T2, S1 == S2.
:- start(T1, P, S1, L1), start(T2, P, S2, L2), S1 > S2, S1 < S2 + L2.
