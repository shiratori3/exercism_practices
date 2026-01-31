class SpaceAge:
    second_earth = 31557600
    factor = {
        "mercury": 0.2408467,
        "venus":   0.61519726,
        "earth":   1.0,
        "mars":    1.8808158,
        "jupiter": 11.862615,
        "saturn":  29.447498,
        "uranus":  84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds):
        self.age_earth = seconds / SpaceAge.second_earth
        print()

    def on_earth(self):
        return round(self.age_earth / SpaceAge.factor["earth"], 2)

    def on_mercury(self):
        return round(self.age_earth / SpaceAge.factor["mercury"], 2)

    def on_venus(self):
        return round(self.age_earth / SpaceAge.factor["venus"], 2)

    def on_mars(self):
        return round(self.age_earth / SpaceAge.factor["mars"], 2)

    def on_jupiter(self):
        return round(self.age_earth / SpaceAge.factor["jupiter"], 2)

    def on_saturn(self):
        return round(self.age_earth / SpaceAge.factor["saturn"], 2)

    def on_uranus(self):
        return round(self.age_earth / SpaceAge.factor["uranus"], 2)

    def on_neptune(self):
        return round(self.age_earth / SpaceAge.factor["neptune"], 2)
