import pytest
import pandas as pd
from usportspy import (
    rugby_get_schedule,
    UsportspyError
)


def test_rugby_get_schedule_womens():
    """Test getting women's rugby schedule."""
    df = rugby_get_schedule(gender="w")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_rugby_get_schedule_mens_raises_error():
    """Test that men's rugby raises error (not available)."""
    with pytest.raises(UsportspyError):
        rugby_get_schedule(gender="m")


def test_rugby_get_schedule_invalid_gender():
    """Test that invalid gender raises error."""
    with pytest.raises(UsportspyError):
        rugby_get_schedule(gender="invalid")
