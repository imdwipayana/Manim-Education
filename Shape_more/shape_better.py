from manim import *

SCALE = 2
FONT = 64
# COLOR=BLUE, GREEN, RED, YELLOW, ORANGE, PURPLE, PINK, TEAL, GOLD

class Shapes(Scene):
    def construct(self):
        # --- Square ---
        square = Square(color=BLUE).scale(SCALE)
        square_text = Text("SQUARE", font_size= FONT, color=BLUE).next_to(square, DOWN)

        self.play(Create(square), Write(square_text))
        self.wait(2)
        self.play(FadeOut(square), FadeOut(square_text))

        # --- Triangle ---
        triangle = Triangle(color=GREEN).scale(3)
        triangle_text = Text("TRIANGLE", font_size= FONT, color=GREEN).next_to(triangle, DOWN)

        self.play(Create(triangle), Write(triangle_text))
        self.wait(2)
        self.play(FadeOut(triangle), FadeOut(triangle_text))

        # --- Rectangle ---
        rectangle = Rectangle(width=8, height=4, color=RED)  # already large
        rectangle_text = Text("RECTANGLE", font_size= FONT, color=RED).next_to(rectangle, DOWN)

        self.play(Create(rectangle), Write(rectangle_text))
        self.wait(2)
        self.play(FadeOut(rectangle), FadeOut(rectangle_text))

        # --- Circle ---
        circle = Circle(color=YELLOW).scale(3)
        circle_text = Text("CIRCLE", font_size= FONT, color=YELLOW).next_to(circle, DOWN)

        self.play(Create(circle), Write(circle_text))
        self.wait(2)
        self.play(FadeOut(circle), FadeOut(circle_text))

        # --- Ellipse ---
        ellipse = Ellipse(width=10, height=5, color=ORANGE)
        ellipse_text = Text("ELLIPSE", font_size= FONT, color=ORANGE).next_to(circle, DOWN)

        self.play(Create(ellipse), Write(ellipse_text))
        self.wait(2)
        self.play(FadeOut(ellipse), FadeOut(ellipse_text))

        # --- Pentagon ---
        pentagon = RegularPolygon(5, color=PURPLE).scale(3)
        pentagon_text = Text("PENTAGON", font_size= FONT, color=PURPLE).next_to(circle, DOWN)

        self.play(Create(pentagon), Write(pentagon_text))
        self.wait(2)
        self.play(FadeOut(pentagon), FadeOut(pentagon_text))

        # --- Hexagon ---
        hexagon = RegularPolygon(6, color=PINK).scale(3)
        hexagon_text = Text("HEXAGON", font_size= FONT, color=PINK).next_to(circle, DOWN)

        self.play(Create(hexagon), Write(hexagon_text))
        self.wait(2)
        self.play(FadeOut(hexagon), FadeOut(hexagon_text))

        # --- Heptagon ---
        heptagon = RegularPolygon(7, color=TEAL).scale(3)
        heptagon_text = Text("HEPTAGON", font_size= FONT, color=TEAL).next_to(circle, DOWN)

        self.play(Create(heptagon), Write(heptagon_text))
        self.wait(2)
        self.play(FadeOut(heptagon), FadeOut(heptagon_text))

        # --- Octagon ---
        octagon = RegularPolygon(8, color=TEAL).scale(3)
        octagon_text = Text("OCTAGON", font_size= FONT, color=TEAL).next_to(circle, DOWN)

        self.play(Create(octagon), Write(octagon_text))
        self.wait(2)
        self.play(FadeOut(octagon), FadeOut(octagon_text))