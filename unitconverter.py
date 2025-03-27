import streamlit as st

st.set_page_config(page_title="Unit Converter App", page_icon="🔄", layout="centered")

name = st.text_input("What is Your Name ?")
if name:
    st.success(f"Great to have you here, {name}! ")


st.title("Unit Converter App")
st.write("This app converts units of length, weight, area, time, and temperature.")

def convert_units(value, from_unit, to_unit, unit_type):
    conversions = {
        "Length": {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084},
        "Weight": {"grams": 1, "kilograms": 0.001 , "miligrams": 1000},
        "Time": {"seconds": 1, "minutes": 1/60, "hours": 1/3600, "days": 1/86400},
        "Area": {"square meters": 1, "square kilometers": 0.000001, "square miles": 3.861e-7,}

    }
    
    if unit_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    
    base_value = value / conversions[unit_type][from_unit]
    return base_value * conversions[unit_type][to_unit]

unit_type_labels = {
    "Length": "🔨 Length Converter",
    "Weight": "⚖️ Weight Converter",
    "Temperature": "🌡️ Temperature Converter",
    "Time": "⏳ Time Converter",
    "Area": "⚠️ Area Converter"
}

unit_type = st.radio("Choose conversion type:", list(unit_type_labels.keys()), index=0)
st.write(unit_type_labels[unit_type])

unit_options = {
    "Length": ["meters", "kilometers", "miles", "feet"],
    "Weight": ["grams", "kilograms"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["seconds", "minutes", "hours", "days"],
    "Area": ["square meters", "square kilometers", "square miles"]
}

from_unit = st.selectbox("From:", unit_options[unit_type])
to_unit = st.selectbox("To:", unit_options[unit_type])
value = st.number_input("Enter value:", value=0, step=1)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_type)
    st.success(f"Converted Value: {result} {to_unit}")



    