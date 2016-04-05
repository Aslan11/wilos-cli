import click
import csv
import datetime
import json
import io

from abc import ABCMeta, abstractmethod
from itertools import groupby
from collections import namedtuple


def get_writer(output_format='stdout', output_file=None):
    return globals()[output_format.capitalize()](output_file)


class BaseWriter(object):

    __metaclass__ = ABCMeta

    def __init__(self, output_file):
        self.output_filename = output_file

    @abstractmethod
    def live_weather(self, live_weather):
        pass


class Stdout(BaseWriter):

    def __init__(self, output_file):
        self.Result = namedtuple("Result",
                                 "summary, temp, precipChange, humidity")

        enums = dict(
            RED="red",
            BLUE="blue",
            YELLOW="yellow",
            GREEN="green",
            WHITE="white",
        )
        self.colors = type('Enum', (), enums)

    def live_weather(self, live_weather):
        """Prints the live weather in a pretty format"""
        summary = live_weather['currently']['summary']
        self.summary(summary)
        click.echo()

    def title(self, title):
        "Prints the title"
        title = " What's it like outside {0}? ".format(title)
        click.secho("{:=^62}".format(title), fg=self.colors.WHITE)
        click.echo()

    def summary(self, summary):
        """Prints the ASCII Icon"""
        if summary is not None:
            if summary == 'Clear':
                click.secho("""

   ________                    \  |  /
  / ____/ /__  ____ ______       .-.
 / /   / / _ \/ __ `/ ___/    ‒ (   ) ‒
/ /___/ /  __/ /_/ / /           `-᾿
\____/_/\___/\__,_/_/          /  |  \\

                """, fg=self.colors.YELLOW)
                click.echo()

            elif summary == 'Partly Cloudy':
                click.secho("""

    ____             __  __         ________                __
   / __ \____ ______/ /_/ /_  __   / ____/ /___  __  ______/ /_  __    \  |  /
  / /_/ / __ `/ ___/ __/ / / / /  / /   / / __ \/ / / / __  / / / /      .-.
 / ____/ /_/ / /  / /_/ / /_/ /  / /___/ / /_/ / /_/ / /_/ / /_/ /    ‒ (  .-.
/_/    \__,_/_/   \__/_/\__, /   \____/_/\____/\__,_/\__,_/\__, /        `(   ).
                       /____/                             /____/       / (___(__)

                """, fg=self.colors.WHITE)

            elif summary == 'Flurries':
                click.secho("""

    ________                _                  .--.
   / ____/ /_  ____________(_)__  _____     .-(    ).
  / /_  / / / / / ___/ ___/ / _ \/ ___/    (___.__)__)
 / __/ / / /_/ / /  / /  / /  __(__  )      *      *
/_/   /_/\__,_/_/  /_/  /_/\___/____/          *

                """, fg=self.colors.BLUE)
                click.echo()

            elif summary == 'Overcast' or summary == 'Mostly Cloudy':
                click.secho("""

   ____                                  __
  / __ \_   _____  ______________ ______/ /_       .--.
 / / / / | / / _ \/ ___/ ___/ __ `/ ___/ __/     .(    ).-.
/ /_/ /| |/ /  __/ /  / /__/ /_/ (__  ) /_      (___.__(   ).
\____/ |___/\___/_/   \___/\__,_/____/\__/            (___(__)

                """, fg=self.colors.WHITE)
                click.echo()

            elif summary == 'Snow':
                click.secho("""

   _____                            .--.
  / ___/____  ____ _      __     .-(    ).
  \__ \/ __ \/ __ \ | /| / /    (___.__)__)
 ___/ / / / / /_/ / |/ |/ /      *   *   *
/____/_/ /_/\____/|__/|__/         *   *

                """, fg=self.colors.BLUE)
                click.echo()

            elif summary == 'Light Rain' or summary == 'Drizzle':
                click.secho("""

    __    _       __    __     ____        _
   / /   (_)___ _/ /_  / /_   / __ \____ _(_)___       .--.
  / /   / / __ `/ __ \/ __/  / /_/ / __ `/ / __ \   .-(    ).
 / /___/ / /_/ / / / / /_   / _, _/ /_/ / / / / /  (___.__)__)
/_____/_/\__, /_/ /_/\__/  /_/ |_|\__,_/_/_/ /_/     /  /  /
        /____/

                """, fg=self.colors.BLUE)

            elif summary == 'Rain':
                click.secho("""

    ____        _
   / __ \____ _(_)___       .--.
  / /_/ / __ `/ / __ \   .-(    ).
 / _, _/ /_/ / / / / /  (___.__)__)
/_/ |_|\__,_/_/_/ /_/     /  /  /

                """, fg=self.colors.BLUE)

            else:
                click.secho("{:=^62}".format(str(summary)), fg=self.colors.GREEN)
