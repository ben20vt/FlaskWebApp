def my_LatLong(Address, CrossStreets):
    address = str(Address + " & " + CrossStreets)
    n = ArcGIS().geocode(address)
    # n is a list [0] = street names [1] = lat/long
    return n[1]

