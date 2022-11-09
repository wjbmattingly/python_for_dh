import streamlit as st
import pandas as pd

# Cache our data
@st.cache()
def load_df():
    df = pd.read_csv("./data/titanic.csv")
    survival_options = df.Survived.unique()
    p_class_options = df.Pclass.unique()
    sex_options = df.Sex.unique()
    embark_options = df.Embarked.unique()


    min_fare = df.Fare.min()
    max_fare = df.Fare.max()

    min_age = df.Age.min()
    max_age = df.Age.max()

    return df, survival_options, p_class_options, sex_options, embark_options, min_fare, max_fare, min_age, max_age

def check_rows(column, options):
    return res.loc[res[column].isin(options)]

st.title("Demo DataFrame Query App")


df, survival_options, p_class_options, sex_options, embark_options, min_fare, max_fare, min_age, max_age = load_df()
res = df

name_query = st.text_input("String match for Name")

cols = st.columns(4)
survival = cols[0].multiselect("Survived", survival_options)
p_class = cols[1].multiselect("Passenger Class", p_class_options)
sex = cols[2].multiselect("Sex", sex_options)
embark = cols[3].multiselect("Embarked", embark_options)

range_cols = st.columns(3)
min_fare_range, max_fare_range = range_cols[0].slider("Lowest Fare", float(min_fare), float(max_fare),
                                        [float(min_fare), float(max_fare)])
min_age_range, max_age_range = range_cols[2].slider("Lowest Age", float(min_age), float(max_age),
                                        [float(min_age), float(max_age)])


if name_query != "":
    res = res.loc[res.Name.str.contains(name_query)]

if survival:
    res = check_rows("Survived", survival)
if p_class:
    res = check_rows("Pclass", p_class)
if sex:
    res = check_rows("Sex", sex)
if embark:
    res = check_rows("Embarked", embark)
if range_cols[0].checkbox("Use Fare Range"):
    res = res.loc[(res.Fare > min_fare_range) & (res.Age < max_fare_range)]
if range_cols[2].checkbox("Use Age Range"):
    res = res.loc[(res.Age > min_age_range) & (res.Age < max_age_range)]


st.header("Result")
removal_columns = st.multiselect("Select Columns to Remove", df.columns.tolist())
for column in removal_columns:
    res = res.drop(column, axis=1)
st.write(res)
