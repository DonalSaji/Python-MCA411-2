
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Livestock Growth Analytics",
    layout="wide"
)

st.title("Livestock Growth & Weight Analytics")
st.caption("Interactive cattle growth and farm analytics dashboard")


# --------------------------------------------------
# DATASET LOADING
# --------------------------------------------------


# --------------------------------------------------
# LOAD DATASET DIRECTLY FROM KAGGLE
# --------------------------------------------------
@st.cache_data
def load_dataset():
    # Download the latest dataset version from Kaggle
    dataset_path = kagglehub.dataset_download(
        "muhammedfakl/livestock-growth-and-weight-prediction-dataset"
    )

    # Find CSV files in the downloaded dataset folder
    csv_files = list(Path(dataset_path).glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            "No CSV file was found in the downloaded Kaggle dataset."
        )

    # Load the first CSV file
    df = pd.read_csv(csv_files[0])

    return df


try:
    with st.spinner("Downloading/loading dataset from Kaggle..."):
        df = load_dataset()
except Exception as e:
    st.error("Unable to load the Kaggle dataset.")
    st.exception(e)
    st.stop()

st.success(f"Dataset loaded successfully: {len(df):,} records")



# --------------------------------------------------
# COLUMN DETECTION
# --------------------------------------------------

def find_column(names):
    for name in names:
        for column in df.columns:
            if column.lower().replace(" ", "_") == name.lower():
                return column
    return None

breed_col = find_column(["breed"])
sex_col = find_column(["sex"])
ration_col = find_column(["ration_type"])
birth_col = find_column(["birth_weight_kg"])
weight3_col = find_column(["weight_3m_kg"])
weight12_col = find_column(["weight_12m_kg"])
id_col = find_column(["animal_id", "cattle_id", "id"])


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Filter Cattle")

filtered_df = df.copy()

if breed_col:
    breeds = sorted(df[breed_col].dropna().unique())
    selected_breeds = st.sidebar.multiselect(
        "Select Breed",
        breeds,
        default=breeds
    )
    if selected_breeds:
        filtered_df = filtered_df[
            filtered_df[breed_col].isin(selected_breeds)
        ]

if sex_col:
    sexes = sorted(df[sex_col].dropna().unique())
    selected_sexes = st.sidebar.multiselect(
        "Select Sex",
        sexes,
        default=sexes
    )
    if selected_sexes:
        filtered_df = filtered_df[
            filtered_df[sex_col].isin(selected_sexes)
        ]

if ration_col:
    rations = sorted(df[ration_col].dropna().unique())
    selected_rations = st.sidebar.multiselect(
        "Select Ration",
        rations,
        default=rations
    )
    if selected_rations:
        filtered_df = filtered_df[
            filtered_df[ration_col].isin(selected_rations)
        ]


# --------------------------------------------------
# NAVIGATION TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Analysis",
    "Visualizations",
    "Insights"
])


# --------------------------------------------------
# TAB 1: OVERVIEW AND KPI
# --------------------------------------------------

with tab1:

    st.header("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Cattle",
        len(filtered_df)
    )

    if weight12_col:
        avg_weight = filtered_df[weight12_col].mean()
        col2.metric(
            "Average 12M Weight",
            f"{avg_weight:.2f} kg"
        )

    if birth_col:
        avg_birth = filtered_df[birth_col].mean()
        col3.metric(
            "Average Birth Weight",
            f"{avg_birth:.2f} kg"
        )

    if birth_col and weight12_col:
        gain = (
            filtered_df[weight12_col]
            - filtered_df[birth_col]
        ).mean()

        col4.metric(
            "Average Weight Gain",
            f"{gain:.2f} kg"
        )

    st.subheader("Dataset Information")

    st.write("Dataset Shape:", df.shape)
    st.write("Number of Columns:", len(df.columns))

    with st.expander("View Dataset"):
        st.dataframe(
            filtered_df,
            use_container_width=True
        )

    with st.expander("Missing Values"):
        st.dataframe(
            filtered_df.isnull().sum().to_frame("Missing Values")
        )


# --------------------------------------------------
# TAB 2: ANALYSIS
# --------------------------------------------------

