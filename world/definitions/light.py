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
from utils.enum import AutoNumberEnum


class AmbientLightLevel(AutoNumberEnum):
    """
    This light scale is intended to describe the light level of a room or area.
    It can be used to help with DC rolls for searching, hiding, etc.
    """
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    PitchBlack = "Pitch Black"
    Poor = "Poorly Lit"
    Dim = "Dimly Lit"
    Well = "Well Lit"
    Daylight = "Daylight"
    Blinding = "Blindingly Bright"


"""
This mapping is a threshold step mapping - values under the given cutoff
values apply, until they reach the next level.

Example: -10 is still Pitch Black, 1 or 2 is still Poor.
"""
LightMap = {
   AmbientLightLevel.PitchBlack:  0,
   AmbientLightLevel.Poor:  30,
   AmbientLightLevel.Dim:  70,
   AmbientLightLevel.Well:  250,
   AmbientLightLevel.Daylight: 1000,
   AmbientLightLevel.Blinding: 2000
}


class LightGenerationType(AutoNumberEnum):
    """
    This light scale is intended for light sources, not sinks.
    Effects that negatively drain light are created auras, not needing this
    table.

    Direct light aids the user of the light source more than others in the
    room, but it is also weaker in light quality since it needs to be pointed
    at sources to be useful.

    Ambient light aids everyone equally.  More powerful light tends to be
    magical, in nature (and therefore created auras, since it is an effect).

    Light sources are not be strictly additive, so 1 lantern might give a light
    value of 40, but two lanterns is not 80, and ten lanterns is certainly not
    400.
    """
    def __init__(self, quality='unknown'):
        self.quality = quality

    WeakDirectLight = ["weak directed light", 10]
    AverageDirectLight = ["average direct light", 40]
    StrongDirectLight = ["strong direct light", 80]
    PowerfulDirectLight = ["powerful direct light", 100]

    WeakAmbientLight = ["weak ambient light", 20]
    AverageAmbientLight = ["average ambient light", 50]
    StrongAmbientLight = ["strong ambient light", 100]
    PowerfulAmbientLight = ["powerful ambient light", 120]
