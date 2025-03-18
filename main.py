from manim import *
import numpy as np


class WavePlot(Scene):
    def construct(self):
        # Define lists of x and y values
        x_values = np.linspace(-2*np.pi, 2*np.pi, 27)
        y_cvalues = np.cos(x_values)
        y_svalues = np.sin(x_values)
    

        # Create Axes
        axes = Axes(
            x_range=[-7, 7, 1],  # Start, End, Step
            y_range=[-1.5, 1.5, .5],
            axis_config={"color": WHITE},
        )
        xlabel = MathTex(r'x')
        ylabel = MathTex(r'y')
        # Label Axes
        labels = axes.get_axis_labels(x_label=xlabel, y_label=ylabel)

        # Convert (x, y) values into points in Manim's coordinate space
        cpoints = [axes.coords_to_point(x, y) for x, y in zip(x_values, y_cvalues)]

        # Create Dots
        cdots = VGroup(*[Dot(point, color=BLUE) for point in cpoints])

        # Create a smooth curve through the points
        cos_graph = axes.plot(lambda x: np.cos(x), color=YELLOW)

        # Convert (x, y) values into points in Manim's coordinate space
        spoints = [axes.coords_to_point(x, y) for x, y in zip(x_values, y_svalues)]

        # Create Dots
        sdots = VGroup(*[Dot(point, color=BLUE) for point in spoints])

        # Create a smooth curve through the points
        sin_graph = axes.plot(lambda x: np.sin(x), color=RED)

        # Show the elements with animations
        self.play(Create(axes), Write(labels))
        self.wait(1)

        self.play(Create(cdots), run_time=1.5)
        self.wait(0.5)

        self.play(Create(cos_graph), run_time=2)
        self.wait(2)

        self.play(Create(sdots), run_time=1.5)
        self.wait(0.5)

        self.play(Create(sin_graph), run_time=2)
        self.wait(2)

        tex = MathTex(r'LaTeX')
        self.add(tex)
        self.wait(2)

        #manim -pql main.py WavePlot
