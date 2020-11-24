## IP Address/User info provider flask api.

this is python flask application that provide information about an ip address or user information through there ip address.

# Run in Test mode(cmd)

You can test this in command mode too.

RUN the following command to run in test mode.

```
$ python app.py -cmd
    OR
$ python app.py -cmd -ip 8.8.8.8

```

# Run flask app (web)

this run in web and return `application/json` data as web api.

To run flask app run the following commands.

### On windows(cmd)

`c:\projects>set FLASK_APP=app.py`

### linux, macOS(bash, zsh)

`$ export FLASK_APP=app.py`

Now run final command to start webserver for the application.

```
$ flask run
```

# Response Data

```
{
    "ip": "8.8.8.8",
    "hostname": "dns.google",
    "city": "Mountain View",
    "region": "California",
    "country": "US",
    "loc": "37.4056,-122.0775",
    "org": "AS15169 Google LLC",
    "postal": "94043",
    "timezone": "America/Los_Angeles",
    "readme": "https://ipinfo.io/missingauth",
    "coord": {
        "lon": 139,
        "lat": 35
    },
    "weather": [
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 28.23,
        "pressure": 1011,
        "humidity": 74,
        "temp_min": 26,
        "temp_max": 31
    },
    "visibility": 10000,
    "wind": {
        "speed": 3.6,
        "deg": 230
    },
    "clouds": {
        "all": 75
    },
    "dt": 1499396400,
    "sys": {
        "type": 1,
        "id": 7616,
        "message": 0.0043,
        "country": "JP",
        "sunrise": 1499369792,
        "sunset": 1499421666
    },
    "id": 1851632,
    "name": "Shuzenji",
    "cod": 200
}
```