with tab2:

    st.header("Dataset Analysis")

    if breed_col:

        st.subheader("Cattle Count by Breed")

        breed_counts = filtered_df[breed_col].value_counts()

        st.dataframe(
            breed_counts.to_frame("Cattle Count"),
            use_container_width=True
        )

    if ration_col:

        st.subheader("Cattle Count by Ration")

        ration_counts = filtered_df[ration_col].value_counts()

        st.dataframe(
            ration_counts.to_frame("Cattle Count"),
            use_container_width=True
        )

    if weight12_col:

        st.subheader("Weight Statistics")

        weights = filtered_df[weight12_col]

        statistics = pd.DataFrame({
            "Statistic": [
                "Total",
                "Average",
                "Minimum",
                "Maximum",
                "Median",
                "Standard Deviation"
            ],
            "Value": [
                weights.sum(),
                weights.mean(),
                weights.min(),
                weights.max(),
                weights.median(),
                weights.std()
            ]
        })

        st.dataframe(
            statistics,
            hide_index=True,
            use_container_width=True
        )


# --------------------------------------------------
# TAB 3: VISUALIZATIONS
# --------------------------------------------------

with tab3:

    st.header("Data Visualizations")

    col1, col2 = st.columns(2)

    # BAR CHART
    with col1:

        st.subheader("Average Weight by Breed")

        if breed_col and weight12_col:

            breed_weight = filtered_df.groupby(
                breed_col
            )[weight12_col].mean()

            fig, ax = plt.subplots()

            breed_weight.plot(
                kind="bar",
                ax=ax
            )

            ax.set_title("Average 12-Month Weight by Breed")
            ax.set_xlabel("Breed")
            ax.set_ylabel("Weight (kg)")
            ax.tick_params(axis="x", rotation=30)

            st.pyplot(fig)
            plt.close(fig)

    # LINE CHART
    with col2:

        st.subheader("Growth Progression")

        if birth_col and weight3_col and weight12_col:

            growth = [
                filtered_df[birth_col].mean(),
                filtered_df[weight3_col].mean(),
                filtered_df[weight12_col].mean()
            ]

            fig, ax = plt.subplots()

            ax.plot(
                ["Birth", "3 Months", "12 Months"],
                growth,
                marker="o"
            )

            ax.set_title("Average Cattle Growth")
            ax.set_xlabel("Growth Stage")
            ax.set_ylabel("Weight (kg)")
            ax.grid(True)

            st.pyplot(fig)
            plt.close(fig)

    # SCATTER CHART
    st.subheader("Birth Weight vs 12-Month Weight")

    if birth_col and weight12_col:

        fig, ax = plt.subplots()

        ax.scatter(
            filtered_df[birth_col],
            filtered_df[weight12_col]
        )

        ax.set_title("Birth Weight and Final Weight")
        ax.set_xlabel("Birth Weight (kg)")
        ax.set_ylabel("12-Month Weight (kg)")
        ax.grid(True)

        st.pyplot(fig)
        plt.close(fig)


# --------------------------------------------------
# TAB 4: INSIGHTS
# --------------------------------------------------

with tab4:

    st.header("Livestock Growth Insights")

    if not filtered_df.empty:

        if weight12_col:

            highest = filtered_df[weight12_col].idxmax()
            lowest = filtered_df[weight12_col].idxmin()

            if id_col:
                highest_id = filtered_df.loc[highest, id_col]
                lowest_id = filtered_df.loc[lowest, id_col]
            else:
                highest_id = highest
                lowest_id = lowest

            st.success(
                f"Highest Weight: "
                f"{filtered_df.loc[highest, weight12_col]} kg "
                f"(Animal ID: {highest_id})"
            )

            st.info(
                f"Lowest Weight: "
                f"{filtered_df.loc[lowest, weight12_col]} kg "
                f"(Animal ID: {lowest_id})"
            )

        if breed_col and weight12_col:

            breed_average = filtered_df.groupby(
                breed_col
            )[weight12_col].mean()

            best_breed = breed_average.idxmax()

            st.write(
                "Breed with highest average weight:",
                best_breed
            )

        if birth_col and weight12_col:

            average_gain = (
                filtered_df[weight12_col]
                - filtered_df[birth_col]
            ).mean()

            st.write(
                "Average Weight Gain:",
                round(average_gain, 2),
                "kg"
            )

        st.warning(
            "Dataset insights are educational and "
            "should not replace veterinary advice."
        )

    else:

        st.warning("No cattle records match the filters.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Regular Lab Exercise 6 | Q8 | "
    "Livestock Growth Analytics"
)
