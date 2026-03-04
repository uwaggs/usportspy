import pytest
import pandas as pd
from usportspy import (
    fh_get_schedule,
    fh_get_team_box_score,
    fh_get_player_box_score,
    fh_get_pbp,
    UsportspyError
)


def test_fh_get_schedule_mens():
    """Test getting men's field hockey schedule."""
    df = fh_get_schedule(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fh_get_schedule_womens():
    """Test getting women's field hockey schedule."""
    df = fh_get_schedule(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fh_get_schedule_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        fh_get_schedule(gender="invalid")


def test_fh_get_team_box_score():
    """Test getting team box scores."""
    df = fh_get_team_box_score(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fh_get_player_box_score():
    """Test getting player box scores."""
    df = fh_get_player_box_score(gender="w", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fh_get_pbp():
    """Test getting play-by-play data."""
    df = fh_get_pbp(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
