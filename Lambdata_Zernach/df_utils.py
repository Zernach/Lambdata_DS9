"""
utility functions for working with DataFrames
"""

import pandas
TEST_DF = pandas.DataFrame([1, 3, 4, 5, 6])


def train_val_test_split(df):
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df, train_size=0.70, test_size=0.30, random_state=42)
    train, val = train_test_split(train, train_size=0.50, test_size=0.50, random_state=42)
    print(train.shape, val.shape, test.shape)
    return train, val, test


def list_to_df_col(list, df):
    series = pd.Series(list)
    df['new_col'] = series
    return df

"""
Classes to represent games.
"""

from random import random


class Game:
    """
    General representation of an abstract game.
    """
    def __init__(self, rounds=2, player1="Nicole", player2 ="Kumar"):
        self.rounds = 2
        self.steps = 5
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """
        Print the game players
        """
        print('{} is playing {}'.format(self.player1,self.player2))

    def add_round(self):
        """
        Increment rounds by 1
        """
        self.rounds += 1

    def winner(self):
        """randomly pick and return winner"""
        return self.player1 if random() > 0.5 else self.player2

class Tic(Game):
    """
    Tictactoe subclass of Game
    """

    def __init__(self, rounds=3, player1='Superman', player2='Stephanie'):
        super().__init__(rounds, player1, player2)

    def print_players(self):
        print('{} is playing Tic Tac Toe with {}'.format(self.player1,
        self.player2))
