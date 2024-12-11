import pytest
from package_sort import sort

def test_volume_overflow():
    """Test cases for volume overflow"""
    # Large numbers that would cause overflow
    assert sort(1e308, 1e308, 1e308, 10) == "REJECTED"
    assert sort(1e200, 1e200, 1e200, 10) == "REJECTED"
    
    # Numbers that multiply to overflow
    assert sort(1e200, 1e200, 1e200, 5) == "REJECTED"
    
    # One very large number
    assert sort(1e308, 10, 10, 10) == "SPECIAL"  # Should still work as it's over 150

def test_standard_packages():
    """Test cases for STANDARD packages"""
    assert sort(10, 10, 10, 10) == "STANDARD"
    assert sort(50, 50, 50, 19.99) == "STANDARD"
    assert sort(1, 1, 1, 1) == "STANDARD"
    assert sort("10.5", "10.5", "10.5", "10.5") == "STANDARD"

def test_special_packages_heavy():
    """Test cases for SPECIAL packages due to weight"""
    assert sort(10, 10, 10, 20) == "SPECIAL"
    assert sort(10, 10, 10, 21) == "SPECIAL"
    assert sort(10, 10, 10, "20.5") == "SPECIAL"

def test_special_packages_bulky():
    """Test cases for SPECIAL packages due to size"""
    assert sort(150, 10, 10, 10) == "SPECIAL"
    assert sort(100, 100, 100.1, 10) == "SPECIAL"
    assert sort("150", 10, 10, 10) == "SPECIAL"

def test_rejected_invalid_inputs():
    """Test cases for REJECTED packages due to invalid inputs"""
    # Negative numbers
    assert sort(-1, 10, 10, 10) == "REJECTED"
    assert sort(10, -1, 10, 10) == "REJECTED"
    assert sort(10, 10, -1, 10) == "REJECTED"
    assert sort(10, 10, 10, -1) == "REJECTED"
    
    # Zero values
    assert sort(0, 10, 10, 10) == "REJECTED"
    assert sort(10, 0, 10, 10) == "REJECTED"
    assert sort(10, 10, 0, 10) == "REJECTED"
    assert sort(10, 10, 10, 0) == "REJECTED"
    
    # Invalid types
    assert sort("abc", 10, 10, 10) == "REJECTED"
    assert sort(None, 10, 10, 10) == "REJECTED"
    assert sort([1], 10, 10, 10) == "REJECTED"
    assert sort({}, 10, 10, 10) == "REJECTED"
    assert sort(10, "abc", 10, 10) == "REJECTED"

def test_rejected_bulky_and_heavy():
    """Test cases for REJECTED packages due to being both bulky and heavy"""
    assert sort(150, 10, 10, 20) == "REJECTED"
    assert sort(100, 100, 100.1, 20) == "REJECTED"
    assert sort(150, 150, 150, 20) == "REJECTED"

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    # Just under limits
    assert sort(149.99, 149.99, 149.99, 19.99) == "SPECIAL"
    
    # At volume limit
    assert sort(100, 100, 100, 10) == "STANDARD"
    
    # String numbers with whitespace
    assert sort(" 10 ", "10", "10", "10") == "STANDARD"
    
    # Scientific notation
    assert sort("1e2", "1e2", "1e2", 10) == "SPECIAL"
    
    # Floating point precision
    assert sort(1.23456789, 1.23456789, 1.23456789, 10) == "STANDARD"

def test_floating_point_precision():
    """Test floating point precision cases"""
    # Values just around volume limit
    assert sort(99.99999, 99.99999, 99.99999, 10) == "STANDARD"
    assert sort(100.00001, 100.00001, 100.00001, 10) == "SPECIAL"

if __name__ == "__main__":
    pytest.main([__file__])