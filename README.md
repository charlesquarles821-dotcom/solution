# Package Sorting System

A robotic automation solution for sorting packages based on their physical characteristics (dimensions and mass) into appropriate handling stacks.

## Overview

This system implements an algorithm for Thoughtful's robotic automation factory to dispatch packages to the correct stack according to their volume and mass, ensuring proper handling of different package types.

## Sorting Rules

### Package Classification

- **Bulky Package**: A package is considered bulky if:
  - Its volume (Width × Height × Length) ≥ 1,000,000 cm³ **OR**
  - Any dimension ≥ 150 cm

- **Heavy Package**: A package is considered heavy if:
  - Its mass ≥ 20 kg

### Stack Assignment

| Package Type | Stack | Description |
|--------------|-------|-------------|
| Standard | `STANDARD` | Neither bulky nor heavy - normal handling |
| Special | `SPECIAL` | Either bulky OR heavy - requires special handling |
| Rejected | `REJECTED` | Both bulky AND heavy - cannot be processed |

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required

### Running the Solution
```bash
# Navigate to the directory containing the solution
cd /path/to/solution

# Run the complete test suite
python3 solution.py
```

## Usage

### Basic Usage

```python
from solution import sort

# Sort a package with dimensions 50×30×20 cm and mass 15 kg
result = sort(width=50, height=30, length=20, mass=15)
print(result)  # Output: "STANDARD"

# Sort a heavy package
result = sort(width=10, height=10, length=10, mass=25)
print(result)  # Output: "SPECIAL"

# Sort a bulky package
result = sort(width=200, height=10, length=10, mass=5)
print(result)  # Output: "SPECIAL"

# Sort a rejected package (both heavy and bulky)
result = sort(width=200, height=10, length=10, mass=25)
print(result)  # Output: "REJECTED"
```

### Function Signature

```python
def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages into appropriate stacks.
    
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
```

## Testing

The solution includes a comprehensive test suite that validates:

- ✅ All sorting logic scenarios
- ✅ Edge cases at threshold boundaries  
- ✅ Input validation and error handling
- ✅ Type checking

### Running Tests

```bash
python3 solution.py
```

Expected output:
```
Package Sorting Algorithm - Test Results
==================================================
Test  1: ✓ PASS - Standard package
Test  2: ✓ PASS - Heavy package (not bulky)
Test  3: ✓ PASS - Bulky by volume (not heavy)
Test  4: ✓ PASS - Bulky by dimension (not heavy)
Test  5: ✓ PASS - Heavy and bulky by volume
Test  6: ✓ PASS - Heavy and bulky by dimension
Test  7: ✓ PASS - Edge case: just under thresholds
Test  8: ✓ PASS - Edge case: exactly at dimension threshold
Test  9: ✓ PASS - Edge case: exactly at volume threshold
Test 10: ✓ PASS - Edge case: exactly at mass threshold
--------------------------------------------------
Results: 10/10 tests passed

Error Handling Tests:
✓ PASS - Negative width: Correctly raised exception
✓ PASS - Zero height: Correctly raised exception
✓ PASS - Non-numeric width: Correctly raised exception
✓ PASS - Negative mass: Correctly raised exception
```

## Code Quality Features

This implementation follows professional software development practices:

- **Type Hints**: Full type annotations for better code clarity
- **Documentation**: Comprehensive docstrings following PEP 257
- **Error Handling**: Robust input validation with meaningful error messages
- **Enums**: Type-safe constants for package stacks
- **Class Design**: Separation of concerns with PackageClassifier
- **Testing**: Comprehensive test coverage including edge cases
- **Code Organization**: Clean, readable structure with logical separation

## Example Test Cases

| Width (cm) | Height (cm) | Length (cm) | Mass (kg) | Result | Reason |
|------------|-------------|-------------|-----------|---------|---------|
| 10 | 10 | 10 | 5 | STANDARD | Normal package |
| 10 | 10 | 10 | 25 | SPECIAL | Heavy only |
| 160 | 10 | 10 | 5 | SPECIAL | Bulky by dimension |
| 100 | 100 | 100 | 5 | SPECIAL | Bulky by volume |
| 160 | 10 | 10 | 25 | REJECTED | Both heavy and bulky |

## Performance Considerations

- **Time Complexity**: O(1) - Constant time for each package classification
- **Space Complexity**: O(1) - No additional data structures needed
- **Scalability**: Suitable for high-throughput robotic systems
