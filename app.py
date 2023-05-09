"""Indico Software Dashboard App"""

# @Email:  leonardocaballero@gmail.com
# @Website:  https://entrenamiento-data-scientist-python.readthedocs.io/
# @Github:  https://github.com/macagua
# @Project:  Indico Software Dashboard

import os
import pandas as pd
import plotly.express as px
import streamlit as st


# ---- MAKE A FULL PATH FOR THE EXCEL FILE ----
def get_full_path(filename):
    """Get full path for Excel file name

    Args:
        filename (str): Excel file name

    Returns:
        str: return a full path for Excel file name
    """
    full_path = os.path.dirname(
        os.path.abspath(__file__)
    ) + os.sep + "data" + os.sep + filename
    return full_path


# ---- READ EXCEL FILE ----
@st.cache_data
def get_data_from_excel(file_path, sheet_name, day_name):
    """Read a Excel file and put it into a Dataframe

    Args:
        file_path (str): the full path for Excel name to read
        sheet_name (str): the Excel sheet name to read

    Returns:
        Dataframe: a Dataframe with the data from Excel file
    """

    data_frame = pd.read_excel(
        io=file_path,
        engine="openpyxl",
        sheet_name=sheet_name,
        skiprows=0,
        nrows=1000,
    )
    # Added 'Dia' column to dataframe
    data_frame["Dia"] = day_name

    if sheet_name == "registrations":
        # Renamed 'Tags' column to dataframe
        data_frame.rename(columns={"Tags": "Tipo_Participantes"}, inplace=True)
        # Renamed 'Registration state' column to dataframe
        data_frame.rename(columns={"Registration state": "Estado_Registro"}, inplace=True)
        # Renamed 'Registration date' column to dataframe
        data_frame.rename(columns={"Registration date": "Fecha_Registro"}, inplace=True)
        # Renamed 'Country' column to dataframe
        data_frame.rename(columns={"Country": "Pais"}, inplace=True)
        # Renamed 'Name' column to dataframe
        data_frame.rename(columns={"Name": "Nombre"}, inplace=True)
        # Renamed 'Correo electrónico' column to dataframe
        data_frame.rename(columns={"Correo electrónico": "Correo_electronico"}, inplace=True)
        # Renamed 'Completed' elements in the 'Estado_Registro' column to dataframe
        data_frame["Estado_Registro"].replace(to_replace="Completed", value="Completado")
        # Renamed '' elements in the 'Country' column to dataframe
        data_frame.Pais = data_frame.Pais.fillna("Desconocido")
    elif sheet_name == "abstracts":
        # TODO: Add implementation
        pass
    elif sheet_name == "contributions":
        # TODO: Add implementation
        # Renamed 'Tags' column to dataframe
        data_frame.rename(columns={
            "Track": "Tematicas",
            "Title": "Titulo_Ponencia",
        }, inplace=True)
    return data_frame


# ---- SET PAGE CONFIG ----
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="Analítica del III evento aniversario 🎉",
    page_icon=":bar_chart:",
    layout="wide"
)

# ---- BUILD THE DATAFRAMES ----
df_3ea_dia1_abstracts = get_data_from_excel(
    get_full_path("3er_evento_aniversario_dia1.xlsx"),
    "abstracts",
    "25/02/2023"
)
df_3ea_dia1_contributions = get_data_from_excel(
    get_full_path("3er_evento_aniversario_dia1.xlsx"),
    "contributions",
    "25/02/2023"
)
df_3ea_dia1_registrations = get_data_from_excel(
    get_full_path("3er_evento_aniversario_dia1.xlsx"),
    "registrations",
    "25/02/2023"
)

df_3ea_dia2_abstracts = get_data_from_excel(
    get_full_path("3er_evento_aniversario_dia2.xlsx"),
    "abstracts",
    "04/03/2023"
)
df_3ea_dia2_contributions = get_data_from_excel(
    get_full_path("3er_evento_aniversario_dia2.xlsx"),
    "contributions",
    "04/03/2023"
)
df_3ea_dia2_registrations = get_data_from_excel(
    get_full_path("3er_evento_aniversario_dia2.xlsx"),
    "registrations",
    "04/03/2023"
)

