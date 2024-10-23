#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player"s scores each round."""

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, paper, scissors? ").lower()
            if choice in moves:
                break
            else:
                continue
        return choice


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = ""
        self.their_move = ""

    def move(self):
        if self.their_move == "":
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = ""
        self.their_move = ""

    def move(self):
        if self.my_move == "":
            return random.choice(moves)
        else:
            choice = moves.index(self.my_move)
            if choice == 2:
                choice = -1
            return moves[choice + 1]

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0
        self.num_round = 0

    def play_round(self):
        self.num_round += 1
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.outcome(move1, move2)
        print(f"Score: Player one {self.score1}, Player two {self.score2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def outcome(self, move1, move2):
        if move1 == move2:
            print("** TIE **")
        else:
            if beats(move1, move2):
                self.score1 += 1
                print("** PLAYER ONE WINS **")
            else:
                self.score2 += 1
                print("** PLAYER TWO WINS **")

    def play_game(self, num):
        print("Game start!")
        for round in range(num):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        if self.score1 == self.score2:
            print(f"BOTH PLAYERS HAD {self.score1}, HENCE DRAW GAME.")
        elif self.score1 > self.score2:
            print("** PLAYER ONE WON! **")
            print(f"Player one: {self.score1}  Player two {self.score2}.")
        else:
            print("** PLAYER TWO WON! **")
            print(f"Player one: {self.score1}  Player two {self.score2}.")


if __name__ == "__main__":
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game(10)
