# test_container.py

def test_functionality():
    # Your test code goes here
    # For example:
    result = add(3, 5)
    assert result == 8, f"Expected 8 but got {result}"

def add(a, b):
    return a + b

if __name__ == "__main__":
    test_functionality()
    print("All tests passed successfully!")