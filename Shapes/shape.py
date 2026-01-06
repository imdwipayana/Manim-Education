from manim import *

class Shapes(Scene):
    def construct(self):
        # --- Square ---
        square = Square()
        square_text = Text("Square").next_to(square, DOWN)

        self.play(Create(square), Write(square_text))
        self.wait(1)
        self.play(FadeOut(square), FadeOut(square_text))

        # --- Triangle ---
        triangle = Triangle()
        triangle_text = Text("Triangle").next_to(triangle, DOWN)

        self.play(Create(triangle), Write(triangle_text))
        self.wait(1)
        self.play(FadeOut(triangle), FadeOut(triangle_text))

        # --- Rectangle ---
        rectangle = Rectangle(width=4, height=2)
        rectangle_text = Text("Rectangle").next_to(rectangle, DOWN)

        self.play(Create(rectangle), Write(rectangle_text))
        self.wait(1)
        self.play(FadeOut(rectangle), FadeOut(rectangle_text))

        # --- Circle ---
        circle = Circle()
        circle_text = Text("Circle").next_to(circle, DOWN)

        self.play(Create(circle), Write(circle_text))
        self.wait(2)
