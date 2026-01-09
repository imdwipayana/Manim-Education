from manim import *

class MakeTenWithSquares(Scene):
    def construct(self):
        # --- Title ---
        title = Text("How to Make 10", font_size=64, weight=BOLD, color=PURPLE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        square_size = 0.9

        for a in range(11):
            b = 10 - a

            # --- Create squares ---
            red_squares = VGroup(*[
                Square(side_length=square_size, fill_color=RED, fill_opacity=1)
                for _ in range(a)
            ]).arrange(RIGHT, buff=0.1)

            blue_squares = VGroup(*[
                Square(side_length=square_size, fill_color=BLUE, fill_opacity=1)
                for _ in range(b)
            ]).arrange(RIGHT, buff=0.1)

            red_squares.move_to(LEFT * 3)
            blue_squares.move_to(RIGHT * 3)

            # --- Plus sign ---
            plus = Text("+", font_size=72).move_to(
                midpoint(red_squares.get_right(), blue_squares.get_left())
                if a > 0 and b > 0 else ORIGIN
            )

            # --- Numbers ---
            red_number = MathTex(str(a), font_size=72, color=RED).next_to(red_squares, DOWN, buff=0.3)
            blue_number = MathTex(str(b), font_size=72, color=BLUE).next_to(blue_squares, DOWN, buff=0.3)

            # --- Show ---
            self.play(
                FadeIn(red_squares),
                FadeIn(blue_squares),
                FadeIn(plus),
                Write(red_number),
                Write(blue_number),
            )
            self.wait(0.5)

            # --- Combine ---
            combined = VGroup(red_squares, blue_squares)
            self.play(
                combined.animate.arrange(RIGHT, buff=0.1).move_to(ORIGIN),
                FadeOut(plus)
            )

            # --- Equation ---
            equation = MathTex(
                str(a), "+", str(b), "=", "10",
                font_size=86
            )
            equation.set_color_by_tex(str(a), RED)
            equation.set_color_by_tex(str(b), BLUE)
            equation.to_edge(DOWN)

            self.play(Write(equation))
            self.wait(1)

            # --- Clear before next pair ---
            self.play(
                FadeOut(combined),
                FadeOut(red_number),
                FadeOut(blue_number),
                FadeOut(equation)
            )

        self.wait(1)
