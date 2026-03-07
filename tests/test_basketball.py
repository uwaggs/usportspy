import pytest
import pandas as pd
from usportspy import (
    basketball_get_schedule,
    basketball_get_team_box_score,
    basketball_get_player_box_score,
    basketball_get_pbp,
    UsportspyError
)


def test_basketball_get_schedule_mens():
    """Test getting men's basketball schedule."""
    df = basketball_get_schedule(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_basketball_get_schedule_womens():
    """Test getting women's basketball schedule."""
    df = basketball_get_schedule(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_basketball_get_schedule_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        basketball_get_schedule(gender="invalid")


def test_basketball_get_team_box_score():
    """Test getting team box scores for a single season."""
    df = basketball_get_team_box_score(gender="m", seasons=[2023])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_basketball_get_player_box_score():
    """Test getting player box scores for a single season."""
    df = basketball_get_player_box_score(gender="w", seasons=[2023])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_basketball_get_pbp():
    """Test getting play-by-play data for a single season."""
    df = basketball_get_pbp(gender="m", seasons=[2023])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
