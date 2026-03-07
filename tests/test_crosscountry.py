import pytest
import pandas as pd
from usportspy import (
    xc_team_rankings,
    xc_rosters,
    xc_meet_results,
    xc_universities,
    UsportspyError
)


def test_xc_team_rankings_mens():
    """Test getting men's team rankings."""
    df = xc_team_rankings(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_xc_team_rankings_womens():
    """Test getting women's team rankings."""
    df = xc_team_rankings(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_xc_team_rankings_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        xc_team_rankings(gender="invalid")


def test_xc_rosters_mens():
    """Test getting men's rosters."""
    df = xc_rosters(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_xc_rosters_womens():
    """Test getting women's rosters."""
    df = xc_rosters(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_xc_meet_results():
    """Test getting meet results."""
    df = xc_meet_results()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_xc_universities():
    """Test getting universities list."""
    df = xc_universities()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
