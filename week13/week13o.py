
import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('mytest-08.png')

result = [r[1] for r in result]
result = " ".join(result)
print(result)



