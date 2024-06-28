import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# タイトルと説明
st.title('世界の国々の人口の推移')
st.write("""
このアプリケーションでは、世界の国々の人口の推移をインタラクティブに表示します。
""")
# データをロード
df = px.data.gapminder()
# ユーザーインターフェース
selected_country = st.selectbox('国を選択してください:', df['Country'].unique())

# 選択された国のデータをフィルタリング
filtered_df = df[df['Country'] == selected_country]

# Plotlyを使用してインタラクティブなグラフを作成
fig = px.line(filtered_df, x='Year', y='Population', title=f'{selected_country}の人口の推移')

# グラフを表示
st.plotly_chart(fig)