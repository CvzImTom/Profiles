# -- coding: utf-8 --
# Scenery = FSimStudios - BGGH Nuuk

version = "1.1.0"
msfs_mode = 1
icao = "bggh"

apron_a = CustomizedName("Apron A | Stand #§", 1)
apron_b = CustomizedName("Apron B | Stand #§", 2)
apron_c = CustomizedName("Apron C | Stand #§", 3)

@AlternativeStopPositions
def default_stop(aircraftData):
    return Distance.fromMeters(0)

@AlternativeStopPositions
def custom_stops(aircraftData):
    distances = {
        0: 9,
        321: 0,
        330: 0
    }

    return Distance.fromMeters(distances.get(aircraftData.idMajor, 9))

parkings = {
    GATE : {
        None : (),
        "1B" : (apron_b, default_stop),
        "2B" : (apron_b, default_stop),
        "3B" : (apron_b, default_stop),
        "2C" : (apron_c, ),
        1 : (apron_a, custom_stops),
        2 : (apron_a, default_stop),
        3 : (apron_a, default_stop),
        5 : (CustomizedName("Apron A | Stand 5A", 1), default_stop),
        6 : (apron_a, default_stop)
    }
}