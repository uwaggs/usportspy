import pytest
import pandas as pd
from usportspy import (
    volleyball_get_schedule,
    volleyball_get_team_box_score,
    volleyball_get_player_box_score,
    volleyball_get_pbp,
    UsportspyError
)


def test_volleyball_get_schedule_mens():
    """Test getting men's volleyball schedule."""
    df = volleyball_get_schedule(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_volleyball_get_schedule_womens():
    """Test getting women's volleyball schedule."""
    df = volleyball_get_schedule(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_volleyball_get_schedule_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        volleyball_get_schedule(gender="invalid")


def test_volleyball_get_team_box_score():
    """Test getting team box scores."""
    df = volleyball_get_team_box_score(gender="m", seasons=[2023])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_volleyball_get_player_box_score():
    """Test getting player box scores."""
    df = volleyball_get_player_box_score(gender="w", seasons=[2023])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_volleyball_get_pbp():
    """Test getting play-by-play data."""
    df = volleyball_get_pbp(gender="m", seasons=[2023])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
