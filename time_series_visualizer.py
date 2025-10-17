import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Limpiar los datos: eliminar los 2,5% superior e inferior
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)
df = df[(df['value'] >= lower) & (df['value'] <= upper)]


def draw_line_plot():
    # Usar una copia de los datos
    df_line = df.copy()

    plt.figure(figsize=(12,6))
    plt.plot(df_line.index, df_line['value'], color='red', linewidth=1)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    plt.savefig("line_plot.png")
    return plt.gcf()


def draw_bar_plot():
    # Usar copia de los datos
    df_bar = df.copy()
    # Extraer año y mes
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Agrupar por año y mes y calcular promedio
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Meses para las etiquetas
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Dibujar gráfico de barras
    fig = df_grouped.plot(kind='bar', figsize=(12,6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=months)

    plt.savefig("bar_plot.png")
    return plt.gcf()


def draw_box_plot():
    # Usar copia de los datos
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    # Ordenar por número de mes para que Jan, Feb... estén en orden
    df_box = df_box.sort_values('month_num')

    fig, axes = plt.subplots(1,2, figsize=(18,6))

    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.savefig("box_plot.png")
    return plt.gcf()
