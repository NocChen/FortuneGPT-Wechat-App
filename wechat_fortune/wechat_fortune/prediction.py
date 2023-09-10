from astropy.coordinates import get_sun, EarthLocation, AltAz
from astropy.time import Time
from astropy import units as u

class Prediction:
    def __init__(self, date: str, prediction: str = None):
        self.date = date
        self.prediction = prediction if prediction else self.generate_prediction()

    def generate_prediction(self) -> str:
        """
        Generate a fortune prediction based on the position of the sun on a given date.
        The prediction is a simple string message that changes based on whether the sun is above or below the horizon.
        """
        time = Time(self.date)
        location = EarthLocation(lat=0*u.deg, lon=0*u.deg, height=0*u.m)
        altaz = AltAz(obstime=time, location=location)
        sun = get_sun(time)
        sun_altaz = sun.transform_to(altaz)

        if sun_altaz.alt > 0:
            return "The sun is above the horizon. Today is a good day for new beginnings."
        else:
            return "The sun is below the horizon. Today is a good day for reflection and planning."

    def get_prediction(self) -> str:
        return self.prediction
