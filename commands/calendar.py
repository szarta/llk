"""
MIT License

Copyright (c) 2021 Brandon Arrendondo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from evennia import Command
import evennia.contrib.custom_gametime as mudtime


from utils.enum import AutoNumberEnum


class AmtalMonth(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Deepwinter = "Deepwinter"
    ClawOfWinter = "Claw of Winter"
    ClawOfSun = "Claw of Sun"
    ClawOfStorms = "Claw of Storms"
    TheMelting = "The Melting"
    TimeOfGrowth = "Time of Growth"
    TheKingsShield = "The King's Shield"
    Summertide = "Summertide"
    Highsun = "Highsun"
    TheFading = "The Fading"
    Leaffall = "Leaffall"
    TheRotting = "The Rotting"
    DrawingDown = "Drawingdown"


def get_day_of_month(day_of_year):
    day = day_of_year

    m = AmtalMonth.DrawingDown
    d = 1

    if day < 31:
        d = day
        m = AmtalMonth.Deepwinter
    elif day < 61:
        d = day - 30
        m = AmtalMonth.ClawOfWinter
    elif day < 91:
        d = day - 60
        m = AmtalMonth.ClawOfSun
    elif day < 121:
        d = day - 90
        m = AmtalMonth.ClawOfStorms
    elif day < 151:
        d = day - 120
        m = AmtalMonth.TheMelting
    elif day < 181:
        d = day - 150
        m = AmtalMonth.TimeOfGrowth
    elif day < 191:
        d = day - 180
        m = AmtalMonth.TheKingsShield
    elif day < 221:
        d = day - 190
        m = AmtalMonth.Summertide
    elif day < 251:
        d = day - 220
        m = AmtalMonth.Highsun
    elif day < 281:
        d = day - 250
        m = AmtalMonth.TheFading
    elif day < 311:
        d = day - 280
        m = AmtalMonth.Leaffall
    elif day < 341:
        d = day - 310
        m = AmtalMonth.TheRotting
    else:
        d = day - 340
        m = AmtalMonth.DrawingDown

    return (d, m)


class CmdTime(Command):
    """
    get the current time

    Usage:
      time

    Shows your inventory.
    """
    key = "time"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        time_str = "Amtal Standard Date: "
        t = mudtime.custom_gametime(absolute=True)
        (year, day, week, hour, minute, second) = t
        (month_day, month) = get_day_of_month(day)

        time_str += "{0!s} {1}, {2!s}".format(
            month_day, month.display_name, year
        )

        time_str += "\nCurrent time: {0!s}:{1!s}".format(
            hour, minute
        )

        caller.msg(time_str)
