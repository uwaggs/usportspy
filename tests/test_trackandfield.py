import pytest
import pandas as pd
from usportspy import (
    tnf_athlete_rankings,
    tnf_team_rankings,
    tnf_rosters,
    tnf_meet_results,
    tnf_universities,
    UsportspyError
)


def test_tnf_athlete_rankings_mens():
    """Test getting men's athlete rankings."""
    df = tnf_athlete_rankings(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_tnf_athlete_rankings_womens():
    """Test getting women's athlete rankings."""
    df = tnf_athlete_rankings(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_tnf_athlete_rankings_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        tnf_athlete_rankings(gender="invalid")


def test_tnf_team_rankings_mens():
    """Test getting men's team rankings."""
    df = tnf_team_rankings(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_tnf_team_rankings_womens():
    """Test getting women's team rankings."""
    df = tnf_team_rankings(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_tnf_rosters_mens():
    """Test getting men's rosters."""
    df = tnf_rosters(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_tnf_rosters_womens():
    """Test getting women's rosters."""
    df = tnf_rosters(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_tnf_meet_results():
    """Test getting meet results."""
    df = tnf_meet_results()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_tnf_universities():
    """Test getting universities list."""
    df = tnf_universities()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
