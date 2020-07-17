import cv2


def draw_boxes(image, boxes, scores, labels, colors, classes, annotations, id , image_id):
    for b, l, s in zip(boxes, labels, scores):
        class_id = int(l)
        class_name = classes[class_id]
    
        xmin, ymin, xmax, ymax = list(map(int, b))
        score = '{:.4f}'.format(s)

        annotations.append({'id':id, 'image_id':image_id, 'category_id':class_id+1,
                            'bbox':[xmin, ymin, xmax-xmin, ymax-ymin], "score":s})
        id += 1
    return id, annotations