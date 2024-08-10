import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

def main():
    st.set_page_config(page_title="Aircraft Sizing Calculator", page_icon="✈️")
    # Get the current directory
    current_directory = os.path.dirname(__file__)
    logo_path = os.path.join(current_directory, "blaze.jpeg")

    image = Image.open(logo_path)
    
    # Center-align the image
    st.markdown(
        "<div style='text-align: center;'>"
        "<img src='data:image/jpeg;base64,{}' alt='Logo' width='300px'>"
        "</div>".format(image_to_base64(image)),
        unsafe_allow_html=True
    )

    st.title("Aircraft Sizing Calculator")
    weight = st.number_input("Enter the desired MTOW in grams:")
    wcl = st.number_input("Enter the desired wing cubical loading:")
    aspect_ratio = st.number_input("Enter the desired aspect ratio:")

    option = st.selectbox("Select the desired wing configuration", ["Rectangular", "Tapered", "Delta"])

    if option == 'Tapered':
        Taper_Ratio = st.number_input("Enter the desired taper ratio:")


    submit_button = st.button("Calculate")

    if submit_button:
        if option == "Rectangular":
            rectangular(weight, wcl, aspect_ratio)

        elif option == "Tapered":
            tapered(weight, wcl, aspect_ratio, Taper_Ratio)

        elif option == "Delta":
            delta(weight, wcl, aspect_ratio)

    # Footer text
    st.markdown(
        "<div style='position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; color: #999;'>"
        "All rights reserved by Blaze Inc."
        "</div>",
        unsafe_allow_html=True
    )

def rectangular(weight, wcl, aspect_ratio):
    # WING CALCULATIONS:
    a = weight / 28.35
    wing_area = (a / wcl) ** (2 / 3)
    a_1 = wing_area * 144
    st.write('### Wing Area:', a_1, 'sq inches')
    wing_span = (aspect_ratio * a_1) ** (1 / 2)
    st.write('### Wing Span:', wing_span, 'inches')
    chord_length = (a_1 / wing_span)
    st.write('### Chord Length:', chord_length, 'inches')
    W_Loading = a / wing_area
    st.write('### Wing loading:', W_Loading, 'oz/sq ft')

    # FUSELAGE CALCULATIONS:
    F_length = 0.70 * wing_span
    F_height = 0.10 * F_length
    st.write('### Fuselage Length:', F_length, 'inches')
    st.write('### Fuselage Height:', F_height, 'inches')

    # EMPENNAGE CALCULATIONS:
    H_stab_w = (0.15 * F_length)
    Area_H_stab = (0.30 * a_1)
    H_stab_length = (Area_H_stab / H_stab_w)
    st.write('### Width of Horizontal Stabilizer:', H_stab_w, 'inches')
    st.write('### Length of Horizontal Stabilizer:', H_stab_length, 'inches')
    st.write('### Area of Horizontal Stabilizer:', Area_H_stab, 'sq inches')

    V_stab_w = (0.15 * F_length)
    Area_V_stab = (0.50 * Area_H_stab)
    V_stab_height = (Area_V_stab / V_stab_w)
    st.write('### Width of Vertical Stabilizer:', V_stab_w, 'inches')
    st.write('### Height of Vertical Stabilizer:', V_stab_height, 'inches')
    st.write('### Area of Vertical Stabilizer:', Area_V_stab, 'sq inches')

    # CONTROL SURFACE CALCULATIONS:
    Aielirons_length = (0.60 * wing_span)
    Aielirons_width = (0.20 * chord_length)
    Rudder_height = (V_stab_height)
    Rudder_width = (0.35 * V_stab_w)
    Elevator_length = H_stab_length
    Elevator_width = (0.35 * H_stab_w)
    st.write('### Aileron Length:', Aielirons_length / 2, 'inches')
    st.write('### Aileron Width', Aielirons_width, 'inches')
    st.write('### Rudder Height:', Rudder_height, 'inches')
    st.write('### Rudder Width', Rudder_width, 'inches')
    st.write('### Elevator Length:', Elevator_length, 'inches')
    st.write('### Elevator Width', Elevator_width, 'inches')

