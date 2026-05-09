% ─── Facts: parent(Parent, Child) ───────────────────────────────────────────
% Grandparent generation
parent(george, john).
parent(george, mary).
parent(alice, john).
parent(alice, mary).

% Parent generation
parent(john, james).
parent(john, lisa).
parent(sarah, james).
parent(sarah, lisa).
parent(mary, peter).
parent(mary, anna).
parent(david, peter).
parent(david, anna).

% Child (grandchild) generation
parent(james, tom).
parent(james, sue).
parent(lisa, ben).

% Gender facts
male(george). male(john). male(david).
male(james). male(peter). male(tom). male(ben).
female(alice). female(mary). female(sarah).
female(lisa). female(anna). female(sue).

% ─── Rules ───────────────────────────────────────────────────────────────────
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
grandchild(GC, GP)  :- grandparent(GP, GC).

father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).

sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y)  :- sibling(X, Y), female(X).

uncle(U, N) :- brother(U, P), parent(P, N).
aunt(A, N)  :- sister(A, P), parent(P, N).

cousin(X, Y) :- parent(PX, X), parent(PY, Y), sibling(PX, PY).

ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).

% ─── Example queries (run in SWI-Prolog) ─────────────────────────────────────
% ?- grandparent(george, james).      % true
% ?- grandchild(tom, john).           % true
% ?- uncle(U, peter).                 % U = james ; U = ... 
% ?- cousin(james, peter).            % true
% ?- findall(C, parent(john, C), L). % L = [james, lisa]