# Import plotting library
import seaborn as sns

# Box plot
sns.boxplot(x="fuel_type_code_pudl", y="utility_id_ferc1",
            palette=["m", "g"], data=fuel_data)
# KDE plot 
sns.kdeplot(sample_df['fuel_cost_per_unit_burned'], shade=True, color="b")
