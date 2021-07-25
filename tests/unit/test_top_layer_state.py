from app.resources.oll_states import OllStates
from app.resources.top_layer_states import TopLayerStates


def test_can_consider_only_oll() -> None:
    assert (
        TopLayerStates.FISH_WITH_EVERYTHING_IN_RIGHT_PLACE.only_considering_oll()
        == OllStates.FISH
    )
