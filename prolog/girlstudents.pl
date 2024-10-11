female(afreen).
female(pranati).
female(srivalli).

student(afreen).
student(pranati).
student(srivalli).


friend(afreen,pranati).
friend(pranati,srivalli).
friend(srivalli,afreen).
friend(srivalli,pranati).


friendly(Student):-female(Student),friend(Student,_).


social(Student):-
    female(Student),
    findall(Friend,friend(Student, Friend),Friends),
    length(Friends,Count),
    Count>1.
