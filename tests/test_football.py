import pytest
import pandas as pd
from usportspy import (
    fb_get_schedule,
    fb_get_offence,
    fb_get_defence,
    fb_get_kicking,
    fb_get_returns,
    fb_get_pbp,
    fb_get_scoring_summaries,
    UsportspyError
)


def test_fb_get_schedule():
    """Test getting football schedule (men's only)."""
    df = fb_get_schedule(gender="m")
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fb_get_schedule_womens_raises_error():
    """Test that women's football raises error (not available)."""
    with pytest.raises(UsportspyError):
        fb_get_schedule(gender="w")


def test_fb_get_offence():
    """Test getting offensive statistics."""
    df = fb_get_offence(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fb_get_defence():
    """Test getting defensive statistics."""
    df = fb_get_defence(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fb_get_kicking():
    """Test getting kicking statistics."""
    df = fb_get_kicking(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fb_get_returns():
    """Test getting return statistics."""
    df = fb_get_returns(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fb_get_pbp():
    """Test getting play-by-play data."""
    df = fb_get_pbp(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_fb_get_scoring_summaries():
    """Test getting scoring summaries."""
    df = fb_get_scoring_summaries(gender="m", seasons=[2024])
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
