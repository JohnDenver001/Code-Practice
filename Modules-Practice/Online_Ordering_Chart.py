import turtle

screen = turtle.Screen()
screen.title("Online Order Processing Flowchart")
screen.setup(width=1200, height=800)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

def draw_circle(x, y, text, radius=40, color="black", fill="white"):
    pen.up()
    pen.goto(x, y - radius)
    pen.down()
    pen.color(color, fill)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.up()
    pen.goto(x, y - 10)
    pen.write(text, align="center", font=("Arial", 12, "bold"))

def draw_double_circle(x, y, text, radius=40, color="black", fill="white"):
    draw_circle(x, y, "", radius+5, color, fill)
    draw_circle(x, y, text, radius, color, fill)

def draw_rectangle(x, y, w, h, text, color="black", fill="white"):
    pen.up()
    pen.goto(x - w//2, y + h//2)
    pen.color(color, fill)
    pen.down()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w)
        pen.right(90)
        pen.forward(h)
        pen.right(90)
    pen.end_fill()
    pen.up()
    pen.goto(x, y - 10)
    pen.write(text, align="center", font=("Arial", 12, "normal"))

def draw_diamond(x, y, w, h, text, color="black", fill="white"):
    pen.color(color, fill)
    pen.up()
    pen.goto(x, y + h//2)
    pen.down()
    pen.begin_fill()
    pen.goto(x + w//2, y)
    pen.goto(x, y - h//2)
    pen.goto(x - w//2, y)
    pen.goto(x, y + h//2)
    pen.end_fill()
    pen.up()
    pen.goto(x, y - 10)
    pen.write(text, align="center", font=("Arial", 12, "normal"))

def draw_arrow(x1, y1, x2, y2):
    pen.color("black")
    pen.up()
    pen.goto(x1, y1)
    pen.down()
    pen.goto(x2, y2)
    pen.setheading(pen.towards(x2, y2))
    pen.right(20)
    pen.forward(10)
    pen.back(10)
    pen.left(40)
    pen.forward(10)
    pen.back(10)
    pen.right(20)

steps = {
    "start": (-400, 250),
    "browse": (-200, 150),
    "select": (50, 150),
    "add_to_cart": (300, 150),
    "checkout_decision": (450, -70),
    "yes": (300, 50),
    "no": (450, 250),
    "shipping_info": (30, 50),
    "payment_info": (-300, 50),
    "process_payment": (-300, -100),
    "payment_successful": (50, -100),
    "confirmed": (50, -250),
    "failed": (-300, -250),
    "done": (300, -250)
}

draw_circle(*steps["start"], "Start", color="black", fill="lightgray")
draw_rectangle(*steps["browse"], 150, 40, "Customer Browses", color="blue", fill="lightblue")
draw_rectangle(*steps["select"], 150, 40, "Select Item", color="blue", fill="lightblue")
draw_rectangle(*steps["add_to_cart"], 150, 40, "Add to Cart", color="blue", fill="lightblue")
draw_diamond(*steps["checkout_decision"], 160, 60, "Proceed to Checkout?", color="black", fill="lightgray")
draw_double_circle(*steps["yes"], "YES", color="black", fill="lightgreen")
draw_double_circle(*steps["no"], "NO", color="red", fill="mistyrose")
draw_rectangle(*steps["shipping_info"], 200, 40, "Enter Shipping Info", color="blue", fill="lightblue")
draw_rectangle(*steps["payment_info"], 200, 40, "Enter Payment Info", color="blue", fill="lightblue")
draw_rectangle(*steps["process_payment"], 200, 40, "Process Payment", color="green", fill="lightgreen")
draw_diamond(*steps["payment_successful"], 160, 60, "Payment Successful?", color="green", fill="lightgreen")
draw_double_circle(*steps["confirmed"], "Order Confirmed", color="black", fill="green")
draw_double_circle(*steps["failed"], "Payment Failed", color="red", fill="mistyrose")
draw_circle(*steps["done"], "Done", color="black", fill="green")

draw_arrow(-400, 210, -200, 170)  # start to browse
draw_arrow(-125, 150, -25, 150)   # browse to select
draw_arrow(125, 150, 225, 150)    # select to add_to_cart
draw_arrow(375, 150, 450, -40)    # add_to_cart to checkout_decision
draw_arrow(430, -50, 330, 30)     # checkout_decision to yes
draw_arrow(270, 50, 130, 50)      # yes to shipping_info
draw_arrow(470, -50, 450, 210)    # checkout_decision to no
draw_arrow(450, 210, -125, 170)   # no to browse
draw_arrow(-70, 50, -200, 50)     # shipping_info to payment_info
draw_arrow(-300, 30, -300, -70)   # payment_info to process_payment
draw_arrow(-200, -100, -30, -100) # process_payment to payment_successful
draw_arrow(130, -100, 50, -210)   # payment_successful to confirmed
draw_arrow(50, -130, -300, -210)  # payment_successful to failed
draw_arrow(-300, -200, -300, -130) # failed to process_payment
draw_arrow(50, -290, 300, -250)   # confirmed to done

turtle.done()
