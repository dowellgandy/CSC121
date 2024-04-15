import pytest
from employee import Employee

@pytest.fixture
def test_employee():
    """A test employee available to all test functions"""
    test_employee = Employee('test', 'employee', 30000)
    return test_employee

def test_give_default_raise(test_employee):
    """Test adding the default raise amount to the employee salary"""
    test_employee.give_raise()

def test_give_custom_raise(test_employee):
    """Test adding a custom raise to the employee salary"""
    test_employee.give_raise(10000)
