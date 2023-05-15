import os
import pandas as pd
import openpyxl
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(layout='centered')

# Durchsuche Ordner und Unterordner nach .xlsx Datei
current_dir = os.getcwd()
file_path = None
for root, dirs, files in os.walk(current_dir):
    for file in files:
        if file.endswith('.xlsx'):
            file_path = os.path.join(root, file)
            break
    if file_path is not None:
        break

if file_path is None:
    st.write("Keine .xlsx-Datei im aktuellen Verzeichnis gefunden")
else:
    df = pd.read_excel(file_path)
    # Rest des Codes...



df = df.fillna(1)
df.iloc[0:, 1:] = df.iloc[0:, 1:].astype(int)
categories = list(df.columns[1:])

num_columns = df.shape[1]
num_raws = df.shape[0]

fig = go.Figure()

for i in range(0, num_raws):
    r_values = df.iloc[i, 1:].tolist()
    r_values.append(r_values[0])

    fig.add_trace(go.Scatterpolar(
        r=r_values,
        theta=categories,
        fill='toself',
        name=df.iloc[i, 0]
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 6]
        )
    ),
    showlegend=True,
    width=1200,  # Anpassen der Breite
    height=1000  # Anpassen der Höhe
)

st.plotly_chart(fig)
