from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

if __name__ == "__main__":
    print("Generando line plot...")
    draw_line_plot()
    print("Se guardó line_plot.png")

    print("Generando bar plot...")
    draw_bar_plot()
    print("Se guardó bar_plot.png")

    print("Generando box plot...")
    draw_box_plot()
    print("Se guardó box_plot.png")
