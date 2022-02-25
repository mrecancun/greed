import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.casting.score import Score


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600 # window size
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40
twoArtifacts=[42,111]

def main():
    
    # create the cast
    cast = Cast()
    
    # create the score_keeper
    score = Score()
    score.set_text("SCORE: 0") # crear score score keeping. This line leaves the score text empty.
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("scores", score)
    score_text=score._text
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y  -25)
    position = Point(x, y) #ubicacion cambiar abajo de la pantalla

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    # with open(DATA_PATH) as file:
        # data = file.read()
        # messages

    for n in range(DEFAULT_ARTIFACTS):
        ind=random.randint(0, 1)
        text = chr(twoArtifacts[ind])
        # message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)

        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(score_text) Capaz se puede crear una funcion para añadir a score
        artifact.set_velocity(Point(0,5))
        cast.add_actor("artifacts", artifact)
        
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()