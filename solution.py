"""
Thoughtful Robotic Automation Factory - Package Sorting System

This module implements a package sorting algorithm for robotic arms to dispatch
packages to appropriate stacks based on their physical characteristics.

Author: [Your Name]
Date: October 25, 2025
"""

from typing import Union
from enum import Enum


class PackageStack(Enum):
    """Enumeration of available package stacks."""
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


class PackageClassifier:
    """Classifier for package sorting based on volume and mass criteria."""
    
    # Class constants for sorting thresholds
    VOLUME_THRESHOLD_CM3 = 1_000_000
    DIMENSION_THRESHOLD_CM = 150
    MASS_THRESHOLD_KG = 20
    
    @classmethod
    def is_bulky(cls, width: float, height: float, length: float) -> bool:
        """
        Determine if a package is considered bulky.
        
        A package is bulky if:
        - Its volume (W × H × L) >= 1,000,000 cm³, OR
        - Any dimension >= 150 cm
        
        Args:
            width: Package width in centimeters
            height: Package height in centimeters
            length: Package length in centimeters
            
        Returns:
            bool: True if package is bulky, False otherwise
        """
        volume = width * height * length
        return (volume >= cls.VOLUME_THRESHOLD_CM3 or 
                any(dim >= cls.DIMENSION_THRESHOLD_CM 
                    for dim in [width, height, length]))
    
    @classmethod
    def is_heavy(cls, mass: float) -> bool:
        """
        Determine if a package is considered heavy.
        
        Args:
            mass: Package mass in kilograms
            
        Returns:
            bool: True if package is heavy (>= 20kg), False otherwise
        """
        return mass >= cls.MASS_THRESHOLD_KG


def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages into appropriate stacks based on their dimensions and mass.
    
    Sorting Rules:
    - STANDARD: Not bulky and not heavy
    - SPECIAL: Either bulky OR heavy (but not both)
    - REJECTED: Both bulky AND heavy
    
    Args:
        width: Package width in centimeters (must be positive)
        height: Package height in centimeters (must be positive)
        length: Package length in centimeters (must be positive)
        mass: Package mass in kilograms (must be positive)
        
    Returns:
        str: Stack designation ("STANDARD", "SPECIAL", or "REJECTED")
        
    Raises:
        ValueError: If any dimension or mass is not positive
        TypeError: If arguments are not numeric
    """
    # Input validation
    try:
        dimensions = [float(width), float(height), float(length), float(mass)]
    except (ValueError, TypeError) as e:
        raise TypeError("All arguments must be numeric") from e
    
    if any(dim <= 0 for dim in dimensions):
        raise ValueError("All dimensions and mass must be positive values")
    
    # Classification logic
    bulky = PackageClassifier.is_bulky(width, height, length)
    heavy = PackageClassifier.is_heavy(mass)
    
    if bulky and heavy:
        return PackageStack.REJECTED.value
    elif bulky or heavy:
        return PackageStack.SPECIAL.value
    else:
        return PackageStack.STANDARD.value


def run_comprehensive_tests() -> None:
    """Run comprehensive test suite to validate the sorting algorithm."""
    
    test_cases = [
        # (width, height, length, mass, expected_result, description)
        (10, 10, 10, 5, "STANDARD", "Standard package"),
        (10, 10, 10, 25, "SPECIAL", "Heavy package (not bulky)"),
        (100, 100, 100, 5, "SPECIAL", "Bulky by volume (not heavy)"),
        (160, 10, 10, 5, "SPECIAL", "Bulky by dimension (not heavy)"),
        (100, 100, 100, 25, "REJECTED", "Heavy and bulky by volume"),
        (160, 10, 10, 25, "REJECTED", "Heavy and bulky by dimension"),
        (149, 149, 45, 19, "STANDARD", "Edge case: just under thresholds"),
        (150, 10, 10, 19, "SPECIAL", "Edge case: exactly at dimension threshold"),
        (100, 100, 100, 19, "SPECIAL", "Edge case: exactly at volume threshold"),
        (10, 10, 10, 20, "SPECIAL", "Edge case: exactly at mass threshold"),
    ]
    
    print("Package Sorting Algorithm - Test Results")
    print("=" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for i, (w, h, l, m, expected, desc) in enumerate(test_cases, 1):
        try:
            result = sort(w, h, l, m)
            status = "✓ PASS" if result == expected else "✗ FAIL"
            if result != expected:
                print(f"Test {i:2d}: {status} - {desc}")
                print(f"         Expected: {expected}, Got: {result}")
            else:
                print(f"Test {i:2d}: {status} - {desc}")
                passed += 1
        except Exception as e:
            print(f"Test {i:2d}: ✗ ERROR - {desc}")
            print(f"         Exception: {e}")
    
    print("-" * 50)
    print(f"Results: {passed}/{total} tests passed")
    
    # Test error handling
    print("\nError Handling Tests:")
    error_cases = [
        ((-1, 10, 10, 5), "Negative width"),
        ((10, 0, 10, 5), "Zero height"), 
        (("abc", 10, 10, 5), "Non-numeric width"),
        ((10, 10, 10, -5), "Negative mass"),
    ]
    
    for args, desc in error_cases:
        try:
            sort(*args)
            print(f"✗ FAIL - {desc}: Should have raised an exception")
        except (ValueError, TypeError):
            print(f"✓ PASS - {desc}: Correctly raised exception")


if __name__ == "__main__":
    run_comprehensive_tests()
