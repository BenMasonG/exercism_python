"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1


    def hit(self):
        '''
        This function decreased the Alien's health by one point when it is called.
        '''
        if self.health > 0:
            self.health -= 1
            return self.health
        return self.health

    def is_alive(self):
        '''
        This method checks to see if the alien is alive.
        '''
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        '''
        This method teleports the Alien.
        '''
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        return self.x_coordinate, self.y_coordinate

    def collision_detection (self, other_object):
        '''
        This method will detect if the Alien has collided with another alien.
        '''
        pass


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.


def new_aliens_collection(aliens):
    '''
    This creates a list of Aliens when given a list of positions, as tuples.

    :param aliens: list - a list of tuples containing the x and y coordinates for a
    collection of aliens.
    :return: list - a list of Aliens with the given coordinates.

    This function creates a list of Aliens when given a list of positions.
    '''
    aliens_collection = []
    for alien in aliens:
        aliens_collection.append(Alien(alien[0], alien[1]))

    return aliens_collection
