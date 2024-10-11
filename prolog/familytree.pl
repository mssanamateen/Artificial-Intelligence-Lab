male(harivansh).
male(amitabh).
male(abhishek).
female(teji).
female(jaya).
female(shweta).
female(aishwarya).
female(aradhya).

parent(harivansh,amitabh).
parent(teji,amitabh).
parent(amitabh,abhishek).
parent(amitabh,shweta).
parent(jaya,abhishek).
parent(jaya,shweta).
parent(abhishek,aradhya).
parent(aishwarya,aradhya).

mother(M,C):-female(M),parent(M,C).
father(F,C):-male(F),parent(F,C).
son(S,P):-male(S),parent(P,S).
daughter(D,P):-female(D), parent(P,D).
brother(B,S):-male(B),parent(P,B),parent(P,S).
sister(S,B):-female(S), parent(P,S), parent(P,B).
grandfather(G,C):-male(G),parent(G,M),parent(M,C).
grandmother(GM,C):-female(GM),parent(GM,M),parent(M,C).


