

% Ensure that for each value of T in start(T, P, S), there is only one P and S
% :- start(T, P1, S1), start(T, P2, S2), P1 != P2; S1 != S2.

% :- task(T, _), assign(T, _).
% :- start(T, P1, S1), start(T, P2, S2).
% :- assigned(T1, P), assigned(T2, P), T1 != T2.
%     start(T1, P, S1),
%     start(T2, P, S2),
%     end(T1, P, E1),
%     end(T2, P, E2),
%     S1 <= E2, S2 <= E1;
%     S1 > E2, S2 > E1.

% :- assigned(T, _), task(T, _), end(T, _, E), d <= E.

% #show start/3.
% #show assigned/2.


----------------------


% Define predicates
task(id).  % Task with unique ID
length(id, value).  % Length of task with ID
processor(id).  % Unique processor ID

% Facts (replace with actual task lengths and number of processors)
length(1, 3).
length(2, 2).
length(3, 1).
length(4, 4).

processor(1).
processor(2).

% Schedule a task on a processor at a specific time point
schedule(task_id, processor_id, start_time) :-
  task(task_id),
  processor(processor_id),
  0 <= start_time.

% Ensure no task overlaps on a single processor
schedule(T1, P, S1), schedule(T2, P, S2) :- T1 != T2, E2 = S2 + length(T2), S1 < E2, S2 < (S1 + length(T1)).

% Each task is assigned to exactly one processor
task(T) :- not schedule(T, _, _).

% Deadline constraint: all tasks must finish before the deadline (D)
schedule(T, _, S) :- S + length(T) > D.

% Find all valid schedules (comment out to find only one)
% #solve.

% Alternatively, find only one valid schedule (uncomment)
% #count #= 1;
% #solve.

------------

% Define the input data
task(1, 3).  % Task 1 has length 3
task(2, 2).  % Task 2 has length 2
task(3, 4).  % Task 3 has length 4
deadline(8). % Overall deadline is 8
processors(2). % Number of processors is 2

% l(x, y) :- y - x.

% Define the schedule: s(Task, Processor, Start_time)
1 { s(T, P, Start) : P = 1..processors(P) } 1 :- task(T, _).
:- s(T, P, Start), s(T2, P, Start2), T != T2, Start <= Start2, (Start + task(T, _)) > Start2.

% Constraints ensuring tasks start before their deadline and processors don't exceed capacity
:- s(T, P, Start), task(T, Length), Start + Length > deadline(D).
:- { s(T, P, Start) : task(T, _) } > processors(P).

% Optimization: minimize the maximum completion time
#minimize { Finish : s(T, P, Start), task(T, Length), Finish = Start + Length }.

% Display the schedule
#show s/3.

-----------------------
% Define the input data
width(1..3).
pattern(1..3).
occurs(1, 1, 1). occurs(1, 2, 2). occurs(1, 3, 1).
occurs(2, 1, 0). occurs(2, 2, 1). occurs(2, 3, 2).
occurs(3, 1, 2). occurs(3, 2, 1). occurs(3, 3, 0).
order(1, 3). order(2, 2). order(3, 2).

% Decision variables
1 { cut(P, X) : pattern(P) } 1 :- pattern(P).

% Objective function
:- not cut(_, _).

% Constraints
:- not enough_width(W), not cut(_, _).
enough_width(W) :- width(W), not order(W, _).
%:- not enough_width(W), order(W, O), not sum { A * X : occurs(W, P, A); cut(P, X) } >= O.
:- not enough_width(W), order(W, O), not sum { A * X : occurs(W, P, A), cut(P, X) } >= O.


% Minimize the total number of rolls
#minimize { X : cut(_, X) }.

% Output the solution
#show cut/2.


----------------------------------------




% Define time intervals for tasks

%{start(T, 0..m-1, 0..(d-L))} = 1 :- task(T, L).
%end(T, P, E) :- task(T, L), start(T, P, S), E = S + L, E <= d.
%legal(S1, E1, S2, E2) 
%:- start(T1, P, S1), start(T2, P, S2), end(T1, P, E1), end(T2, P, E2), S1 > S2, S1 < E2; S2 > S1, S2 < E1.
%:- { S1 > S2, S1 >= E2 } = 0, start(T1, P, S1), start(T2, P, S2), end(T1, P, E1), end(T2, P, E2),.
%:- start(T1, P, S1), start(T2, P, S2), task(T1, L1), task(T2, L2), E2 = S2+L2, E1 = S1+L1, not legal(S1, E1, S2, E2).

#show start/3.
#show end/3.
% #show legal/4.

%assigned(T, P) :- task(T, L), start(T, P, S), end(T, P, E), E == S+L, P = 0..m-1.

%end(T, P, E) :- end(T, P, E), end(T1, P1, E1), T != T1, P == P1. 
%1 {start(T, P, S) : task(T, _)} 1 :- task(T, L), m(M), P = 0..M-1, K = 5-L, S = 0..K.
%start(T, P, S) :- start

%:- start(T, P1, _), start(T, P2, _), P1 != P2.
% % Define auxiliary predicate to calculate end time
%1 {end(T, P, E) : task(T, _)} 1 :- start(T, P, S), task(T, L), E = S + L, E <= d.

% % 1 {assigned(T, P)} 1 :- task(T, _), m(M), P = 0..M-1.
% % :- task(T, _), not 1 {assigned(T, P)}, m(M).

% 1 { assign(T, P) : task(T, _) } 1 :- m(M), P = 0..M-1.

%1 {start(T, P, S)} 1 :- task(T, L), P = 0..m-1, K = 5-L, S = 0..K.