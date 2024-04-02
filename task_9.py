class StandsDNA:
    """
    The class stores DNA strands
    """
    def __init__(self, all_strands):
        """
        A method that defines an instance of all DNA strands
        :param all_strands: a string that contains of all DNA strands
        """
        self.all_strands = all_strands

    def add_strands(self, strands):
        """
        A method that allows you to add DNA strands from a string strands
        :param strands: a string containing a string with chains
        """
        for strand in strands.split():
            self.all_strands.append(strand)

    def get_max_strands(self):
        """
        The method determines the maximum length of chains according to some parameters
        :return: a string containing chains of maximum length
        """
        max_len = len(max(self.all_strands))
        large_strands = []
        for strand in self.all_strands:
            if len(strand) == max_len and strand not in large_strands:
                large_strands.append(strand)
        large_strands.sort()
        return ' '.join(large_strands)

    def __str__(self):
        """
        The method outputs a string
        :return: with information about all the chains available to us
        """
        return f'All DNA chains: {self.all_strands}'

    def __repr__(self):
        """
        The method outputs a string
        :return: with information about all the chains available to us
        """
        return self.__str__()
