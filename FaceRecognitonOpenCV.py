import PIL.Image
import PIL.ImageDraw
import face_recognition

img = face_recognition.load_image_file('/home/iustin/Desktop/face.jpg')

face_locations = face_recognition.face_locations(img)

number_of_faces = len(face_locations)
print("We found {} face(s) in this image.".format(number_of_faces))

pil_image = PIL.Image.fromarray(img)

for face_location in face_locations:
    top, left, bottom, right = face_location
    print("A face is detected at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

draw = PIL.ImageDraw.Draw(pil_image)
draw.rectangle([left, top, right, bottom], outline="green", width=10)

pil_image.show()