import matplotlib.pyplot as plt
import pandas as pd

# Your data
data = {
    'Country': [
        "Nigeria", "Congo", "Uganda", "Mozambique", "Angola",
        "Burkina Faso", "Mali", "Tanzania", "Niger", "Cote d’Ivore",
        "Cameroon", "Ghana", "Benin", "Ethiopia", "Malawi",
        "Guinea", "Chad", "Zambia", "Kenya", "Burundi",
        "Rwanda", "Central African Republic", "Madagascar", "South Sudan", "Sierra Leone"
    ],
    'GDP per Capita': [
        2163, 653, 964, 558, 3000,
        830, 833, 1192, 585, 2486,
        1563, 2203, 1302, 1027, 645,
        1515, 716, 1456, 2099, 259,
        966, 427, 516, 1071, 475
    ],
    'Malaria Cases': [
        24.96, 21.58, 15.342, 11.331, 7.156,
        11.567, 3.379, 6.015, 4.378, 4.98,
        2.975, 5.88, 2.632, 1.848, 7.17,
        2.009, 1.89, 5.36, 6.875, 4.732,
        2.043, 1.981, 1.95, 1.805, 1.223
    ]
}

df = pd.DataFrame(data)
df['GDP per Capita'] = df['GDP per Capita'] / 1000
fig, ax1 = plt.subplots(figsize=(14, 6))

malaria_bars = ax1.bar(df.index - 0.2, df['Malaria Cases'], width=0.3, color='red', label='Malaria Cases (in millions)')
ax2 = ax1.twinx()
gdp_bars = ax2.bar(df.index + 0.2, df['GDP per Capita'], width=0.5, color='blue', label='GDP per Capita')

# Reference lines for EU and US gdp/capita
gdp_eu, gdp_us = 56, 80
ax2.axhline(y=gdp_eu, color='blue', linestyle='--', label='EU GDP per capita')
ax2.axhline(y=gdp_us, color='purple', linestyle='--', label='US GDP per capita')

# Axis labels, title, and legends
ax1.set_xticks(df.index)
ax1.set_xticklabels(df['Country'], rotation=75)
ax1.set_ylabel('Malaria Cases (in millions)', color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax2.set_ylabel('GDP per Capita ($1000)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Combined legend
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper right', bbox_to_anchor=(1, 0.95))
plt.title('Malaria cases in most affected countries with reference to EU & US GDP per capita')
plt.tight_layout()
plt.show()