# ---- MAKE THE SIDEBAR ----
st.sidebar.header("Por favor, filtre aquí:")
dias = st.sidebar.multiselect(
    "Seleccione el(los) día(s):",
    options=df_3ea_dia1_registrations["Dia"].unique(),
    default=df_3ea_dia1_registrations["Dia"].unique(),
)

pais = st.sidebar.multiselect(
    "Seleccione el país:",
    options=df_3ea_dia1_registrations["Pais"].unique(),
    default=df_3ea_dia1_registrations["Pais"].unique(),
)

estado_registro = st.sidebar.multiselect(
    "Seleccione el estado del registro:",
    options=df_3ea_dia1_registrations["Estado_Registro"].unique(),
    default=df_3ea_dia1_registrations["Estado_Registro"].unique(),
)

tipo_participantes = st.sidebar.multiselect(
    "Seleccione el tipo de participante:",
    options=df_3ea_dia1_registrations["Tipo_Participantes"].unique(),
    default=df_3ea_dia1_registrations["Tipo_Participantes"].unique(),
)

tipo_contribucion = st.sidebar.multiselect(
    "Seleccione el Tipo de contribución:",
    options=df_3ea_dia1_contributions["Type"].unique(),
    default=df_3ea_dia1_contributions["Type"].unique(),
)

track_contribucion = st.sidebar.multiselect(
    "Seleccione la(s) Temática(s):",
    options=df_3ea_dia1_contributions["Tematicas"].unique(),
    default=df_3ea_dia1_contributions["Tematicas"].unique(),
)

# ---- MAKE QUERY ----
df_seleccion_dia1_contributions = df_3ea_dia1_contributions.query(
    "Type == @tipo_contribucion & Tematicas ==@track_contribucion"
)

df_seleccion_dia1_registrations = df_3ea_dia1_registrations.query(
    "Pais == @pais & Estado_Registro ==@estado_registro & Tipo_Participantes ==@tipo_participantes"
)

# ---- MAIN PAGE ----
st.title(":bar_chart: Analítica del III evento aniversario - Día 1")
st.markdown("##")

# ---- KPI CONTRIBUTIONS ----
total_contribuidores = int(
    df_seleccion_dia1_contributions["Titulo_Ponencia"].count()
)
total_tracks = int(
    df_seleccion_dia1_contributions["Tematicas"].nunique()
)
total_track_0 = int(
    len(
        df_seleccion_dia1_contributions.loc[
            df_seleccion_dia1_contributions['Tematicas'] == 'Key Note'
        ]
    )
)

TRACK_1 = 'Transformación cultural organizacional'
total_track_1 = int(
    len(
        df_seleccion_dia1_contributions.loc[
            df_seleccion_dia1_contributions['Tematicas'] == TRACK_1
        ]
    )
)

TRACK_2 = 'Desarrollo de Equipos y Liderazgo Ágil'
total_track_2 = int(
    len(
        df_seleccion_dia1_contributions.loc[
            df_seleccion_dia1_contributions['Tematicas'] == TRACK_2
        ]
    )
)

TRACK_3 = 'Marcos de trabajo y metodologías ágiles'
total_track_3 = int(
    len(
        df_seleccion_dia1_contributions.loc[
            df_seleccion_dia1_contributions['Tematicas'] == TRACK_3
        ]
    )
)

TRACK_4 = 'Mindset Agile'
total_track_4 = int(
    len(
        df_seleccion_dia1_contributions.loc[
            df_seleccion_dia1_contributions['Tematicas'] == TRACK_4
        ]
    )
)

TRACK_5 = 'Otros conceptos importantes de la cultura agile'
total_track_5 = int(
    len(
        df_seleccion_dia1_contributions.loc[
            df_seleccion_dia1_contributions['Tematicas'] == TRACK_5
        ]
    )
)

