"""
Tests for the main module.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.main import greet


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
    # Simple test runner with error handling
    print("Running tests...")
    tests = [
        ("test_greet_default", test_greet_default),
        ("test_greet_custom_name", test_greet_custom_name),
        ("test_greet_empty_string", test_greet_empty_string),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            test_func()
            print(f"✓ {test_name} passed")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_name} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_name} error: {e}")
            failed += 1
    
    print(f"\n{passed} passed, {failed} failed")
    if failed > 0:
        sys.exit(1)
