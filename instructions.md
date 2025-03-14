# Turtle Graphics Guessing Game
Create a simple guessing game utilizing the Turtle graphics library. This game will compare the player’s guess to a generated random number and will draw shapes and write text on the turtle screen accordingly.

# Instructions
1. **Import Libraries**
   Import the turtle and random libraries.
   ```python
   import turtle
   import random
   ```
   
2. **Generate Random Number**
   Generate a random number between 1 and 10 and store it in a variable.
   ```python
   random_number = random.randint(1, 10)
   ```

3. **Player’s Guess**
   Use the turtle library to get the player’s guess and check if the guess is correct.
   ```python
   guess = int(turtle.textinput("Guessing Game", "Guess a number between 1 and 10:"))
   ```

4. **Setup Turtle Screen**
   Set up the turtle screen with a title and background color.
   ```python
   screen = turtle.Screen()
   screen.title("Simple Guessing Game")
   screen.bgcolor("lightblue")
   ```

5. **Setup Turtle**
   Set up the turtle object and give it the fastest speed.
   ```python
   pen = turtle.Turtle()
   pen.speed(0)
   ```

6. **Player’s Input and Hints**
   Use the turtle library to receive player’s input and to return hints or messages depending on the guess.

7. **Define Drawing Functions**
   Define two functions, `draw_circle()` and `draw_cross()`, which will draw a circle and a cross, respectively, with the turtle object.
   ```python
   def draw_circle():
       # Logic to draw a circle
   
   def draw_cross():
       # Logic to draw a cross
   ```

8. **Define Writing Function**
   Define a function `write_text()` to write text on the screen with the specified message.
   ```python
   def write_text(text):
       pen.write(text, font=("Arial", 16, "normal"))
   ```

## Example
### Correct Output
```plaintext
The Turtle Screen displays the respective shape and message based on the player's guess compared to the generated random number.
```

## Hint
- Use `pen.penup()` and `pen.pendown()` to move the turtle without drawing.
- Utilize `pen.goto(x, y)` to position the turtle at specific coordinates on the screen before drawing or writing.
