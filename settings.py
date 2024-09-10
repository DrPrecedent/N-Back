from singleton import Singleton

__author__ = 'erb'

@Singleton
class Settings():
    version = "0.3.1"

    # The N in N-Back
    nBack = 2

    # Probability that one of the last N slides will be next
    repeatProbability = 0.75

    # Time given to answer each slide, the correct answer is shown afterwards at a fraction of the time
    slideTime = 1000

    # How many slides to show during one game
    numOfSlides = 20

    # Window settings
    windowSize = (600, 600)
    # Kind of quirky, messes up resolution settings in my dev env.
    fullscreen = False

    drawNumber = True

    # Set to true to skip menu
    standalone = False

    # Unsupported
    android = False

    debug = True

    # Start Screen and Game Over Screen
    start_screen = True
    game_over_screen = True

    def __init__(self):
        print("Settings loaded")