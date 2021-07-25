from app.concepts import OllState
from app.resources.basic import Positions


class OllStates:
    EVERYTHING_ON_TOP = OllState(
        {
            Positions.FRONT_RIGHT_TOP,
            Positions.FRONT_LEFT_TOP,
            Positions.BACK_LEFT_TOP,
            Positions.BACK_RIGHT_TOP,
        }
    )

    SUPERMAN = OllState(
        {
            Positions.FRONT_RIGHT_FRONT,
            Positions.FRONT_LEFT_FRONT,
            Positions.BACK_LEFT_TOP,
            Positions.BACK_RIGHT_TOP,
        }
    )

    SUPERMAN_AFTER_CLOCKWISE = OllState(
        {
            Positions.FRONT_RIGHT_RIGHT,
            Positions.FRONT_LEFT_TOP,
            Positions.BACK_LEFT_TOP,
            Positions.BACK_RIGHT_RIGHT,
        }
    )

    FISH = OllState(
        {
            Positions.FRONT_RIGHT_FRONT,
            Positions.FRONT_LEFT_TOP,
            Positions.BACK_LEFT_BACK,
            Positions.BACK_RIGHT_RIGHT,
        }
    )

    H = OllState(
        {
            Positions.FRONT_RIGHT_RIGHT,
            Positions.FRONT_LEFT_LEFT,
            Positions.BACK_LEFT_LEFT,
            Positions.BACK_RIGHT_RIGHT,
        }
    )
