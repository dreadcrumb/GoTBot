import urllib
import json

from urllib import urlopen

def get_distance(point_a,point_b,vehicle=None):


    if vehicle is None:
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&language=en&destinations=%s"%(point_a,point_b)
    else:
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&language=en&destinations=%s&mode=%s"%(point_a,point_b,vehicle)

    maps_json = get_json(url,vehicle)

    return form_response(maps_json)



def get_json(url,vehicle):
    u = urllib.urlopen(url).read()
    response = json.loads(u)
    values = response["rows"][0]["elements"][0]
    result = {
        "start": response["origin_addresses"][0],
        "end": response["destination_addresses"][0],
        "distance": values["distance"]["value"]#distance is metres
    }
    if (vehicle != None) and (vehicle != ""):
        result["vehicle"] = vehicle
        #duration in seconds
        result["duration"] = values["duration"]["value"]

    return result


def form_response(maps_json):
    print maps_json
    start = maps_json["start"]
    end = maps_json["end"]
    distance = maps_json["distance"] / 1000.0

    vehicle = maps_json.get("vehicle", None)
    duration = maps_json.get("duration", None)

    text = "The distance from %s to %s is %skm."%(start, end, distance)

    if vehicle != None:
        duration = duration / 60 / 60
        text += " To get there by %s you need %.2f hours"%(vehicle, duration)


    resp = {
        "speech": text,
        "displayText": text,
        "source": "webhook test"
    }
    resp = json.dumps(resp, indent=4)

    return resp
