# Unit Converter

A Python library for converting between SI units and temperature measurements.

## Installation

```bash
pip install unit-converter
```

## Usage

The library provides a set of functions for converting between different units.

### Length Conversion

```python
from unit_converter import convert_length

# Convert 5 kilometers to miles
result = convert_length(5, 'kilometer', 'mile')
print(result)  # 3.1068559611866697

# Convert 12 inches to centimeters
result = convert_length(12, 'inch', 'centimeter')
print(result)  # 30.48
```

### Mass Conversion

```python
from unit_converter import convert_mass

# Convert 2 pounds to kilograms
result = convert_mass(2, 'pound', 'kilogram')
print(result)  # 0.90718474

# Convert 500 grams to ounces
result = convert_mass(500, 'gram', 'ounce')
print(result)  # 17.636980974790206
```

### Time Conversion

```python
from unit_converter import convert_time

# Convert 2 hours to minutes
result = convert_time(2, 'hour', 'minute')
print(result)  # 120

# Convert 1 week to days
result = convert_time(1, 'week', 'day')
print(result)  # 7
```

### Temperature Conversion

```python
from unit_converter import convert_temperature

# Convert 100 Celsius to Fahrenheit
result = convert_temperature(100, 'celsius', 'fahrenheit')
print(result)  # 212

# Convert 32 Fahrenheit to Celsius
result = convert_temperature(32, 'fahrenheit', 'celsius')
print(result)  # 0
```

### Get Supported Units

```python
from unit_converter import get_supported_units

# Get all supported units by category
supported_units = get_supported_units()
print(supported_units)
```

## Supported Units

### Length
- meter
- kilometer
- centimeter
- millimeter
- micrometer
- nanometer
- mile
- yard
- foot
- inch

### Mass
- kilogram
- gram
- milligram
- metric_ton
- pound
- ounce

### Time
- second
- minute
- hour
- day
- week
- year

### Temperature
- celsius
- fahrenheit
- kelvin

## Features

- High precision calculations using Python's Decimal
- Type hints for better IDE support
- Comprehensive error handling
- Support for both SI and common imperial units
- Easy to extend with new units

## License

MIT License
