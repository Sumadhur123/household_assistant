import xml.etree.ElementTree as ET
import os
#See sample xml file for reference
def parse_annotation(ann_dir, img_dir, labels=[], x_ratio =1, y_ratio = 1):
    all_imgs = []
    seen_labels = {}
    
    for ann in sorted(os.listdir(ann_dir)):
        img = {'object':[]}

        tree = ET.parse(ann_dir + ann)
        
        for elem in tree.iter():
            if 'filename' in elem.tag:
                img['filename'] = img_dir + elem.text
            if 'width' in elem.tag:
                img['width'] = int(elem.text)
            if 'height' in elem.tag:
                img['height'] = int(elem.text)
            if 'object' in elem.tag or 'part' in elem.tag:
                obj = {}
                
                for attr in list(elem):
                    if 'name' in attr.tag:
                        obj['name'] = attr.text

                        if obj['name'] in seen_labels:
                            seen_labels[obj['name']] += 1
                        else:
                            seen_labels[obj['name']] = 1
                        
                        if len(labels) > 0 and obj['name'] not in labels:
                            break
                        else:
                            img['object'] += [obj]
                            
                    if 'bndbox' in attr.tag:
                        for dim in list(attr):
                            if 'xmin' in dim.tag:
                                obj['xmin'] = int(round(float(dim.text))*x_ratio)
                            if 'ymin'  in dim.tag:
                                obj['ymin'] = int(round(float(dim.text))*y_ratio)
                            if 'xmax' in dim.tag:
                                obj['xmax'] = int(round(float(dim.text))*x_ratio)
                            if 'ymax' in dim.tag:
                                obj['ymax'] = int(round(float(dim.text))*y_ratio)

        if len(img['object']) > 0:
            all_imgs += [img]
                        
    return all_imgs, seen_labels

LABELS = ['person','car','bike','pole','stairs','fence','dustbin','bus','truck','tree'] # array containing labels. Can be more than one.
train_image_folder = r'C:\Users\sumov\OneDrive\Desktop\Data\\'
train_annot_folder = r'C:\Users\sumov\OneDrive\Desktop\folder1\\'

train_imgs, seen_train_labels = parse_annotation(train_annot_folder, train_image_folder, labels=LABELS,)

label_ids = seen_train_labels.copy()
#labels_ids = {'person': 'person'}

train_imgs #Checking data format

f = open ('labels1.csv', 'w+')
for img_number in range(0,len(train_imgs)):
    image = train_imgs[img_number]
    im_name = image['filename'].split('/')[-1]
    objects = image['object']
    # print (im_name)
#     line = im_name
    for objs in objects:
        xmin = objs['xmin']
        ymin = objs['ymin']
        xmax = objs['xmax']
        ymax = objs['ymax']
        c_id = objs['name']
#         print (xmin, ymin, xmax, ymax, c_id)
        line = im_name+','+str(xmin)+',' +str(ymin)+',' +str(xmax)+','+str(ymax)+','+ str(c_id) +'\n'
        f.write (line)

  #  print (line)
    
f.close()

