width(2).
width(3).
order(2, 3).
order(3, 2).
#const npat = 2.
pattern(1, 3, 2). %pattern(patternid, width, count)
pattern(2, 2, 3).

cut(1..npat, w) :- I = 1..n, width(w).
1 { cut(1..nPAT) }.

#minimize { 1, X : cut(X) }.

:- not fulfill(I), order(I).
fulfill(I) :- order(I), sum { Y : nbr(I,Y), cut(Y) } >= order(I).