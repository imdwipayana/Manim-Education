from manim import *

SCALE = 2
FONT = 64
# COLOR=BLUE, GREEN, RED, YELLOW, ORANGE, PURPLE, PINK, TEAL, GOLD

class Shapes(ThreeDScene):
    def construct(self):
        # --- Square ---
        square = Square(color=BLUE, stroke_width=6).scale(SCALE)
        square_text = Text("SQUARE", font_size= FONT, color=BLUE).next_to(square, DOWN)

        self.play(Create(square), Write(square_text))
        self.wait(2)
        self.play(FadeOut(square), FadeOut(square_text))

        # --- Triangle ---
        triangle = Triangle(color=GREEN, stroke_width=6).scale(3)
        triangle_text = Text("TRIANGLE", font_size= FONT, color=GREEN).next_to(triangle, DOWN)

        self.play(Create(triangle), Write(triangle_text))
        self.wait(2)
        self.play(FadeOut(triangle), FadeOut(triangle_text))

        # --- Rectangle ---
        rectangle = Rectangle(width=8, height=4, color=RED, stroke_width=6)  # already large
        rectangle_text = Text("RECTANGLE", font_size= FONT, color=RED).next_to(rectangle, DOWN)

        self.play(Create(rectangle), Write(rectangle_text))
        self.wait(2)
        self.play(FadeOut(rectangle), FadeOut(rectangle_text))

        # --- Circle ---
        circle = Circle(color=YELLOW, stroke_width=6).scale(3)
        circle_text = Text("CIRCLE", font_size= FONT, color=YELLOW).next_to(circle, DOWN)

        self.play(Create(circle), Write(circle_text))
        self.wait(2)
        self.play(FadeOut(circle), FadeOut(circle_text))

        # --- Ellipse ---
        ellipse = Ellipse(width=10, height=5, color=ORANGE, stroke_width=6)
        ellipse_text = Text("ELLIPSE", font_size= FONT, color=ORANGE).next_to(circle, DOWN)

        self.play(Create(ellipse), Write(ellipse_text))
        self.wait(2)
        self.play(FadeOut(ellipse), FadeOut(ellipse_text))

        # --- Pentagon ---
        pentagon = RegularPolygon(5, color=PURPLE, stroke_width=6).scale(3)
        pentagon_text = Text("PENTAGON", font_size= FONT, color=PURPLE).next_to(circle, DOWN)

        self.play(Create(pentagon), Write(pentagon_text))
        self.wait(2)
        self.play(FadeOut(pentagon), FadeOut(pentagon_text))

        # --- Hexagon ---
        hexagon = RegularPolygon(6, color=PINK, stroke_width=6).scale(3)
        hexagon_text = Text("HEXAGON", font_size= FONT, color=PINK).next_to(circle, DOWN)

        self.play(Create(hexagon), Write(hexagon_text))
        self.wait(2)
        self.play(FadeOut(hexagon), FadeOut(hexagon_text))

        # --- Heptagon ---
        heptagon = RegularPolygon(7, color=TEAL, stroke_width=6).scale(3)
        heptagon_text = Text("HEPTAGON", font_size= FONT, color=TEAL).next_to(circle, DOWN)

        self.play(Create(heptagon), Write(heptagon_text))
        self.wait(2)
        self.play(FadeOut(heptagon), FadeOut(heptagon_text))

        # --- Octagon ---
        octagon = RegularPolygon(8, color=GOLD, stroke_width=6).scale(3)
        octagon_text = Text("OCTAGON", font_size= FONT, color=GOLD).next_to(circle, DOWN)

        self.play(Create(octagon), Write(octagon_text))
        self.wait(2)
        self.play(FadeOut(octagon), FadeOut(octagon_text))

        # --- Decagon ---
        decagon = RegularPolygon(10, color=BLUE, stroke_width=6).scale(3)
        decagon_text = Text("DECAGON", font_size= FONT, color=BLUE).next_to(circle, DOWN)

        self.play(Create(decagon), Write(decagon_text))
        self.wait(2)
        self.play(FadeOut(decagon), FadeOut(decagon_text))

        # --- Line ---
        line = Line(LEFT * 5 + DOWN, RIGHT * 5 + UP, color=GREEN, stroke_width=8)
        line_text = Text("LINE", font_size= FONT, color=GREEN).next_to(circle, DOWN)

        self.play(Create(line), Write(line_text))
        self.wait(2)
        self.play(FadeOut(line), FadeOut(line_text))

        # --- Arrow ---
        arrow = Arrow(LEFT * 4, RIGHT * 4, color=RED, stroke_width=8)
        arrow_text = Text("ARROW", font_size=FONT, color=RED).next_to(arrow, DOWN)

        self.play(Create(arrow), Write(arrow_text))
        self.wait(2)
        self.play(FadeOut(arrow), FadeOut(arrow_text))

        # --- Arc ---
        arc = Arc(radius=3, angle=(3*PI) / 4, color=YELLOW, stroke_width=8)
        arc_text = Text("ARC", font_size=FONT, color=YELLOW).next_to(arc, DOWN)

        self.play(Create(arc), Write(arc_text))
        self.wait(2)
        self.play(FadeOut(arc), FadeOut(arc_text))

        # --- Sphere ---
        sphere = Sphere(radius=2, color=ORANGE, fill_opacity=0.6)
        #sphere_text = Text("SPHERE", font_size=FONT, color=ORANGE).next_to(sphere, DOWN)

        ## --- Set camera orientation (IMPORTANT) ---
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # --- Text fixed on screen below sphere ---
        sphere_text = Text("SPHERE", font_size=FONT, color=ORANGE)
        self.add_fixed_in_frame_mobjects(sphere_text)  # Makes it 2D
        sphere_text.to_edge(DOWN)  # Place it at bottom of screen
        self.play(Write(sphere_text))

        ## --- Animate ---
        self.play(Create(sphere))
        self.play(Write(sphere_text))
        self.wait(2)
        self.play(FadeOut(sphere), FadeOut(sphere_text))


        # --- Cube ---
        cube = Cube(color=PURPLE, fill_opacity=0.6).scale(1.8)

        ## --- Set camera orientation (IMPORTANT) ---
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # --- Text fixed on screen below cube ---
        cube_text = Text("CUBE", font_size=FONT, color=PURPLE)
        self.add_fixed_in_frame_mobjects(cube_text)  # Makes it 2D
        cube_text.to_edge(DOWN)  # Place it at bottom of screen
        self.play(Write(cube_text))

        ## --- Animate ---
        self.play(Create(cube))
        self.play(Write(cube_text))
        self.wait(2)
        self.play(FadeOut(cube), FadeOut(cube_text))


        # --- Cylinder ---
        cylinder = Cylinder(color=PINK, fill_opacity=0.6).scale(1.8)

        ## --- Set camera orientation (IMPORTANT) ---
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # --- Text fixed on screen below cube ---
        cylinder_text = Text("CYLINDER", font_size=FONT, color=PINK)
        self.add_fixed_in_frame_mobjects(cylinder_text)  # Makes it 2D
        cylinder_text.to_edge(DOWN)  # Place it at bottom of screen
        self.play(Write(cylinder_text))

        ## --- Animate ---
        self.play(Create(cylinder))
        self.play(Write(cylinder_text))
        self.wait(2)
        self.play(FadeOut(cylinder), FadeOut(cylinder_text))


        # --- Cuboid ---
        cuboid = Prism(color=TEAL, fill_opacity=0.6).scale(1.8)

        ## --- Set camera orientation (IMPORTANT) ---
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # --- Text fixed on screen below cube ---
        cuboid_text = Text("Cuboid", font_size=FONT, color=TEAL)
        self.add_fixed_in_frame_mobjects(cuboid_text)  # Makes it 2D
        cuboid_text.to_edge(DOWN)  # Place it at bottom of screen
        self.play(Write(cuboid_text))

        ## --- Animate ---
        self.play(Create(cuboid))
        self.play(Write(cuboid_text))
        self.wait(2)
        self.play(FadeOut(cuboid), FadeOut(cuboid_text))


        # --- Triangular prism ---
        # --- Vertices of a triangular prism ---
        vertices = [
            [-1, -1, -2],
            [ 1, -1, -2],
            [ 0,  1, -2],  # triangle base (z = -2)
            [-1, -1,  2],
            [ 1, -1,  2],
            [ 0,  1,  2],  # triangle top (z = +2)
        ]

        # --- Faces: indices into vertices ---
        faces = [
            [0, 1, 2],  # base triangle
            [3, 4, 5],  # top triangle
            [0, 1, 4, 3],  # side rectangle 1
            [1, 2, 5, 4],  # side rectangle 2
            [2, 0, 3, 5],  # side rectangle 3
        ]

        # --- Create Polyhedron ---
        prism = Polyhedron(vertices, faces)
        prism.set_fill(GREEN, opacity=0.6)
        prism.set_stroke(BLACK, width=1)

        # --- Set camera orientation ---
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # --- Label below prism ---
        prism_text = Text("TRIANGULAR PRISM", font_size=FONT, color=GREEN)
        self.add_fixed_in_frame_mobjects(prism_text)
        prism_text.to_edge(DOWN)

        # --- Animate ---
        self.play(Create(prism))
        self.play(Write(prism_text))
        self.wait(2)
        self.play(FadeOut(prism), FadeOut(prism_text))


        # --- Cone ---
        cone = Cone(color=GOLD, fill_opacity=0.6).scale(3)

        ## --- Set camera orientation (IMPORTANT) ---
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # --- Text fixed on screen below cube ---
        cone_text = Text("CONE", font_size=FONT, color=GOLD)
        self.add_fixed_in_frame_mobjects(cone_text)  # Makes it 2D
        cone_text.to_edge(DOWN)  # Place it at bottom of screen
        self.play(Write(cone_text))

        ## --- Animate ---
        self.play(Create(cone))
        self.play(Write(cone_text))
        self.wait(2)
        self.play(FadeOut(cone), FadeOut(cone_text))

