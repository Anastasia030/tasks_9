import time
import random


class NotSleeping:
    """
    The class of the person who can't sleep
    """

    def __init__(self, count):
        """
        The method that defines the count of sheeps
        :param count: string contains the count of sheeps
        """
        self.count = count

    def add_sheep(self):
        """
        The method that allows you to count sheep
        :return: the number of sheep
        """
        for count_sheep in range(1, 100):
            time.sleep(1)
            print('Sheep:', count_sheep)
            self.count += 1

    @staticmethod
    def lost():
        number = 1
        r = random.randint(1, 10)
        while number <= r:
            print(number)
            number += 1
            time.sleep(1)
            if number == r:
                print("Try again!")
                number = 1
                r = random.randint(1, 10)

    def get_count_sheeps(self):
        return self.count

    def __str__(self):
        """
        The method outputs a string with the count of sheeps
        :return: string with the count of sheeps
        """
        return f'The falling asleep person counted: {self.count} sheeps'

    def __repr__(self):
        """
        The method outputs a string with the name of the person
        :return: string with the name of the person
        """
        return self.__str__()

