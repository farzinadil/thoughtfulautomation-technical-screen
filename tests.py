import pytest
from sort import sort

def test_volume_calculations():
    """Test cases for volume calculations"""
    assert sort(100, 100, 100, 10) == "SPECIAL"    # Volume = 1,000,000 
    assert sort(99, 99, 99, 10) == "STANDARD"      # Volume < 1,000,000
    assert sort(101, 100, 100, 10) == "SPECIAL"    # Volume > 1,000,000

def test_dimensions():
    """Test cases for dimension limits"""
    assert sort(150, 10, 10, 10) == "SPECIAL"      # Width at limit
    assert sort(10, 150, 10, 10) == "SPECIAL"      # Height at limit
    assert sort(10, 10, 150, 10) == "SPECIAL"      # Length at limit
    assert sort(25, 25, 25, 10) == "STANDARD"   # All under limits

def test_mass():
    """Test cases for mass limits"""
    assert sort(10, 10, 10, 20) == "SPECIAL"       # Mass at limit
    assert sort(10, 10, 10, 19) == "STANDARD"      # Mass under limit
    assert sort(10, 10, 10, 21) == "SPECIAL"       # Mass over limit

def test_rejected_combinations():
    """Test cases for rejected packages"""
    # Both bulky and heavy
    assert sort(150, 10, 10, 20) == "REJECTED"     # Size limit + heavy
    assert sort(100, 100, 100, 20) == "REJECTED"   # Volume limit + heavy

def test_invalid_inputs():
    """Test cases for invalid inputs"""
    # Negative numbers
    assert sort(-1, 10, 10, 10) == "REJECTED"
    assert sort(10, -1, 10, 10) == "REJECTED"
    
    # Zero
    assert sort(0, 10, 10, 10) == "REJECTED"
    assert sort(10, 0, 10, 10) == "REJECTED"
    
    # Non-numbers
    assert sort("abc", 10, 10, 10) == "REJECTED"
    assert sort(None, 10, 10, 10) == "REJECTED"
    assert sort([1], 10, 10, 10) == "REJECTED"
    
    # NaN and infinity
    assert sort(float('nan'), 10, 10, 10) == "REJECTED"
    assert sort(float('inf'), 10, 10, 10) == "REJECTED"

def test_string_numbers():
    """Test cases for valid string number inputs"""
    assert sort("10", "10", "10", "10") == "STANDARD"
    assert sort("150", "10", "10", "10") == "SPECIAL"
    assert sort("100", "100", "100", "20") == "REJECTED"

def test_floating_point():
    """Test cases for floating point numbers"""
    assert sort(15.9, 15.9, 15.9, 19.9) == "STANDARD"
    assert sort(150.1, 10, 10, 10) == "SPECIAL"
    assert sort(100.1, 100, 100, 10) == "SPECIAL"

if __name__ == "__main__":
    pytest.main([__file__])