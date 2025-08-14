def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    import os
    # Use environment variable or default for CI
    user = os.environ.get("CI_USER", "CI Runner")
    print(greet(user))
