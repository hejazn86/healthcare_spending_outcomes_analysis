
# 🩺 EU Healthcare Spending & Health Outcomes Dashboard

A data analytics project exploring the relationship between healthcare spending and health outcomes—**life expectancy** and **mortality rate**—across Europe (2012–2022).

## 📁 Project Structure


health_dashboard_project/
│
├── data/
│   ├── raw/
│   │   ├── eu_health_expending.csv
│   │   ├── life_expectancy.csv
│   │   └── mortality_rate.csv
│   └── cleaned/
│       ├── Cleaned_health_spending.csv
│       ├── Cleaned_life_expectancy.csv
│       ├── Cleaned_mortality_rate.csv
│       └── merged_eu_health_data.csv  
│
├── Scripts/
│   ├── dashboard.py           # Streamlit dashboard app
│   └── requirements.txt       # Python dependencies  
│
├── notebooks/
│   ├── explore_and_analyse_data.ipynb 
│   └── 02_Statistical_analysis.ipynb         
│
│
└── README.md
```

---

## 💡 Project Goals

* Explore health spending trends in EU countries.
* Investigate how public health expenditure relates to **life expectancy** and **mortality rates**.
* Use statistical modeling and dashboards to derive and communicate insights.

---

## 📊 Dashboard Features

🚀 [Live Streamlit App](https://eu-healthcare-spending-analysis-dashboard.streamlit.app)

* Explore life expectancy and mortality trends interactively
* Filter by country and year
* Visualize spending vs. outcome relationships

---

## 🔍 Key Research Questions

* How does **public health spending** influence **life expectancy**?
* Are there disparities by **gender** and **age group**?
* What are the **temporal patterns** in EU healthcare spending and outcomes?

---

## 🧪 Methods & Statistical Analysis

We used **Ordinary Least Squares (OLS)** regression to quantify the impact of spending, gender, age class, and year on life expectancy.

**Model Specification**:

```text
Life Expectancy ~ Spending + Gender + Age Class + Year
```

### ➕ Handling Categorical Variables

Both `Gender` and `Age Class` were encoded using `pandas.get_dummies()` with `drop_first=True`:

* **Gender**:

  * Categories: `F`, `M`, `T` → Dummy Variables: `Gender_M`, `Gender_T`
  * Reference group: `Gender_F` (Female)

* **Age Class**:

  * Categories: `Less than 1 year`, `1 year`, `2 years`, `3 years`, `4 years`
  * Dummy Variables: `Age Class_2 years`, `Age Class_3 years`, `Age Class_4 years`, `Age Class_Less than 1 year`
  * Reference group: `1 year`

> ✅ This avoids the dummy variable trap and enables clear interpretation of coefficients relative to a baseline.

---

### 📈 Key Regression Findings

* **Spending**: Significantly associated with **longer life expectancy**, even after controlling for gender, age, and year.
* **Gender**:

  * `Male` reduces life expectancy by \~5.5 years compared to `Female`.
  * `Transgender` has a negative but smaller, non-significant effect.
* **Age Class**:

  * All groups under 5 years have significantly **lower** life expectancy (as expected) compared to 1-year-olds.
* **Year**:

  * Slight negative trend, possibly due to demographic changes or data artifact.
* **Multicollinearity**: Variance Inflation Factor (VIF) scores were all below **2.01**, indicating no severe multicollinearity.

---

## 🧰 Technologies Used

* **Python**: `pandas`, `statsmodels`, `seaborn`, `matplotlib`
* **Streamlit**: Interactive dashboard app
* **Plotly**: Dynamic data visualization

---

## 🔮 Future Work

* Model interaction effects between spending & gender/age
* Explore **panel regression**, **mixed models** or **hierarchical/multilevel models**
* Include **socioeconomic covariates** (GDP, education, urbanization, etc.)
* Improve outlier detection & time lag analysis
* Extend analysis to post-COVID trends

---

## ▶️ How to Run Locally

```bash
# Install dependencies
pip install -r Scripts/requirements.txt

# Launch Streamlit dashboard
streamlit run Scripts/dashboard.py
```

---

## 🌐 Links

* 📊 **[Live Streamlit Dashboard](https://eu-healthcare-spending-analysis-dashboard.streamlit.app)**
* 📁 Final dataset: `data/cleaned/merged_eu_health_data.csv`
* 📓 Main notebooks:

  * `explore_and_analyse_data.ipynb`
  * `02_Statistical_analysis.ipynb`


