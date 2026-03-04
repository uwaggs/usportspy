import pandas as pd
from usportspy import (
    swimming_team_rankings,
    swimming_athlete_rankings
)


def test_swimming_team_rankings():
    """Test getting swimming team rankings."""
    df = swimming_team_rankings()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_swimming_athlete_rankings():
    """Test getting swimming athlete rankings."""
    df = swimming_athlete_rankings()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
