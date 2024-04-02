class Dog:
    """
    Class of dogs
    """
    def __init__(self, name):
        """
        The method that defines the instance name
        :param name: string contains the name of the dog
        """
        self.name = name

    def __str__(self):
        """
        The method outputs a string with the name of the dog
        :return: string with the name of the dog
        """
        return f'The name of the dog: {self.name}'

    def __repr__(self):
        """
        The method outputs a string with the name of the dog
        :return: string with the name of the dog
        """
        return self.__str__()

    def say(self):
        """
        A method that allows you to output a phrase
        :return: instance
        """
        return f'{self.name}: Гав!'
