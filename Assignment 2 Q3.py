import turtle

def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor, branch_width):
    if depth > 0:
        #set the branch color and width
        if depth == recursion_depth:
            turtle.color("red")
        else:
            turtle.color("green")
        turtle.width(branch_width)

        #draw the current branch
        turtle.forward(branch_length)

        #draw the left subtree
        turtle.left(left_angle)
        draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor, branch_width - 2)

        #draw the right subtree
        turtle.right(left_angle + right_angle)
        draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor, branch_width - 2)

        #return to the main trunk
        turtle.left(right_angle)
        turtle.penup()
        turtle.backward(branch_length)
        turtle.pendown()
        
def main():
    #set up the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Assignment 2 Q3 - Recursive Tree Pattern")

    #Get user input for parameters
    left_angle = int(screen.numinput("Input", "Enter the left branch angle: "))
    right_angle = int(screen.numinput("Input", "Enter the right branch angle: "))
    start_length = int(screen.numinput("Input", "Enter the starting branch length: "))
    global recursion_depth
    recursion_depth = int(screen.numinput("Input", "Enter the recursion depth: "))
    reduction_factor = float(screen.numinput("Input", "Enter the branch length reduction factor(e.g. 0.7): "))
    
    #Initializing the turtle
    turtle.speed("fastest")
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()

    #draw the tree
    draw_tree(start_length, left_angle, right_angle, recursion_depth, reduction_factor, 10)

    #finish drawing
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()