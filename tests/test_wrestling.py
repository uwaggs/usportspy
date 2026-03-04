import pytest
import pandas as pd
from usportspy import (
    wrestling_team_rankings,
    wrestling_athlete_rankings,
    UsportspyError
)


def test_wrestling_team_rankings_mens():
    """Test getting men's team rankings."""
    df = wrestling_team_rankings(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_wrestling_team_rankings_womens():
    """Test getting women's team rankings."""
    df = wrestling_team_rankings(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_wrestling_team_rankings_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        wrestling_team_rankings(gender="invalid")


def test_wrestling_athlete_rankings_mens():
    """Test getting men's athlete rankings."""
    df = wrestling_athlete_rankings(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_wrestling_athlete_rankings_womens():
    """Test getting women's athlete rankings."""
    df = wrestling_athlete_rankings(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_wrestling_athlete_rankings_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        wrestling_athlete_rankings(gender="invalid")
