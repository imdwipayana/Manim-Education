from manim import *

class MakeTenWithSquares(Scene):
    def construct(self):
        # --- Title ---
        title = Text("How to Make 10", font_size=64, weight=BOLD, color=PURPLE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # --- Create squares ---
        square_size = 0.9

        red_squares = VGroup(*[
            Square(side_length=square_size, fill_color=RED, fill_opacity=1)
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.1)

        blue_squares = VGroup(*[
            Square(side_length=square_size, fill_color=BLUE, fill_opacity=1)
            for _ in range(6)
        ]).arrange(RIGHT, buff=0.1)

        red_squares.move_to(LEFT * 3)
        blue_squares.move_to(RIGHT * 3)

        # --- Animate appearance ---
        self.play(FadeIn(red_squares))
        self.play(FadeIn(blue_squares))
        self.wait(1)

        # --- Plus sign ---
        plus = Text("+", font_size=72)
        plus.move_to(
                    midpoint(
                    red_squares.get_right(),
                    blue_squares.get_left()
                    ))

        self.play(FadeIn(plus))
        self.wait(1)

        # --- Plus sign ---
        plus = Text("+", font_size=72)
        plus.move_to(
                midpoint(
                red_squares.get_right(),
                blue_squares.get_left()
                ))
        self.play(FadeIn(plus))
        self.wait(1)

        # --- Add numbers under squares ---
        red_number = MathTex("4", font_size=72, color=RED).next_to(red_squares, DOWN, buff=0.3)
        blue_number = MathTex("6", font_size=72, color=BLUE).next_to(blue_squares, DOWN, buff=0.3)
        self.play(Write(red_number), Write(blue_number))
        self.wait(0.5)

        # --- Move squares together and remove plus ---
        combined = VGroup(red_squares, blue_squares)
        self.play(
                combined.animate.arrange(RIGHT, buff=0.1).move_to(ORIGIN),
                FadeOut(plus)
                )
        self.wait(1)

        # --- Equation with colored numbers ---
        equation = MathTex("4", "+", "6", "=", "10", font_size=86)

        # Color numbers
        equation.set_color_by_tex("4", RED)
        equation.set_color_by_tex("6", BLUE)

        # Position under the combined squares
        #equation.next_to(combined, DOWN, buff=0.8)
        self.play(equation.animate.to_edge(DOWN))

        # Animate writing
        self.play(Write(equation))
        self.wait(2)


