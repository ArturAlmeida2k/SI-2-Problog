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




