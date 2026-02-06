# Test Project

A simple Python project demonstrating basic project structure and functionality.

## Project Structure

```
.
├── src/
│   └── main.py          # Main application code
├── tests/
│   └── test_main.py     # Test cases
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── LICENSE             # Project license
└── README.md           # This file
```

## Features

- Simple greeting function with customizable name parameter
- Basic test suite demonstrating functionality
- Clean project structure following Python best practices

## Installation

No external dependencies are required for basic functionality. Simply clone the repository:

```bash
git clone https://github.com/MoltJinx/test.git
cd test
```

## Usage

Run the main application:

```bash
python src/main.py
```

This will output:
```
Hello, World!
Hello, Python!
```

## Running Tests

Run the test suite:

```bash
python tests/test_main.py
```

Expected output:
```
Running tests...
✓ test_greet_default passed
✓ test_greet_custom_name passed
✓ test_greet_empty_string passed

All tests passed!
```

## Development

To use the greet function in your own code:

```python
from src.main import greet

# Default greeting
message = greet()  # Returns "Hello, World!"

# Custom greeting
custom = greet("GitHub")  # Returns "Hello, GitHub!"
```

## License

See LICENSE file for details.