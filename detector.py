'''
 to return the locatn of bounding boxes that r above a given threshold.
'''

import numpy as np

class Detector(object):
    def __init__(self):
        self.boxes = []

    # Helper function to convert image into numpy array
    def load_image_into_numpy_array(self, image):
         (im_width, im_height) = image.size
         return np.array(image.getdata()).reshape(
            (im_height, im_width, 3)).astype(np.uint8)
    # Helper function to convert normalized box coordinates to pixels
    def box_normal_to_pixel(self, box, dim):

        height, width = dim[0], dim[1]
        box_pixel = [int(box[0]*height), int(box[1]*width), int(box[2]*height), int(box[3]*width)]
        return np.array(box_pixel)

    def get_localization(self,boxes,scores, classes, image):
        """determines locatn of classes in the image.

        Args:
            boxes: bounding boxes detected.
            scores: scores for the bounding boxes.
            classes: class index.

        Returns:
            list of bounding boxes: coordinates [y_up, x_left, y_down, x_right]
            idx_vec: indices of the boxes that were successfully detected.

        """
        idx_vec = []
        tmp_boxes=[]
        

        for idx, bb in enumerate(boxes):
            dim = image.shape[0:2]
            box = self.box_normal_to_pixel(bb, dim)
            tmp_boxes.append(box)
            idx_vec.append(idx)


        self.boxes = tmp_boxes

        return self.boxes,idx_vec