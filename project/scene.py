from re import X
from manim import *
from matplotlib.pyplot import xlabel
from numpy import *

def f(x):
    return sqrt(x)

class Glib(Scene):

    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[0]),
            (top_right[0], bottom_left[0]),
        ]

    def construct(self):
        ax = Axes(
            x_range=[-3, 20],
            y_range=[0, 5],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": False, "include_numbers": True},
        )

        t = ValueTracker(10)
        k = 25

        graph = ax.plot(
            f,
            color=ORANGE,
            x_range=[0, 20, 0.1],
            use_smoothing=False,
        )
        labels = ax.get_axis_labels(x_label=Text("glib.var0",font_size=32), y_label=Text("glib.res0",font_size=32))

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (t.get_value(), f(t.get_value()))
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE_E, opacity=0.1)
            polygon.set_stroke(BLUE_E)
            return polygon

        polygon = always_redraw(get_rectangle)

        dot = Dot()
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), f(t.get_value()))))
        dot.set_z_index(10)

        self.add(ax, labels, graph, dot)
        self.play(Create(polygon))
        self.play(t.animate.set_value(0))
        self.play(t.animate.set_value(20))