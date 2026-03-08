import pytest
import pandas as pd
from usportspy import (
    ice_hockey_get_schedule,
    ice_hockey_get_team_box_score,
    ice_hockey_get_player_box_score,
    ice_hockey_get_pbp,
    UsportspyError
)


def test_ice_hockey_get_schedule_mens():
    """Test getting men's ice hockey schedule."""
    df = ice_hockey_get_schedule(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_ice_hockey_get_schedule_womens():
    """Test getting women's ice hockey schedule."""
    df = ice_hockey_get_schedule(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_ice_hockey_get_schedule_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        ice_hockey_get_schedule(gender="invalid")


# NOTE: team box scores are currently unavailable
# def test_ice_hockey_get_team_box_score():
#     """Test getting team box scores."""
#     df = ice_hockey_get_team_box_score(gender="m", seasons=[2023])
#     assert isinstance(df, pd.DataFrame)
#     assert len(df) > 0


def test_ice_hockey_get_pbp():
    """Test getting play-by-play data."""
    df = ice_hockey_get_pbp(gender="m", seasons=[2023])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
