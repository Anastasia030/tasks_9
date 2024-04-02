import json


class Game:
    """
    Class of basketball teams
    """
    def __init__(self, commands):
        """
        The method that defines the instance teams
        :param commands: dictionary containing the names of the commands
        """
        self.commands = commands

    def ball_throw(self, command, points):
        """
        The method that adds points to the team
        :param command: number indicating the command number
        :param points: number indicating how many points the team scored
        """
        number = 0
        for name in self.commands:
            number += 1
            if number == command:
                self.commands[name] += points

    def get_score(self):
        """
        The method that counts the current score of the game
        :return: a tuple containing team points
        """
        game_score = []
        for point in self.commands.values():
            game_score.append(point)
        return tuple(game_score)

    def get_winner(self):
        """
        The method determines the name of the winning team
        :return: a string containing the name of the team, or a draw
        """
        if len(set(self.get_score())) == 1:
            return 'Drawn game'
        else:
            winner_points = max(self.commands.values())
            for key, val in self.commands.items():
                if val == winner_points:
                    return key

    def __str__(self, **commands):
        """
        The method outputs a string with the current score of the teams
        :return: string with current score
        """
        teams = list(self.commands.keys())
        return f'The teams {teams[0]} and {teams[1]} keep score: {self.get_score()}'

    def __repr__(self):
        """
        A method that allows you to present the result in a different format
        :return: a string in the json format
        """
        return json.dumps(self.commands, indent=4)
