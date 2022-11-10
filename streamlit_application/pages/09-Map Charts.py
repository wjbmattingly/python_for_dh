import streamlit as st
import pandas as pd
import pydeck as pdk

st.header("Preparing the Data")
df = pd.read_feather("data/trc")
df = df.dropna()
df = df[["full_name", "long", "lat"]]
df["lat"] = pd.to_numeric(df["lat"], downcast="float")
df["long"] = pd.to_numeric(df["long"], downcast="float")
df.columns = ["full_name", "lon", "lat"]

df_code = """
df = pd.read_feather("data/trc")
df = df.dropna()
df = df[["full_name", "long", "lat"]]
df["lat"] = pd.to_numeric(df["lat"], downcast="float")
df["long"] = pd.to_numeric(df["long"], downcast="float")
df.columns = ["full_name", "lon", "lat"]
"""
st.code(df_code, language="python")
st.write(df)

st.header("Basic Map with st.map()")
st.code("st.map(df)", language="python")
st.map(df)

st.header("Advanced Map with st.pydeck_chart()")

map_code = """
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=-25.97,
        longitude=30.50,
        zoom=5,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            df,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=False,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=1000,
            line_width_min_pixels=5,
            get_position="[lon, lat]",
            get_radius="radius",
            get_fill_color=[255, 140, 0],
            get_line_color=[255, 140, 0],
                ),
    ],
))

"""
st.code(map_code, language="python")

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=-25.97,
        longitude=30.50,
        zoom=5,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            df,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=False,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=1000,
            line_width_min_pixels=5,
            get_position="[lon, lat]",
            get_radius="radius",
            get_fill_color=[255, 140, 0],
            get_line_color=[255, 140, 0],
                ),
    ],
))
