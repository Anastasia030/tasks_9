import time


class NotSleeping:
    """
    The class of the person who can't sleep
    """
    def __init__(self, name):
        """
        The method that defines the instance name
        :param name: string contains the name of the person
        """
        self.name = name

    def __str__(self):
        """
        The method outputs a string with the name of the person
        :return: string with the name of the person
        """
        return f'The name of the person falling asleep: {self.name}'

    def __repr__(self):
        """
        The method outputs a string with the name of the person
        :return: string with the name of the person
        """
        return self.__str__()

    @staticmethod
    def add_sheep():
        """
        The method that allows you to count sheep
        :return: the number of sheep
        """
        for count_sheep in range(1, 100):
            time.sleep(1)
            print('Sheep:', count_sheep)
