import modules.Questions
import modules.Answer
import modules.Rectangles
import modules.Circles
import modules.Triangles

def main_function():
  loop_running = True

  while loop_running:
    modules.Questions.print_questions()
    answer = int(modules.Answer.get_answer_for_shape())

    if modules.Answer.errors_found(answer):
      print()
      print(str(answer) + " is not a proper answer. Please try again.")
      continue

    if answer == 1:
      print(modules.Rectangles.Rectangle_run())
      
    elif answer == 2:
      print(modules.Circles.Circle_run())

    elif (answer == 3) or (answer == 4):
      print(modules.Triangles.Triangle_run(answer))

    elif answer == 5:
      print()
      print('Bye!')
      print()
      loop_running = False  # Ending loop
      
    else:
      # Unknow error
      print()
      print("Unknow error. Please try again.")