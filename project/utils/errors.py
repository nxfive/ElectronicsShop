class NoSpaceError(Exception):
    """
        Raised when there is no space in the Container
        Attributes:
            item -- added item which caused an error
            message -- description of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ItemNotFoundError(Exception):
    """
        Raised when given item was not found in the Container
        Attributes:
            item -- added item which caused an error
            message -- description of the error
    """

    def __init__(self, item, message):
        self.item = item
        self.message = message
        super().__init__(self.message)


class ChangeContainerSizeError(Exception):
    """
            Raised when you want to increase size of the container to less than
            amount of items in.
            Attributes:
                value -- wanted value which caused an error
                message -- description of the error
        """

    def __init__(self, value, message):
        self.value = value
        self.message = message
        super().__init__(self.message)





