from app.concepts import concatenate
from app.resources.algorithms import (
    anticlockwise_rotation,
    clockwise_rotation,
    headlights_at_back,
    l_algorithm,
)
from app.resources.top_layer_states import TopLayerStates


def test_clockwise_rotation() -> None:
    assert (
        clockwise_rotation.result(TopLayerStates.SOLVED)
        == TopLayerStates.EVERYTHING_SOLVED_BUT_TURNED_CLOCKWISE
    )


def test_if_we_do_clockwise_and_then_anticlockwise_we_have_done_nothing() -> None:
    initial_state = TopLayerStates.SOLVED
    final_state = anticlockwise_rotation.result(
        clockwise_rotation.result(initial_state)
    )
    assert initial_state == final_state


def test_if_we_do_anticlockwise_and_then_clockwise_we_have_done_nothing() -> None:
    initial_state = TopLayerStates.SOLVED
    final_state = clockwise_rotation.result(
        anticlockwise_rotation.result(initial_state)
    )
    assert initial_state == final_state


def test_if_we_do_clockwise_four_times_we_have_done_nothing() -> None:
    initial_state = TopLayerStates.SOLVED
    final_state = concatenate(*([clockwise_rotation] * 4))(initial_state)
    assert initial_state == final_state


def test_if_we_do_clockwise_three_times_it_is_like_doing_anti_clockwise() -> None:
    initial_state = TopLayerStates.SOLVED
    after_three_clockwise = concatenate(
        clockwise_rotation, clockwise_rotation, clockwise_rotation
    )(initial_state)
    after_one_anticlockwise = anticlockwise_rotation.result(initial_state)
    assert after_three_clockwise == after_one_anticlockwise


def test_l_algorithm() -> None:
    initial_state = TopLayerStates.SUPERMAN_AFTER_ANTI_WITH_HORIZONTAL_SWAPSIES
    final_state = l_algorithm.result(initial_state)
    assert final_state == TopLayerStates.SOLVED


def test_if_we_do_the_l_algorithm_six_times_we_have_done_nothing() -> None:
    initial_state = TopLayerStates.SOLVED
    final_state = concatenate(*([l_algorithm] * 6))(initial_state)
    assert initial_state == final_state


def test_headlights_at_back() -> None:
    initial_state = TopLayerStates.HEADLIGHTS_AT_BACK
    final_state = headlights_at_back.result(initial_state)
    assert final_state == TopLayerStates.SOLVED
