"""
Tests for the main module.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import greet


def test_greet_default():
    """Test greet function with default parameter."""
    result = greet()
    assert result == "Hello, World!"


def test_greet_custom_name():
    """Test greet function with custom name."""
    result = greet("Python")
    assert result == "Hello, Python!"


def test_greet_empty_string():
    """Test greet function with empty string."""
    result = greet("")
    assert result == "Hello, !"


if __name__ == "__main__":
    # Simple test runner
    print("Running tests...")
    test_greet_default()
    print("✓ test_greet_default passed")
    
    test_greet_custom_name()
    print("✓ test_greet_custom_name passed")
    
    test_greet_empty_string()
    print("✓ test_greet_empty_string passed")
    
    print("\nAll tests passed!")
