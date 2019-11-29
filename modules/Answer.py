def get_answer_for_shape():
  answer = input("Choose the shape by selecting a number: ")
  return answer

def errors_found(ans):
  if (ans < 1) or ans > 5:
    return True
  return False