class Point:
    """
    Class describing the coordinates of a point
    """
    def __init__(self, coordinates=None):
        """
        The method that defines the instance coordinates
        :param coordinates: the tuple with the original coordinates
        """
        self.coordinates = coordinates
        if coordinates is None:
            self.coordinates = (0, 0)

    def get_x(self):
        """
        The method that defines the x coordinate
        :return: number with an x coordinate
        """
        return self.coordinates[0]

    def get_y(self):
        """
        The method that defines the н coordinate
        :return: number with a y coordinate
        """
        return self.coordinates[1]

    def distance(self, other):
        """
        A method that determines the distance between two points
        :param other: a tuple with coordinates of another point
        :return: the number containing the distance
        """
        spacing = ((self.get_x() - other[0]) ** 2 + (self.get_y() - other[1]) ** 2) ** 0.5
        return spacing

    def sum(self, other):
        """
        The method determines the coordinates of a new point
        :param other: a tuple with coordinates of another point
        :return: a tuple with a new coordinate
        """
        new_x = self.get_x() + other[0]
        new_y = self.get_y() + other[1]
        self.coordinates = tuple([new_x, new_y])
        return self.coordinates

    def __str__(self):
        """
        The method outputs a string with the current point coordinate
        :return: string with current point coordinate
        """
        return f'The current coordinate: {self.coordinates}'

    def __repr__(self):
        """
        The method outputs a string with the current point coordinate
        :return: string with current point coordinate
        """
        return self.__str__()
