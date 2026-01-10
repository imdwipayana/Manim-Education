from manim import *

class MakeTenWithSquares(Scene):
    def construct(self):
        # Title with animation
        title = Text("How to Make 10", font_size=64, weight=BOLD, gradient=(PURPLE, PINK))
        self.play(Write(title, run_time=1.5))
        self.play(title.animate.to_edge(UP), run_time=0.8)
        self.wait(0.3)

        square_size = 0.7
        
        for a in range(11):
            b = 10 - a
            
            # Create squares with rounded corners for better aesthetics
            red_squares = VGroup(*[
                RoundedRectangle(
                    corner_radius=0.1,
                    width=square_size, 
                    height=square_size,
                    fill_color=RED,
                    fill_opacity=0.9,
                    stroke_color=RED_E,
                    stroke_width=3
                )
                for _ in range(a)
            ]).arrange(RIGHT, buff=0.08)

            blue_squares = VGroup(*[
                RoundedRectangle(
                    corner_radius=0.1,
                    width=square_size,
                    height=square_size,
                    fill_color=BLUE,
                    fill_opacity=0.9,
                    stroke_color=BLUE_E,
                    stroke_width=3
                )
                for _ in range(b)
            ]).arrange(RIGHT, buff=0.08)

            # Positioning with better spacing
            if a == 0:
                blue_squares.move_to(ORIGIN + UP * 0.5)
            elif b == 0:
                red_squares.move_to(ORIGIN + UP * 0.5)
            else:
                gap = 1.5
                total_width = red_squares.get_width() + blue_squares.get_width() + gap
                red_squares.move_to(LEFT * (gap/2 + blue_squares.get_width()/2) + UP * 0.5)
                blue_squares.move_to(RIGHT * (gap/2 + red_squares.get_width()/2) + UP * 0.5)

            # Plus sign with glow effect
            plus = Text("+", font_size=72, color=YELLOW, weight=BOLD)
            if a > 0 and b > 0:
                plus.move_to(midpoint(red_squares.get_right(), blue_squares.get_left()))

            # Numbers below squares (show for non-zero groups)
            red_number = Text(str(a), font_size=60, color=RED, weight=BOLD)
            blue_number = Text(str(b), font_size=60, color=BLUE, weight=BOLD)

            if a > 0:
                red_number.next_to(red_squares, DOWN, buff=0.4)
            if b > 0:
                blue_number.next_to(blue_squares, DOWN, buff=0.4)

            # Animate squares appearing with stagger
            animations = []
            if a > 0:
                animations.append(LaggedStart(*[GrowFromCenter(sq) for sq in red_squares], lag_ratio=0.1))
                animations.append(FadeIn(red_number, shift=UP*0.2))
            if b > 0:
                animations.append(LaggedStart(*[GrowFromCenter(sq) for sq in blue_squares], lag_ratio=0.1))
                animations.append(FadeIn(blue_number, shift=UP*0.2))
            if a > 0 and b > 0:
                animations.append(GrowFromCenter(plus))
            
            self.play(*animations, run_time=1)
            self.wait(0.3)

            # Combine with smooth animation
            combined = VGroup(red_squares, blue_squares)
            target_pos = ORIGIN + UP * 0.5
            
            animations = [combined.animate.arrange(RIGHT, buff=0.08).move_to(target_pos)]
            if a > 0 and b > 0:
                animations.append(FadeOut(plus, scale=0.5))
            
            self.play(*animations, run_time=1)
            self.wait(0.2)

            # Equation with color-coded parts
            eq_parts = [str(a), "+", str(b), "=", "10"]
            equation = VGroup(*[Text(part, font_size=72, weight=BOLD) for part in eq_parts])
            equation.arrange(RIGHT, buff=0.2)
            
            equation[0].set_color(RED)      # a
            equation[1].set_color(YELLOW)   # +
            equation[2].set_color(BLUE)     # b
            equation[3].set_color(WHITE)    # =
            equation[4].set_color(GREEN)    # 10
            
            equation.to_edge(DOWN, buff=0.8)

            # Highlight the result with a background box
            box = SurroundingRectangle(equation[4], color=GREEN, buff=0.15, corner_radius=0.1)
            box.set_fill(GREEN, opacity=0.2)
            
            self.play(
                Write(equation),
                Create(box),
                run_time=1
            )
            self.wait(0.8)

            # Clear everything with smooth fadeout
            fadeout_items = [combined, equation, box]
            if a > 0:
                fadeout_items.append(red_number)
            if b > 0:
                fadeout_items.append(blue_number)
            
            self.play(
                FadeOut(VGroup(*fadeout_items), scale=0.8),
                run_time=0.8
            )
            self.wait(0.2)

        # Final message
        final_text = Text("All ways to make 10!", font_size=56, gradient=(GREEN, TEAL), weight=BOLD)
        final_text.move_to(ORIGIN)
        self.play(Write(final_text), run_time=1.5)
        self.wait(2)