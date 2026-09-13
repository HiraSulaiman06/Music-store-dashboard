import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Music Store Dashboard",
    page_icon="🎵",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("music_combined.csv")
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    return df

df = load_data()

# -----------------------------
# Dashboard Header
# -----------------------------
st.title("🎵 Music Store Sales Dashboard")
st.markdown(
    "### Explore sales performance, customer activity, genres and tracks"
)

st.divider()

#----------------------------
# Professional Sidebar
# -----------------------------
st.sidebar.title("🎵 Music Store")
st.sidebar.markdown("### 🔎 Dashboard Filters")
st.sidebar.caption("Use the filters below to explore sales performance.")

st.sidebar.divider()

# Country Filter
countries = st.sidebar.multiselect(
    "🌍 Country",
    options=sorted(df["billing_country"].unique()),
    default=sorted(df["billing_country"].unique())
)

# Genre Filter
genres = st.sidebar.multiselect(
    "🎸 Genre",
    options=sorted(df["genre_name"].unique()),
    default=sorted(df["genre_name"].unique())
)

# Date Filter
st.sidebar.markdown("📅 **Date Range**")

date_range = st.sidebar.date_input(
    "Select period",
    value=[
        df["invoice_date"].min().date(),
        df["invoice_date"].max().date()
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

# Reset button
if st.sidebar.button("🔄 Reset Filters", use_container_width=True):
    st.rerun()

st.sidebar.caption("🎶 Music Store Sales Analysis")

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df[
    (df["billing_country"].isin(countries)) &
    (df["genre_name"].isin(genres)) &
    (df["invoice_date"].dt.date >= date_range[0]) &
    (df["invoice_date"].dt.date <= date_range[1])
]

# -----------------------------
# KPI Cards
# -----------------------------
total_revenue = filtered_df["revenue"].sum()
total_invoices = filtered_df["invoice_id"].nunique()
total_tracks = filtered_df["track_id"].nunique()
total_customers = filtered_df["customer_id"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Revenue",
    f"${total_revenue:,.2f}"
)

col2.metric(
    "🧾 Invoices",
    f"{total_invoices:,}"
)

col3.metric(
    "🎵 Tracks Sold",
    f"{total_tracks:,}"
)

col4.metric(
    "👥 Customers",
    f"{total_customers:,}"
)

st.divider()

# -----------------------------
# Monthly Revenue Trend
# -----------------------------
monthly = (
    filtered_df
    .assign(month=filtered_df["invoice_date"].dt.to_period("M").astype(str))
    .groupby("month", as_index=False)["revenue"]
    .sum()
)

fig_monthly = px.line(
    monthly,
    x="month",
    y="revenue",
    markers=True,
    title="📈 Monthly Revenue Trend"
)

fig_monthly.update_layout(
    xaxis_title="",
    yaxis_title="Revenue ($)",
    hovermode="x unified"
)

fig_monthly.update_traces(
    hovertemplate="Revenue: $%{y:,.2f}<extra></extra>"
)

st.plotly_chart(fig_monthly, use_container_width=True)


# -----------------------------
# Revenue by Genre & Country
# -----------------------------
col1, col2 = st.columns(2)

# Genre
genre_sales = (
    filtered_df.groupby("genre_name", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=True)
)

fig_genre = px.bar(
    genre_sales,
    x="revenue",
    y="genre_name",
    orientation="h",
    title="🎸 Revenue by Genre"
)

fig_genre.update_layout(
    xaxis_title="Revenue ($)",
    yaxis_title="",
    showlegend=False
)

fig_genre.update_traces(
    hovertemplate="$%{x:,.2f}<extra></extra>"
)

col1.plotly_chart(fig_genre, use_container_width=True)


# Country
country_sales = (
    filtered_df.groupby("billing_country", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
    .head(10)
    .sort_values("revenue", ascending=True)
)

fig_country = px.bar(
    country_sales,
    x="revenue",
    y="billing_country",
    orientation="h",
    title="🌍 Top 10 Countries by Revenue"
)

fig_country.update_layout(
    xaxis_title="Revenue ($)",
    yaxis_title="",
    showlegend=False
)

fig_country.update_traces(
    hovertemplate="$%{x:,.2f}<extra></extra>"
)

col2.plotly_chart(fig_country, use_container_width=True)


# -----------------------------
# Top Tracks & Cities
# -----------------------------
col1, col2 = st.columns(2)

# Top Tracks
top_tracks = (
    filtered_df.groupby("track_name", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
    .head(10)
    .sort_values("revenue", ascending=True)
)

fig_tracks = px.bar(
    top_tracks,
    x="revenue",
    y="track_name",
    orientation="h",
    title="🎵 Top 10 Tracks by Revenue"
)

fig_tracks.update_layout(
    xaxis_title="Revenue ($)",
    yaxis_title="",
    showlegend=False
)

fig_tracks.update_traces(
    hovertemplate="$%{x:,.2f}<extra></extra>"
)

col1.plotly_chart(fig_tracks, use_container_width=True)


# Top Cities
top_cities = (
    filtered_df.groupby("billing_city", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
    .head(10)
    .sort_values("revenue", ascending=True)
)

fig_city = px.bar(
    top_cities,
    x="revenue",
    y="billing_city",
    orientation="h",
    title="🏙️ Top 10 Cities by Revenue"
)

fig_city.update_layout(
    xaxis_title="Revenue ($)",
    yaxis_title="",
    showlegend=False
)

fig_city.update_traces(
    hovertemplate="$%{x:,.2f}<extra></extra>"
)

col2.plotly_chart(fig_city, use_container_width=True)


# -----------------------------
# Data Preview
# -----------------------------
with st.expander("📋 View Combined Data"):
    st.dataframe(filtered_df, use_container_width=True)
# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("🎵 Music Store Analytics | Built with Python, Pandas & Streamlit")
st.caption("Music Store Sales Dashboard - Created by Hira Sulaiman")
