import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

ipr_concat = '/Users/macvbookpro/PycharmProjects/miuul/output/data/ipr_concat.csv'
out_file = '/Users/macvbookpro/PycharmProjects/miuul/output/data/ipr_purpleexclusiveheatmap.png'

def plot_heatmap(df):
    sns.set_style('whitegrid', {'axes.grid': False})
    plt.figure(figsize=(20,10))

    #create the heatmap
    ax= sns.heatmap(df,


                    #cmap=sns.color_palette("rocket_r", as_cmap=True)
                    cmap=sns.color_palette("ch:s=-.2,r=.6", as_cmap=True),
                    square=True,
                    fmt='g',
                    linewidths=.4,
                    annot=True,
                    cbar_kws={'shrink': .5},
                    annot_kws={'size': 5}) #adjust font size of annotations here

    plt.savefig(out_file, format='png', bbox_inches='tight', dpi=800)
    return plt.show()

#count ipr for each family
df = pd.read_csv(ipr_concat, header='infer', sep='\t')
df_ipr = df.groupby(['ipr', 'sp']).size().reset_index().sort_values(by=[0], ascending=False)
df_ipr = df_ipr.rename(columns={0: 'count'})[:50]

df_pivot = df_ipr.pivot(index='ipr', columns='sp', values='count').fillna(0)
df_transpose = df_pivot.transpose()

plot_heatmap(df_transpose)




