import pytest
from src.string_converter import to_constant_case

def test_to_constant_case_basic():
    assert to_constant_case("hello world") == "HELLO_WORLD"
    assert to_constant_case("camelCase") == "CAMEL_CASE"
    assert to_constant_case("snake_case") == "SNAKE_CASE"

def test_to_constant_case_special_chars():
    assert to_constant_case("hello-world") == "HELLO_WORLD"
    assert to_constant_case("hello@world") == "HELLO_WORLD"
    assert to_constant_case("  hello  world  ") == "HELLO_WORLD"

def test_to_constant_case_mixed_case():
    assert to_constant_case("MixedCaseString") == "MIXED_CASE_STRING"

def test_to_constant_case_edge_cases():
    assert to_constant_case("") == ""
    assert to_constant_case("a") == "A"

def test_to_constant_case_error_handling():
    with pytest.raises(TypeError):
        to_constant_case(123)
    with pytest.raises(TypeError):
        to_constant_case(None)