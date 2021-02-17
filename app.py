# Core pkgs
import streamlit as st



# EDA pkgs
import pandas as pd 
import numpy as np

# Data visulization pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
st.set_option('deprecation.showfileUploaderEncoding', False)  # Apagar warning

# ML pkgs

def main():

	"""Aplicación de aprendizaje automático"""

	st.title("Aplicación de aprendizaje automático")
	st.text("Exploración de datos, visualización y construcción del modelo")

	activites = ["EDA","Plot","Model Building","About"]

	choice = st.sidebar.selectbox("Seleccine el paso",activites)

	if choice == 'EDA':
		st.subheader("Análisis exploratorio de los datos")

		data = st.file_uploader("Subir Dataset",type=["csv","txt"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())

			if st.checkbox("Ver dimensiones"):
				st.write(df.shape)

			if st.checkbox("Mostrar columnas"):
				all_columns = df.columns.to_list()
				st.write(all_columns)

			if st.checkbox("Mostrar resumen"):
				st.write(df.describe())

			if st.checkbox("Seleccionar columnas a mostrar"):
				selected_columns = st.multiselect("Select Columns",all_columns)
				new_df =  df[selected_columns]
				st.dataframe(new_df)

			if st.checkbox("Show Value Counts"):
				st.write(df.iloc[:,-1].value_counts())

			if st.checkbox("Correlation with Seaborn"):
				st.write(sns.heatmap(df.corr(),annot=True))
				st.pyplot()

			if st.checkbox("Pie Chart"):
				all_columns = df.columns.to_list()
				columns_to_plot = st.selectbox("Select 1 Column ",all_columns)
				pie_plot = df[columns_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
				st.write(pie_plot)
				st.pyplot()

	elif choice == 'Plot':
		st.subheader("Data Visualization")

		data = st.file_uploader("Upload Dataset",type=["csv","txt"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())

		if st.checkbox("Correlation with Seaborn"):
			st.write(sns.heatmap(df.corr(),annot=True))
			st.pyplot()
	





	elif choice == 'Model Building':
		st.subheader("Building ML Model ")





	elif choice == 'About':
		st.subheader("About")
		st.text("")





if __name__ == "__main__":
    main()