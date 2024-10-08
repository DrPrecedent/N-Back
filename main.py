﻿"""
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

Created on Feb 3, 2012

@author: Erik Bjareholt

Modified 2024 by Rick Solarski
"""

import pygame

try:
    import android
except ImportError:
    android = None

from settings import Settings
from nBack import NBack


def main():
    settings = Settings.Instance()

    if settings.debug:
        pygame.display.init()
        print("Pygame Display Initialized")
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, allowedchanges=pygame.AUDIO_ALLOW_ANY_CHANGE)
        print("Pygame Mixer Audio Initialized")
        pygame.mixer.init()
        print("Pygame Mixer Audio Fully Initialized")
        pygame.joystick.init()
        print("Pygame Joystick Initialized")
        pygame.font.init()
        print("Pygame Fonts Initialized")
    else:
        pygame.init()

    if settings.android:
        settings.android = True
        android.init()
        android.map_key(android.KEYCODE_SEARCH, pygame.K_ESCAPE)

    nback = NBack()
    pygame.display.set_caption('N-Back v' + settings.version)
    nback.run()


if __name__ == "__main__" or __name__ == "main":
    main()
