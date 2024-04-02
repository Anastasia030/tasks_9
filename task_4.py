class User:
    """
    Class describing user data
    """
    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        """
        The method that defines the instance user data
        :param id: string contains an individual number
        :param nick_name: string contains the name of user
        :param first_name: string contains first name of user
        :param last_name: string contains last name of user by default
        :param middle_name: string contains middle name of user by default
        :param gender: string contains gender of user by default
        """
        self.__id = id
        self.__nick_name = nick_name
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__gender = gender
        if last_name is None:
            self.__last_name = '-'
        if middle_name is None:
            self.__middle_name = '-'
        if gender is None:
            self.__gender = '-'

    def update(self, new_nick=None, new_first_name=None, new_last_name=None):
        """
        Method that updates some attributes of a class
        :param new_nick: string contains a new nickname of user by default
        :param new_first_name: string contains a new first name of user by default
        :param new_last_name: string contains a new last name of user by default
        """
        if new_nick is not None:
            self.__nick_name = new_nick
        if new_first_name is not None:
            self.__first_name = new_first_name
        if new_last_name is not None:
            self.__last_name = new_last_name

    def __str__(self):
        """
        The method outputs a string with all user data
        :return: string with user data
        """
        return f'User unique number: {self.__id}\nAlias: {self.__nick_name}\nName: {self.__first_name} ' \
               f'\nLast name: {self.__last_name}\nMiddle_name: {self.__middle_name}\nGender: {self.__gender}'
