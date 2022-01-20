import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r'C:\Users\jcazarotto\Desktop\world-population-growth-analysis\growth_and_migration_population.csv')
tabela = tabela.drop(columns=['iso2c', 'region', 'adminregion', 'capitalCity', 'lendingType', 'longitude', 'latitude'])
print(tabela.info())
remove_aggregates = tabela['incomeLevel'] != 'Aggregates'
tabela = tabela[remove_aggregates]
tabela = tabela.dropna(subset=['incomeLevel'])
tabela = tabela.sort_values(by=['year'], ascending=True)
print(tabela)

fig = px.choropleth(tabela,                            # Input Dataframe
                     locations="iso3c",           # identify country code column
                     color="population",                     # identify representing column
                     hover_name="country",              # identify hover name
                     animation_frame="year",        # identify date column
                     projection="natural earth",        # select projection
                     color_continuous_scale = 'Reds',  # select prefer color scale
                     labels={"iso3c": 'ISO Code',
                             "year": 'Year',
                             "population": 'Population'},
                     range_color=[3000000,300000000] # select range of dataset
                     )
fig.update_layout(
    title_text = 'World Growth Population: 1960-2018',
    title_font_family = 'Arial',
    title_font_size = 30,
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = True,
    ))
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 20
fig.update_geos(resolution=110)

fig.show()
fig.write_html("example_map.html")
