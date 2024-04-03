class Point(object):
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


class Segment(Point):
    """
    Class of segment
    """

    def __init__(self, point_1, point_2):
        """
        A method for defining an instance using two points from another class
        :param point_1: the tuple with coordinates
        :param point_2: the tuple with coordinates
        """
        self.point_1 = super().__init__(point_1)
        self.point_2 = super().__init__(point_2)
        self.one_intersection = False

    def __str__(self):
        """
        A method that outputs a string with two dots
        :return: string containing information about two points
        """
        return f'The first point is: {self.point_1}. The second point: {self.point_2}.'

    def __repr__(self):
        """
        A method that outputs a string with two dots
        :return: string containing information about two points
        """
        return self.__str__()


class CoordinateSystem(Segment):
    """
    The class of the coordinate system or plane
    """
    segments = []

    def __init__(self, point_1, point_2):
        """
        Method for defining an instance of a list of segments
        :param point_1: the tuple with coordinates
        :param point_2: the tuple with coordinates
        """
        sgmnt = super().__init__(point_1, point_2)
        CoordinateSystem.segments.append(sgmnt)

    @classmethod
    def add_segment(cls, segment):
        """
        The method of adding a segment to a plane
        :param segment: a list with segments
        """
        cls.segments.append(segment)

    @classmethod
    def axis_intersection(cls):
        """
        A method that determines the number of segments intersecting only one ordinate axis
        :return: the number of segments that intersect the plane
        """
        count = 0
        for segment in cls.segments:
            if (segment.point_1.coordinates[0] * segment.point_2.coordinates[0]) < 0 != \
                    (segment.point_1.coordinates[1] * segment.point_2.coordinates[1]) < 0:
                count += 1
                segment.one_intersection = True
        return count

    def __str__(self):
        """
        A method that outputs a string with the number of segments that intersect the plane
        :return: a string containing information about the number of segments that intersect the plane
        """
        return f'The number of segments intersecting one plane: {self.axis_intersection()}'

    def __repr__(self):
        """
        A method that outputs a string with the number of segments that intersect the plane
        :return: a string containing information about the number of segments that intersect the plane
        """
        return self.__str__()
