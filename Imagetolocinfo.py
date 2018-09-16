from watson_developer_cloud import VisualRecognitionV3
import json
import os
import getLatLong as geotag

#all photos must be stored in 'Photos' directory (same dir as code)

#tagged_images = [] #[(lat,long),roof_true probability, roof_false probability]
lats = []
longs = []
rt = []
rf = []

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='vFTSKJUVMqQs9h4mHY0wwqI9yPjYS6z1tbv_ZkCfV3SX')

def tag_photos():
    
    for file in os.listdir('Photos'):

        direc = 'Photos/' + file

        with open(direc, 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file,
                threshold='0.0',
                owners=["me"]).get_result()
                #classifier_ids=['default']).get_result()

            roof_false = classes['images'][0]['classifiers'][0]['classes'][0]['score']
            roof_true = classes['images'][0]['classifiers'][0]['classes'][1]['score']


        (lat,long) = geotag.getLatLong(direc)

        lats.append(lat)
        longs.append(long)
        rt.append(roof_true)
        rf.append(roof_false)
        #tagged_images.append([(lat,long),roof_true,roof_false])
        
    return(lats,longs,rt,rf)

print(tag_photos())