# ---- KPI REGISTRATIONS ----
total_pais = int(
    df_seleccion_dia1_registrations["Pais"].nunique()
)
total_inscritos = int(
    df_seleccion_dia1_registrations["Nombre"].count()
)
total_participantes = int(
    len(
        df_seleccion_dia1_registrations.loc[
            df_seleccion_dia1_registrations['Tipo_Participantes'] == 'Participantes'
        ]
    )
)
total_facilitadores = int(
    len(
        df_seleccion_dia1_registrations.loc[
            df_seleccion_dia1_registrations['Tipo_Participantes'] == 'Facilitadores'
        ]
    )
)
total_staff = int(
    len(
        df_seleccion_dia1_registrations.loc[
            df_seleccion_dia1_registrations['Tipo_Participantes'] == 'Staff'
        ]
    )
)

st.header(":busts_in_silhouette: Tablero de asistencia")
columna_izquierda, columna_media, columna_derecha = st.columns(3)
with columna_izquierda:
    st.subheader("Total de Paises :earth_americas:")
    st.subheader(f"{total_pais}")
with columna_media:
    st.subheader("Total de inscritos :memo:")
    st.subheader(f":busts_in_silhouette: {total_inscritos}")
with columna_derecha:
    st.subheader("Total de Participantes :school_satchel:")
    st.subheader(f":busts_in_silhouette: {total_participantes}")
    # st.markdown("""---""")
    # st.subheader("Total de Facilitadores :school:")
    # st.subheader(f"{total_facilitadores}")
    st.markdown("""---""")
    st.subheader("Total de Moderadores :bust_in_silhouette:")
    st.subheader(":busts_in_silhouette: 8")
    st.markdown("""---""")
    st.subheader("Total de Staff :bust_in_silhouette:")
    st.subheader(f":busts_in_silhouette: {total_staff}")

st.markdown("""---""")

st.header(":school: Tablero de Facilitadores")
columna_izquierda, columna_media, columna_derecha = st.columns(3)
with columna_izquierda:
    st.subheader("Total de Facilitadores :mortar_board:")
    st.subheader(f":busts_in_silhouette: {total_contribuidores}")
with columna_media:
    st.subheader("Total de Temáticas :books:")
    st.subheader(f":notebook: {total_tracks}")
with columna_derecha:
    st.subheader("Facilitadores por Temáticas :memo:")
    st.markdown(f"* Key Note: **{total_track_0}**")
    st.markdown(f"* Transformación cultural organizacional: **{total_track_1}**")
    st.markdown(f"* Desarrollo de Equipos y Liderazgo Ágil: **{total_track_2}**")
    st.markdown(f"* Marcos de trabajo y metodologías ágiles: **{total_track_3}**")
    st.markdown(f"* Mindset Agile: **{total_track_4}**")
    st.markdown(f"* Otros conceptos importantes de la cultura agile: **{total_track_5}**")

# PONECIAS POR TEMATICAS [GRÁFICO DE BARRAS]
ponencias_por_tematicas = (
    df_seleccion_dia1_contributions.groupby(
        by=["Tematicas"]
    )['Titulo_Ponencia'].count()
)
fig_ponencias_por_tematicas = px.bar(
    ponencias_por_tematicas,
    x="Titulo_Ponencia",
    y=ponencias_por_tematicas.index,
    orientation="h",
    title="<b>Ponencias por Temáticas</b>",
    color_discrete_sequence=["#0083B8"] * len(ponencias_por_tematicas),
    template="plotly_white",
)
fig_ponencias_por_tematicas.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict({"title": "Total de ponencias"}, showgrid=False)),
    yaxis={"title": "Temáticas"},
)

columna_izquierda, columna_derecha = st.columns(2)
# columna_derecha = st.columns(1)
# columna_izquierda.plotly_chart(fig_ventas_por_horas, use_container_width=True)
columna_derecha.plotly_chart(
    fig_ponencias_por_tematicas,
    use_container_width=True
)

st.markdown("""---""")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# import pdb; pdb.set_trace();
