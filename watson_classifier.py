from watson_developer_cloud import VisualRecognitionV3 as vr
import webbrowser
import time

# creating a VR instance

instance = vr(api_key='ff644e192cbf2fcd509165d85a7b053f360ca6a1', version='2016-05-20')

# select an image (local or url). Copy its location (path or url):

img = instance.classify(images_url='http://i.dailymail.co.uk/i/pix/2011/12/23/article-2077964-0CAA9E3A000005DC-263_468x319.jpg')

# you can run this code in the interpreter. If you request >>> img it will output a json formatted result
# getting down the json tree with the following input will display what Watson sees in the image, and the confidence level

# >>> img['images'][0]['classifiers'][0]['classes']

# for a better view of the results, you can use pprint
print "The output given by Watson \n"
print(img)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------- \n")

num_of_results= len(img['images'][0]['classifiers'][0]['classes'])
print "The output in a readable user-friendly way \n"
print("This image contains the following:")

for x in range(0, num_of_results):
   print img['images'][0]['classifiers'][0]['classes'][x]['class'],'with confidence level:' , img['images'][0]['classifiers'][0]['classes'][x]['score']

print("--------------------------------------------------------------------------------------------------------------------------------------------------------- \n")

print "To know more about the topic in the images. We will redirect you to a Wikipedia article, please wait for a couple of seconds"
time.sleep(20)
search_key_word = img['images'][0]['classifiers'][0]['classes'][0]['class']
webbrowser.open('en.wikipedia.org/w/index.php?search=' + search_key_word)


