from app.concepts import OllAlgorithm
from app.resources.basic import EffectsOnPosition, Places

clockwise_rotation = OllAlgorithm(
    {
        Places.FRONT_RIGHT: EffectsOnPosition.CLOCKWISE_ROTATION,
        Places.FRONT_LEFT: EffectsOnPosition.CLOCKWISE_ROTATION,
        Places.BACK_LEFT: EffectsOnPosition.CLOCKWISE_ROTATION,
        Places.BACK_RIGHT: EffectsOnPosition.CLOCKWISE_ROTATION,
    }
)

l_algorithm = OllAlgorithm(
    {
        Places.FRONT_RIGHT: EffectsOnPosition.CLOCKWISE_ROTATION,
        Places.FRONT_LEFT: EffectsOnPosition.VERTICAL_AXIS_FLIP,
        Places.BACK_LEFT: EffectsOnPosition.VERTICAL_AXIS_FLIP,
        Places.BACK_RIGHT: EffectsOnPosition.ANTICLOCKWISE_ROTATION,
    }
)

anticlockwise_rotation = OllAlgorithm(
    {
        Places.FRONT_RIGHT: EffectsOnPosition.ANTICLOCKWISE_ROTATION,
        Places.FRONT_LEFT: EffectsOnPosition.ANTICLOCKWISE_ROTATION,
        Places.BACK_LEFT: EffectsOnPosition.ANTICLOCKWISE_ROTATION,
        Places.BACK_RIGHT: EffectsOnPosition.ANTICLOCKWISE_ROTATION,
    }
)
