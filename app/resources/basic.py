from typing import Generator

from app.concepts import (
    DirectionOfMovement,
    EffectOnPosition,
    MannerOfMoving,
    Orientation,
    Piece,
    Place,
    Position,
)


class Places:
    FRONT_RIGHT = Place(0)
    FRONT_LEFT = Place(1)
    BACK_LEFT = Place(2)
    BACK_RIGHT = Place(3)

    @classmethod
    def all(cls) -> Generator[Place, None, None]:
        yield from (cls.FRONT_RIGHT, cls.FRONT_LEFT, cls.BACK_LEFT, cls.BACK_RIGHT)


class Pieces:
    FRONT_RIGHT = Piece(Places.FRONT_RIGHT)
    FRONT_LEFT = Piece(Places.FRONT_LEFT)
    BACK_LEFT = Piece(Places.BACK_LEFT)
    BACK_RIGHT = Piece(Places.BACK_RIGHT)


class Orientations:
    TOP = Orientation("top")
    RIGHT = Orientation("right")
    FRONT = Orientation("front")


class Positions:
    FRONT_RIGHT_TOP = Position(Places.FRONT_RIGHT, Orientations.TOP)
    FRONT_RIGHT_RIGHT = Position(Places.FRONT_RIGHT, Orientations.RIGHT)
    FRONT_RIGHT_FRONT = Position(Places.FRONT_RIGHT, Orientations.FRONT)

    FRONT_LEFT_TOP = Position(Places.FRONT_LEFT, Orientations.TOP)
    FRONT_LEFT_FRONT = Position(Places.FRONT_LEFT, Orientations.RIGHT)
    FRONT_LEFT_LEFT = Position(Places.FRONT_LEFT, Orientations.FRONT)

    BACK_LEFT_TOP = Position(Places.BACK_LEFT, Orientations.TOP)
    BACK_LEFT_LEFT = Position(Places.BACK_LEFT, Orientations.RIGHT)
    BACK_LEFT_BACK = Position(Places.BACK_LEFT, Orientations.FRONT)

    BACK_RIGHT_TOP = Position(Places.BACK_RIGHT, Orientations.TOP)
    BACK_RIGHT_BACK = Position(Places.BACK_RIGHT, Orientations.RIGHT)
    BACK_RIGHT_RIGHT = Position(Places.BACK_RIGHT, Orientations.FRONT)


class MannersOfMoving:
    VERTICAL_AXIS_FLIP = MannerOfMoving(
        {
            Places.FRONT_RIGHT: {
                Orientations.TOP: Orientations.FRONT,
                Orientations.FRONT: Orientations.RIGHT,
                Orientations.RIGHT: Orientations.TOP,
            },
            Places.FRONT_LEFT: {
                Orientations.TOP: Orientations.RIGHT,
                Orientations.RIGHT: Orientations.FRONT,
                Orientations.FRONT: Orientations.TOP,
            },
            Places.BACK_LEFT: {
                Orientations.TOP: Orientations.FRONT,
                Orientations.FRONT: Orientations.RIGHT,
                Orientations.RIGHT: Orientations.TOP,
            },
            Places.BACK_RIGHT: {
                Orientations.TOP: Orientations.RIGHT,
                Orientations.RIGHT: Orientations.FRONT,
                Orientations.FRONT: Orientations.TOP,
            },
        }
    )
    CLOCKWISE_ROTATION = MannerOfMoving(
        {
            place: {
                o: o for o in (Orientations.TOP, Orientations.FRONT, Orientations.RIGHT)
            }
            for place in Places.all()
        }
    )
    ANTICLOCKWISE_ROTATION = MannerOfMoving(
        {
            place: {
                o: o for o in (Orientations.TOP, Orientations.FRONT, Orientations.RIGHT)
            }
            for place in Places.all()
        }
    )


class DirectionsOfMovement:
    CLOCKWISE_ROTATION = DirectionOfMovement(
        {
            Places.FRONT_RIGHT: Places.FRONT_LEFT,
            Places.FRONT_LEFT: Places.BACK_LEFT,
            Places.BACK_LEFT: Places.BACK_RIGHT,
            Places.BACK_RIGHT: Places.FRONT_RIGHT,
        }
    )
    ANTICLOCKWISE_ROTATION = DirectionOfMovement(
        {
            Places.FRONT_RIGHT: Places.BACK_RIGHT,
            Places.BACK_RIGHT: Places.BACK_LEFT,
            Places.BACK_LEFT: Places.FRONT_LEFT,
            Places.FRONT_LEFT: Places.FRONT_RIGHT,
        }
    )
    VERTICAL_AXIS_FLIP = DirectionOfMovement(
        {
            Places.FRONT_RIGHT: Places.FRONT_LEFT,
            Places.FRONT_LEFT: Places.FRONT_RIGHT,
            Places.BACK_LEFT: Places.BACK_RIGHT,
            Places.BACK_RIGHT: Places.BACK_LEFT,
        }
    )
    DOUBLE_TURN = DirectionOfMovement(
        {
            Places.FRONT_RIGHT: Places.BACK_LEFT,
            Places.FRONT_LEFT: Places.BACK_RIGHT,
            Places.BACK_LEFT: Places.FRONT_RIGHT,
            Places.BACK_RIGHT: Places.FRONT_LEFT,
        }
    )
    IDENTITY = DirectionOfMovement({place: place for place in Places.all()})


class EffectsOnPosition:
    VERTICAL_AXIS_FLIP = EffectOnPosition(
        DirectionsOfMovement.VERTICAL_AXIS_FLIP, MannersOfMoving.VERTICAL_AXIS_FLIP
    )
    CLOCKWISE_ROTATION = EffectOnPosition(
        DirectionsOfMovement.CLOCKWISE_ROTATION, MannersOfMoving.CLOCKWISE_ROTATION
    )
    ANTICLOCKWISE_ROTATION = EffectOnPosition(
        DirectionsOfMovement.ANTICLOCKWISE_ROTATION,
        MannersOfMoving.ANTICLOCKWISE_ROTATION,
    )
