W.I.L.O.S. CLI
=====
What's It Like Out Side? - A weather tool for all the coders living in dark caves.

Install
=====


##### Note:
Currently supports Linux, Mac OS X, NetBSD and FreeBSD.

You'll need a *free* API key from [developer.forecast.io](http://developer.forecast.io/).

Set your forecast.io API key in an environment variable `WILOS_CLI_FORECAST_API_TOKEN`

For example:

```bash
export WILOS_CLI_FORECAST_API_TOKEN="<YOUR_API_TOKEN>"
```

If you want to use the `--loc` flag and conveniently search by a location string you'll need a Google Maps API key.

Which you can get by clicking on the *Get A Key* button on this [page](https://developers.google.com/maps/web-services/).

Set your Google Maps API key in an environment variable `WILOS_CLI_GOOGLE_API_TOKEN`

For example:

```bash
export WILOS_CLI_GOOGLE_API_TOKEN="<YOUR_API_TOKEN>"
```

### Install via `pip`
```bash
$ pip install wilos-cli
```

### Build from source

```bash
$ git clone git@github.com:aslan11/wilos-cli.git
$ cd wilos-cli
$ python setup.py install
```

You can set the API key using an environment variable as shown above or create a file `config.py` in the wilos package directory (`wilos/config.py`) with a few lines

```python
config = {
    "WILOS_CLI_FORECAST_API_TOKEN": "<YOUR_FORECAST_API_TOKEN>",
    "WILOS_CLI_GOOGLE_API_TOKEN": "<YOUR_GOOGLE_API_TOKEN>",
}
```

Usage
====

### Get Weather for a latitude and longitude (Requires Forecast.io Key)

```bash
$ wilos --lat=19.8968 --lon=155.5828 # weather for Hawaii
```

### Get Weather for a location (Requires Forecast.io and Google Key)
```bash
$ wilos --loc='Los Angeles' # weather for LA
"======== What's it like outside Los Angeles, CA, USA? ========"

   ________                    \  |  /
  / ____/ /__  ____ ______       .-.
 / /   / / _ \/ __ `/ ___/    ‒ (   ) ‒
/ /___/ /  __/ /_/ / /           `-᾿
\____/_/\___/\__,_/_/          /  |  \

```

### Help
```bash
$ wilos --help
```

License
====
Open sourced under [MIT License](LICENSE)

Support
====
If you like my work and you're in LA, let's grab a beer and talk tech.
Feel free to open up PR's with features, I'll be adding more when I find time to.
