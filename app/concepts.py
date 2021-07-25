from dataclasses import dataclass
from typing import Callable, Dict, Generator, Set, Tuple


@dataclass(frozen=True)
class Orientation:
    orientation: str


@dataclass(frozen=True)
class Place:
    place: int


@dataclass(frozen=True)
class Piece:
    home_position: Place


@dataclass(frozen=True)
class Position:
    place: Place
    orientation: Orientation


@dataclass
class MannerOfMoving:
    effects_for_all_places_and_orientations: Dict[Place, Dict[Orientation, Orientation]]

    def final_orientation(self, initial_position: Position) -> Orientation:
        return self.effects_for_all_places_and_orientations[initial_position.place][
            initial_position.orientation
        ]


@dataclass
class DirectionOfMovement:
    effects_for_all_places: Dict[Place, Place]

    def final_place(self, initial_place: Place) -> Place:
        return self.effects_for_all_places[initial_place]


@dataclass
class EffectOnPosition:
    direction_of_movement: DirectionOfMovement
    manner_of_moving: MannerOfMoving

    def final_position(self, initial_position: Position) -> Position:
        return Position(
            self.direction_of_movement.final_place(initial_position.place),
            self.manner_of_moving.final_orientation(initial_position),
        )


@dataclass
class OllState:
    positions: Set[Position]

    def __iter__(self) -> Generator[Position, None, None]:
        yield from self.positions


@dataclass
class TopLayerState:
    piece_positions: Dict[Piece, Position]

    def __iter__(self) -> Generator[Tuple[Piece, Position], None, None]:
        yield from self.piece_positions.items()

    def only_considering_oll(self) -> OllState:
        return OllState({position for _, position in self})


class Algorithm:
    def result(self, state: TopLayerState) -> TopLayerState:
        pass


@dataclass
class OllAlgorithm(Algorithm):
    effects: Dict[Place, EffectOnPosition]

    def result(self, state: TopLayerState) -> TopLayerState:
        return TopLayerState(
            {
                piece: self.effects[position.place].final_position(position)
                for piece, position in state
            }
        )


@dataclass
class PllAlgorithm(Algorithm):
    effects: Dict[Place, DirectionOfMovement]

    def result(self, state: TopLayerState) -> TopLayerState:
        return TopLayerState(
            {
                piece: Position(
                    self.effects[position.place].final_place(position.place),
                    position.orientation,
                )
                for piece, position in state
            }
        )


def concatenate(*algorithms: Algorithm) -> Callable:
    def result(initial_state: TopLayerState) -> TopLayerState:
        running_result = initial_state
        for algorithm in algorithms:
            running_result = algorithm.result(running_result)
        return running_result

    return result
