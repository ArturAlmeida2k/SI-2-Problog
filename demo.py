#!/usr/bin/env python3
from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable
import os

def demos(inp):
    if inp == 1:
        string = """0.4::heads(1).
0.7::heads(2).
0.5::heads(3).
win :- heads(1).
win :- heads(2),heads(3).
query(heads(_)).
query(win).""" 

    elif inp == 2:
        string = """0.4::heads(1).
0.7::heads(2).
0.5::heads(3).
win :- heads(1).
win :- heads(2),heads(3).
query(heads(_)).
query(win).
evidence(heads(3), false).""" 


    elif inp == 3:
        string = """0.5::weather(sun,0) ; 0.5::weather(rain,0).

0.6::weather(sun,T) ; 0.4::weather(rain,T) :- T>0, Tprev is T-1, weather(sun,Tprev).
0.2::weather(sun,T) ; 0.8::weather(rain,T) :- T>0, Tprev is T-1, weather(rain,Tprev).

query(weather(_,10)).""" 

    elif inp == 4:
        string = """person(john).
person(mary).

0.001::burglary.
0.02::earthquake.

0.9::alarm :- burglary.
0.1::alarm :- earthquake, \+burglary.
0.001::alarm :- \+burglary, \+earthquake.

0.95::calls(mary) :- alarm.
0.001::calls(mary) :- \+alarm.
0.9::calls(john) :- alarm.
0.0::calls(john) :- \+alarm.


evidence(calls(_)).

query(alarm).
query(burglary).
query(earthquake)."""
    
    elif inp == 5:
        string = """weight(skis,6).
weight(boots,4).
weight(helmet,3).
weight(gloves,2).

P::pack(Item) :- weight(Item,Weight), P is 1.0/Weight.

excess(Limit) :- excess([skis,boots,helmet,gloves],Limit).

excess([],Limit) :- Limit<0.
excess([I|R],Limit) :- pack(I), weight(I,W), L is Limit-W, excess(R,L).
excess([I|R],Limit) :- \+pack(I), excess(R,Limit).

constraint :- pack(helmet).
constraint :- pack(boots).

evidence(constraint).
evidence(excess(10),false).
query(pack(_))."""

    elif inp == 6:
        string = """:- use_module(library(apply)).
:- use_module(library(lists)).

PH::make_coin(C,PH).
coin(C) :- make_coin(C,0.8).
tonum(C, Num) :- (coin(C), Num=1; \+coin(C), Num=0).

total(S) :-
    findall(X, between(1,10,X), L),
    maplist(tonum, L, Nums),
    sum_list(Nums, S).

query(total(_))."""

    print("\033[F", end="")
    print(string)
    input()

    p = PrologString(string)

    dictionary = get_evaluatable().create_from(p).evaluate()
    dictionary = dict(sorted(dictionary.items(), key=lambda x: str(x[0])))   
    for k in dictionary:
        print(f'{k}: {dictionary[k]:.5f}')

    input()


key = 1
os.system('clear')

while key != 0:
    try:
        key = int(input())

    except:
        os.system('clear')
        break

    if key != 0:
        demos(key)
    
    os.system('clear')




