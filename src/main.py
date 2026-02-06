"""
Main application module.
"""

def greet(name: str = "World") -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet. Defaults to "World".
    
    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def main():
    """Main entry point of the application."""
    message = greet()
    print(message)
    
    # Example with custom name
    custom_message = greet("Python")
    print(custom_message)


if __name__ == "__main__":
    main()
