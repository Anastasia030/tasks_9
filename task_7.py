class TrafficLight:
    """
    A class describing the current traffic light signal
    """
    permissible_values = ['Green', 'Yellow', 'Red', 'Yellow']

    def __init__(self):
        """
        The method that defines the instance current traffic light signal
        """
        self.__current_signal = 0

    def next_signal(self):
        """
        The method that defines the instance next traffic light signal
        :return: a string containing next traffic light signal
        """
        next_index = self.__current_signal + 1
        if next_index == 4:
            next_index = 0
        self.__current_signal = next_index

    def __str__(self):
        """
        The method outputs a string with the current traffic light signal
        :return: string with current traffic light signal
        """
        return f'Traffic light signal: {self.permissible_values[self.__current_signal]}'

    def __repr__(self):
        """
        The method outputs a string with the current traffic light signal
        :return: string with current traffic light signal
        """
        return self.__str__()
