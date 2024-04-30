#!/usr/bin/env python3

from rps.players import ComputerPlayer
from rps.game import RockPaperScissors

def test1():
    p = ComputerPlayer("bot")
    rocks = 0
    scissors = 0
    papers = 0
    for _ in range(100):
        h = p.choose()
        if h =="rock":
            rocks += 1
        elif h == "scissors":
            scissors += 1
        elif h == "paper":
            papers += 1
    
    assert(rocks > 0)
    assert(papers > 0)
    assert(scissors > 0)
    print("Test 1 succeed")

def test2():
    p1 = ComputerPlayer("bot")
    p2 = ComputerPlayer("bot")
    g = RockPaperScissors(p1, p2)
    assert(g.max_turns > 1)
    print("Test 2 succeed")

def run_tests():
    test1()
    test2()

if __name__ == "__main__":
    run_tests()