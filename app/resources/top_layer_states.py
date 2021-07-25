from app.concepts import TopLayerState
from app.resources.basic import Pieces, Positions


class TopLayerStates:
    SOLVED = TopLayerState(
        {
            Pieces.FRONT_RIGHT: Positions.FRONT_RIGHT_TOP,
            Pieces.FRONT_LEFT: Positions.FRONT_LEFT_TOP,
            Pieces.BACK_LEFT: Positions.BACK_LEFT_TOP,
            Pieces.BACK_RIGHT: Positions.BACK_RIGHT_TOP,
        }
    )

    FISH_WITH_EVERYTHING_IN_RIGHT_PLACE = TopLayerState(
        {
            Pieces.FRONT_RIGHT: Positions.FRONT_RIGHT_FRONT,
            Pieces.FRONT_LEFT: Positions.FRONT_LEFT_TOP,
            Pieces.BACK_LEFT: Positions.BACK_LEFT_BACK,
            Pieces.BACK_RIGHT: Positions.BACK_RIGHT_RIGHT,
        }
    )

    EVERYTHING_SOLVED_BUT_TURNED_CLOCKWISE = TopLayerState(
        {
            Pieces.FRONT_RIGHT: Positions.FRONT_LEFT_TOP,
            Pieces.FRONT_LEFT: Positions.BACK_LEFT_TOP,
            Pieces.BACK_LEFT: Positions.BACK_RIGHT_TOP,
            Pieces.BACK_RIGHT: Positions.FRONT_RIGHT_TOP,
        }
    )

    SUPERMAN_AFTER_ANTI_WITH_HORIZONTAL_SWAPSIES = TopLayerState(
        {
            Pieces.FRONT_RIGHT: Positions.FRONT_LEFT_LEFT,
            Pieces.FRONT_LEFT: Positions.FRONT_RIGHT_TOP,
            Pieces.BACK_LEFT: Positions.BACK_RIGHT_TOP,
            Pieces.BACK_RIGHT: Positions.BACK_LEFT_LEFT,
        }
    )
