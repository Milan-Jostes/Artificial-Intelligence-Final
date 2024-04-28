
from CustomLanguage import basic
def run(text):
  result, error = basic.run('<stdin>', text)
  if error: print(error.as_string())

  else:
    print(type(result))
    print(type(result.as_normal()))
    return result.as_normal() #print(result)