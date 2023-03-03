import streamlit as st

# Add a header
st.header("Ghost Dance - A continued prophecy")

# Add text underneath the link
st.write("This is the patent that the math is based on.")


# Add a link
st.markdown("https://patents.google.com/patent/US20060014125A1/en")

st.write("""* Purpose of the training system is to increase human energy substantially 
* Result of training will enable capabilities such as:
    * Walking through walls
    * Body levitation
    * Instantaneous healing of infections
    * Full-body teleportation to another location
    * Remote viewing at vast distances in terms of light-years
    * Looking into hyperspace co-dimensions
    
* Invention based on the relationship between water molecule and boundary between space and hyperspace
* Mass of water molecule = energy of water molecule at Planck boundary
* Body composed of 67% water and sits on the boundary
* Additional increase in energy would move body out of dimension into "hyperspace"
* Human beings are hyperspace energy beings living in physical bodies
* Additional energy required to move body out of dimension comes from increasing energy of hyperspace being
* One source of this energy comes from walking cross-handed at proper velocity to generate a large hyperspace energy vortex
* This increased hyperspace energy enables person to walk around out of dimension through solid wooden doors
* Door and person are in two slightly different dimensions at the same moment
* Person appears to be walking through door""")


# Create a sidebar with a slider to choose between pounds and kilograms
unit = st.sidebar.selectbox("Choose a unit of weight", ["pounds", "kilograms"])

# Create a text input field for the user to enter their weight
weight = st.number_input("Enter your weight:", value=1)

# Convert the weight to the selected unit
if unit == "pounds":
    weight_in_kg = weight * 0.453592
else:
    weight_in_kg = weight

# Calculate the length using the formula L=(M/W)*T
length_in_meters = (50.909563606 / weight_in_kg) * 1

# Convert the length to feet and display the result
length_in_feet = length_in_meters * 3.28084
st.write(f"Meters per second to step: {length_in_meters}")
st.write(f"Feet per second to step: {length_in_feet}")

st.markdown("""
### Use a metronome to improve your accuracy.
""")
st.video("https://www.youtube.com/watch?v=ymJIXzvDvj4&t=79s")
