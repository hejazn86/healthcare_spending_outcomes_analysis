# Required Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

fitted_data = pd.read_csv("C:/Users/39351/github/Eu_healthcare_spending_analysis/data/cleaned/fitted_data.csv")
ols_summary = joblib.load("C:/Users/39351/github/Eu_healthcare_spending_analysis/reports/ols_model.pkl")
glm_summary = joblib.load("C:/Users/39351/github/Eu_healthcare_spending_analysis/reports/glm_model.pkl")
mixed_summary = joblib.load("C:/Users/39351/github/Eu_healthcare_spending_analysis/reports/mix_model.pkl")


# ------------------------------ Page setup -------------------------------
st.set_page_config(page_title="Life Expectancy & Mortality Analysis", layout="wide")

st.title("📊 Life Expectancy & Mortality Analysis Dashboard")
st.markdown("This dashboard presents results from OLS, GLM, and Mixed Effects models.")


# ------------------------------- Section 1: Model Summaries -------------------------------
st.header("🔎 Model Summaries")

# Example placeholders – replace with your real summaries
ols_summary = "R² = 0.45, Robust SE applied, heteroscedasticity corrected"
glm_summary = "Pseudo R² (CS) = 0.2021, Pearson Chi²/df ≈ 0.36 → No strong overdispersion"
mixed_summary = "Random intercepts by country significant, variance explained at country level."

with st.expander("OLS Model"):
    st.write(ols_summary)

with st.expander("GLM Model"):
    st.write(glm_summary)

with st.expander("Mixed Effects Model"):
    st.write(mixed_summary)


# ------------------------------- Section 2: Random Effects Plot -------------------------------
st.header("🌍 Random Effects by Country")

# Extract random effects (group-specific intercepts)
rand_eff = mixed_summary.random_effects
rand_eff_df = pd.DataFrame(rand_eff).T   
rand_eff_df = rand_eff_df.reset_index()
rand_eff_df.columns = ["Country", "Random Intercept"]
# Sort by random intercept
rand_eff_sorted = rand_eff_df.sort_values("Random Intercept", ascending=False)
# Add a column for color
rand_eff_sorted["Effect Sign"] = rand_eff_sorted["Random Intercept"].apply(
    lambda x: "Positive" if x >= 0 else "Negative"
)

fig_rand = px.bar(rand_eff_sorted,
             x="Country",
             y="Random Intercept",
             color="Effect Sign",
             color_discrete_map={"Positive": "darkblue", "Negative": "darkred"},
             title="Random Intercepts by Country",
             labels={"Random Intercept": "Random Effect Value", "Country": "Country", 'Effect Sign':'Random Effect'})

fig_rand.update_layout(xaxis_tickangle=90)
# rand_eff_df = pd.DataFrame({
#     "Country": ["A", "B", "C", "D"],
#     "Random Intercept": [0.1, -0.05, 0.2, -0.1]
# })

# fig_rand = px.bar(rand_eff_df, x="Country", y="Random Intercept",
#                   title="Random Intercepts by Country")
st.plotly_chart(fig_rand, use_container_width=True)


# ------------------------------- Section 3: Predicted Mortality Plot -------------------------------
st.header("📈 Predicted Mortality Curves (GLM)")

# prediction data
spending_range = np.linspace(fitted_data.Spending_centered.min(), fitted_data.Spending_centered.max(), 100)
genders = ["F", "M", "T"]
year_mean = fitted_data.Year_centered.mean()

pred_data = pd.DataFrame([
    {"Spending_centered": s, "Gender": g, "Year_centered": year_mean}
    for g in genders for s in spending_range
])


pred_data["Predicted"] = glm_summary.predict(pred_data)

# Plot with Plotly
fig_pred = px.line(
    pred_data,
    x="Spending_centered",
    y="Predicted",
    color="Gender",
    title="Predicted log Mortality Rate by Spending and Gender (GLM)",
    labels={
        "Spending_centered": "Spending (centered)",
        "Predicted": "Predicted log Mortality Rate",
        "C(Gender)": "Gender"
    }
)

st.plotly_chart(fig_pred, use_container_width=True)


# ------------------------------- Section 4: Interactive Filter -------------------------------
st.header("🔧 Interactive Exploration")

gender_choice = st.selectbox("Select Gender", pred_data["C(Gender)"].unique())
subset = pred_data[pred_data["C(Gender)"] == gender_choice]

fig_subset = px.line(subset, x="Spending_centered", y="Predicted",
                     title=f"Predicted Mortality for Gender: {gender_choice}")
st.plotly_chart(fig_subset, use_container_width=True)


# ------------------------------- Footer -------------------------------
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit & Plotly.")