def tapered(weight, wcl, aspect_ratio, Taper_Ratio):
    a = weight / 28.35
    wing_area = (a / wcl) ** (2 / 3)
    a_1 = wing_area * 144
    st.write('### Wing Area:', a_1, 'sq inches')
    wing_span = (aspect_ratio * a_1) ** (1 / 2)
    st.write('### Wing Span:', wing_span, 'inches')
    W_Loading = a / wing_area
    st.write('### Wing loading:', W_Loading, 'oz/sq ft')
    Tp_area = a_1 / 2
    Root_chord = 2 * Tp_area / ((Tp_area / 10) * (1 + Taper_Ratio))
    Tip_chord = Taper_Ratio * Root_chord
    MAC = (2/3) * Root_chord * ((1 + Taper_Ratio + Taper_Ratio**2) / (1 + Taper_Ratio))
    st.write('### Trapezium Area:', Tp_area, 'sq inches')
    st.write('### Root Chord:', Root_chord, 'inches')
    st.write('### Tip Chord:', Tip_chord, 'inches')
    st.write('### Mean Aerodynamic Chord:', MAC, 'inches')

    # FUSELAGE CALCULATIONS:
    F_length = 0.70 * wing_span
    F_height = 0.10 * F_length
    st.write('### Fuselage Length:', F_length, 'inches')
    st.write('### Fuselage Height:', F_height, 'inches')

    # EMPENNAGE CALCULATIONS:
    H_stab_w = (0.15 * F_length)
    Area_H_stab = (0.30 * a_1)
    H_stab_length = (Area_H_stab / H_stab_w)
    st.write('### Width of Horizontal Stabilizer:', H_stab_w, 'inches')
    st.write('### Length of Horizontal Stabilizer:', H_stab_length, 'inches')
    st.write('### Area of Horizontal Stabilizer:', Area_H_stab, 'sq inches')

    V_stab_w = (0.15 * F_length)
    Area_V_stab = (0.50 * Area_H_stab)
    V_stab_height = (Area_V_stab / V_stab_w)
    st.write('### Width of Vertical Stabilizer:', V_stab_w, 'inches')
    st.write('### Height of Vertical Stabilizer:', V_stab_height, 'inches')
    st.write('### Area of Vertical Stabilizer:', Area_V_stab, 'sq inches')

    # CONTROL SURFACE CALCULATIONS:
    Avg_chord = (Root_chord + Tip_chord / 2)
    Aielirons_length = (0.60 * wing_span)
    Aielirons_width = (0.20 * Avg_chord)
    Rudder_height = (V_stab_height)
    Rudder_width = (0.35 * V_stab_w)
    Elevator_length = H_stab_length
    Elevator_width = (0.35 * H_stab_w)
    st.write('### Aileron Length:', Aielirons_length / 2, 'inches')
    st.write('### Aileron Width', Aielirons_width, 'inches')
    st.write('### Rudder Height:', Rudder_height, 'inches')
    st.write('### Rudder Width', Rudder_width, 'inches')
    st.write('### Elevator Length:', Elevator_length, 'inches')
    st.write('### Elevator Width', Elevator_width, 'inches')

def delta(weight, wcl, aspect_ratio):
    Taper_Ratio = 0
    a = weight / 28.35
    wing_area = (a / wcl) ** (2 / 3)
    a_1 = wing_area * 144
    st.write('### Wing Area:', a_1, 'sq inches')
    wing_span = (aspect_ratio * a_1) ** (1 / 2)
    st.write('### Wing Span:', wing_span, 'inches')
    Root_chord = 2 * a_1 / wing_span
    st.write('### Root Chord:', Root_chord, 'inches')
    W_Loading = a / wing_area
    st.write('### Wing loading:', W_Loading, 'oz/sq ft')
    MAC = (2/3) * Root_chord * ((1 + Taper_Ratio + Taper_Ratio**2) / (1 + Taper_Ratio))
    st.write('### Mean Aerodynamic Chord:', MAC, 'inches')

    # FUSELAGE CALCULATIONS:
    F_length = 0.70 * wing_span
    F_height = 0.10 * F_length
    st.write('### Fuselage Length:', F_length, 'inches')
    st.write('### Fuselage Height:', F_height, 'inches')

    # EMPENNAGE CALCULATIONS:
    H_stab_w = (0.15 * F_length)
    Area_H_stab = (0.30 * a_1)
    H_stab_length = (Area_H_stab / H_stab_w)
    st.write('### Width of Horizontal Stabilizer:', H_stab_w, 'inches')
    st.write('### Length of Horizontal Stabilizer:', H_stab_length, 'inches')
    st.write('### Area of Horizontal Stabilizer:', Area_H_stab, 'sq inches')
    
    V_stab_w = (0.15 * F_length)
    Area_V_stab = (0.50 * Area_H_stab)
    V_stab_height = (Area_V_stab / V_stab_w)
    st.write('### Width of Vertical Stabilizer:', V_stab_w, 'inches')
    st.write('### Height of Vertical Stabilizer:', V_stab_height, 'inches')
    st.write('### Area of Vertical Stabilizer:', Area_V_stab, 'sq inches')

    # CONTROL SURFACE CALCULATIONS:
    Avg_chord = (Root_chord / 2)
    Aielirons_length = (0.50 * wing_span)
    Aielirons_width = (0.20 * Avg_chord)
    Rudder_height = (V_stab_height)
    Rudder_width = (0.35 * V_stab_w)
    Elevator_length = (0.50 * wing_span)
    Elevator_width = (0.40 * Avg_chord)
    st.write('### Aileron Length:', Aielirons_length / 2, 'inches')
    st.write('### Aileron Width', Aielirons_width, 'inches')
    st.write('### Rudder Height:', Rudder_height, 'inches')
    st.write('### Rudder Width', Rudder_width, 'inches')
    st.write('### Elevator Length:', Elevator_length / 2, 'inches')
    st.write('### Elevator Width', Elevator_width, 'inches')


# if __name__ == "__main__":
main()
