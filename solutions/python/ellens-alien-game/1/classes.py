"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.health = 3
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1

    def is_alive(self):
        return self.health > 0

    def hit(self):
        if self.is_alive():
            self.health -= 1

    def teleport(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object: any):
        pass


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_pos: list[tuple]) -> list[Alien]:
    """
    Docstring for new_aliens_collection
    
    :param alien_pos: list of tuple describe the postions of Alien
    :type alien_pos: list[tuple]
    :return: return a list of Alien with input pos
    :rtype: list[Alien]
    """

    return [Alien(pos[0], pos[1]) for pos in alien_pos]
