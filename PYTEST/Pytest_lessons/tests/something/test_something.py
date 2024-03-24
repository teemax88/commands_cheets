import pytest
from src.generators.player_localization import PlayerLocalization
from src.generators.player import Player

from src.enums.user_enums import Statuses


@pytest.mark.parametrize("status", Statuses.list())
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


# @pytest.mark.parametrize("delete_key", [
#     "account_status",
#     "balance",
#     "localize",
#     "avatar"
# ])
# def test_something2(delete_key, get_player_generator):
#     object_to_send = get_player_generator.build()
#     del object_to_send[delete_key]
#     print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR"),
    ("it", "it_IT"),
    ("jp", "ja_JP")
])
def test_something3(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(['localize', localizations],
                                                             PlayerLocalization(loc).build()).build()
    print(object_to_send)
