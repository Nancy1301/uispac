import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from streamlit_option_menu import option_menu
import numpy as np
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
import pandas_bokeh
pandas_bokeh.output_notebook()
import plotly.graph_objects as go

st.set_page_config(
    page_title="PAC Recommendation System",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# ticket_data = pd.read_csv("showsData/Report_TicketBuyerReport_9-25-2023_10-53-43AM.csv")
# show_data=pd.read_excel("showsData/SHOWS.xlsx", header=None)
# uis_ticket_data=pd.read_excel("showsData/UISPAC_TICKET_DATA.xlsx")

# show_data.rename(columns={0: 'Season'}, inplace=True)
# show_data.rename(columns={1: 'Genre'}, inplace=True)
# show_data.rename(columns={2: 'PerformanceName'}, inplace=True)
# show_data['Genre'] = show_data['Genre'].str.replace('/', ', ')
# show_data['Season'] = show_data['Season'].astype(str).str.replace('.', ' - ')
# show_data['Season'] = show_data['Season'].astype(str).str.replace('19 - 2', '19 - 20')
# show_data.loc[show_data['Genre'] == 'MUSC', 'Genre'] = 'MUSIC'
# show_data['Genres'] = show_data['Genre'].str.split(', ')

# all_genres = [genre for genres_list in show_data['Genres'].dropna() for genre in genres_list]
# unique_genres = set(all_genres)
# unique_genres_array = np.array(list(unique_genres))
# num_unique_genres = len(unique_genres)
# genre_counts = show_data['Genres'].explode().value_counts()

# # Disabling the warning
# st.set_option('deprecation.showPyplotGlobalUse', False)
# result = pd.merge(uis_ticket_data, ticket_data, how='outer', left_index=True, right_index=True, suffixes=('', '_remove'))
# exclude_columns = ['OrderID']
# aggregation_functions = {col: 'first' for col in result.columns if col not in exclude_columns}

# aggregation_functions.update({'Quantity': 'sum'})
# result['Quantity'] = 1
# result_df = result.groupby('OrderID').agg(aggregation_functions).reset_index()

# nunique = result_df.nunique()
# cols_to_drop = nunique[nunique == 1].index
# result_df = result_df.drop(cols_to_drop, axis=1)

# nunique = result_df.nunique()
# cols_to_drop = nunique[nunique == 0].index
# result_df = result_df.drop(cols_to_drop, axis=1)

# result_df.to_csv('showsData/research_data_merge.csv', index=True)

# result_df['Quantity'] = result_df['Quantity'].astype(int)

# nomi = pgeocode.Nominatim('us')

# result_df['Location Name'] = (nomi.query_postal_code(result_df['Billing_ZipCode'].tolist()).place_name + ', ' + (nomi.query_postal_code(result_df['Billing_ZipCode'].tolist()).state_code))
# result_df['Latitude'] = (nomi.query_postal_code(result_df['Billing_ZipCode'].tolist()).latitude)
# result_df['Longitude'] = (nomi.query_postal_code(result_df['Billing_ZipCode'].tolist()).longitude)


# merged_show_data = pd.merge(result_df, show_data, how='inner', on='PerformanceName')
# grouped_zip_data = merged_show_data.groupby('Billing_ZipCode')['Quantity'].sum().reset_index()
# unique_zip_count = grouped_zip_data['Quantity'].sum()
# grouped_data = merged_show_data.groupby('PerformanceName')['Quantity'].sum().reset_index()
# unique_show_count = grouped_data['Quantity'].sum()

# def plot_data(data):
#     plt.figure(figsize=(5, 3))
#     sns.countplot(y='Season', data=data, palette='Dark2')
#     plt.title('Count of data by Season')
#     plt.xlabel('Count')
#     plt.ylabel('Season')
#     plt.grid(True, axis='x')
#     st.pyplot()

# def plot_genre_counts(genre_counts):
#     plt.figure(figsize=(10, 6))
#     genre_counts.plot(kind='bar')
#     plt.xlabel('Genre')
#     plt.ylabel('Count')
#     plt.title('Count of Shows by Genre')
#     st.pyplot()

# def generate_density_map(result_df):
#     # Create the figure
#     fig = go.Figure(data=go.Densitymapbox(
#         lon=result_df['Longitude'],
#         lat=result_df['Latitude'],
#         z=result_df['Quantity'],
#         text=result_df['Location Name'],
#         customdata=result_df['OrderID'],
#         radius=10,
#         colorscale='HSV',
#         colorbar_title='Quantity',
#         hovertemplate='<b>Order Id:</b> %{customdata}<br><b><b>Location:</b> %{text}<br><b>Quantity:</b> %{z}<extra></extra>'
#     ))
#     fig.update_layout(
#         mapbox_style="carto-positron",
#         mapbox_zoom=5,
#         mapbox_center={"lat": 41.8781, "lon": -87.6298},  # Centered around Chicago, Illinois
#         margin={"r": 0, "t": 0, "l": 0, "b": 0},
#         title='Heat Map of Illinois: Zip Code Counts'
#     )
#     st.plotly_chart(fig)

# def plot_bar_chart(grouped_data):
#     # Create the figure
#     plt.figure(figsize=(12, 8))
#     plt.bar(grouped_data['PerformanceName'], grouped_data['Quantity'], color=sns.palettes.mpl_palette('Dark2'))
#     plt.xlabel('Performance Name')
#     plt.ylabel('Total Quantity')
#     plt.title('Total Quantity Grouped by Genre')
#     plt.xticks(rotation=45, ha='right')
#     # Show the plot using Streamlit
#     st.pyplot(plt)

def uploadFile():
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    # for uploaded_file in uploaded_files:
    #     st.write("The uploaded file is", uploaded_file.name)
    # Place a button for process to show summary + head
    

with st.sidebar:
    st.title('PAC Recommendation System')
    plot_type = st.sidebar.radio("Select Plot Type", ("Count by Season","Upload the file","Count by Genre", "Total Quantity With Genre", "Density Map"  ))

    
def main():

   # uploadFile()
    # if plot_type == "Count by Season":
    #     plot_data(show_data)
    if plot_type == "Upload the file":
        uploadFile()
    # elif plot_type == "Count by Genre":
    #     plot_genre_counts(genre_counts)
    # elif plot_type == "Total Quantity With Genre":
    #     plot_bar_chart(grouped_data)
    # elif plot_type == "Density Map":
    #     generate_density_map(result_df)

if __name__ == "__main__":
    main()

