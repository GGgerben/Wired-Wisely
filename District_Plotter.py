import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def df_generator(batteries_filepath, houses_filepath):
    with open(batteries_filepath) as batteries:
        battery_df = pd.read_csv(batteries)

        battery_df[['x', 'y']] = battery_df['positie'].str.split(',', expand=True).astype(int)

        battery_df = battery_df.drop(columns=['positie'])

        print(battery_df.head())

    with open(houses_filepath) as houses:
        house_df = pd.read_csv(houses)

        print(house_df.head())
    return battery_df, house_df

def plotter(battery_df, house_df):
    fig, ax = plt.subplots()
    sns.scatterplot(data=house_df, x='x', y='y', size='maxoutput', hue='maxoutput')
    sns.scatterplot(data=battery_df, x='x', y='y', color='red', marker='X', label='batteries', s=150)

    ax.set_title('House and Battery Locations')
    ax.set_xlabel('X coordinate')
    ax.set_ylabel('Y coordinate')
    ax.legend(bbox_to_anchor=(1, 1), borderaxespad=0.)
    ax.grid(True)
    return fig

battery_df, house_df = df_generator('Huizen&Batterijen/district_1/district-1_batteries.csv', 'Huizen&Batterijen/district_1/district-1_houses.csv')
fig1 = plotter(battery_df, house_df)

battery_df, house_df = df_generator('Huizen&Batterijen/district_2/district-2_batteries.csv', 'Huizen&Batterijen/district_2/district-2_houses.csv')
fig2 = plotter(battery_df, house_df)

battery_df, house_df = df_generator('Huizen&Batterijen/district_3/district-3_batteries.csv', 'Huizen&Batterijen/district_3/district-3_houses.csv')
fig3 = plotter(battery_df, house_df)

fig1.savefig('plot_1.png', dpi=300, bbox_inches='tight')
fig2.savefig('plot_2.png', dpi=300, bbox_inches='tight')
fig3.savefig('plot_3.png', dpi=300, bbox_inches='tight')
