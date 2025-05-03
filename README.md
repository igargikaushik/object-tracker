# Real Time Object Tracking
modified vers. of  [kcg2015](https://github.com/kcg2015/Vehicle-Detection-and-Tracking)
### -to track multiple objects in real time and organized into classes for easier usage in other packages, tracking algorithm used here is a simple Kalman Filter.

To incorporate the tracking into own project,  assume- to hv the o/p bounding boxes using a prebuilt model such as Faster R-CNN or SSD. the [Tensorflow Object Detection Model Zoo] (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/) for details.

**Run the session. Output bounding boxes**
First, run  model and output the bounding boxes as well as additional information.
```
[bounding_boxes, scores, class_labels,num_detections] = sess.run(
              [boxes, scores, classes, num_detections],
               feed_dict={image_tensor: image_np_expanded})
```


**Feed the output into the tracking pipeline.**
The tracking pipeline automatically runs the Kalman filter and returns the updated set of bounding boxes.
```
[bounding_boxes, scores, class_labels,num_detections,
img] = global_tracker.pipeline(bounding_boxes,
                             scores,
                             class_labels,
                             image_np,
                             score_thresh=0.5)
```
**Display the tracking in real time.**
```
while True:
    if bounding_boxes != ():    
        output_frame = vis_util.visualize_boxes_and_labels_on_image_array(
          img,
          bounding_boxes,
          class_labels.astype(np.int32),
          scores,
          category_labels,
          use_normalized_coordinates=True,
          line_thickness=3,
          min_score_thresh=0.1)
    cv2.imshow('frame', output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        done = True
        break
```   

### changes from [org. vehicle detection and tracking repo](https://github.com/kcg2015/Vehicle-Detection-and-Tracking).
- detector.py: able to detect all classes above a threshold 'score_thresh' (default value of 0.3) defined in 'get_localization'.
          The get_localization function also returns an 'idx_vector' containing an array of indices for which the localization process is detected. This is useful for mapping the bounding boxes to it's corresponding classes and scores so it can be plotted on the image.
  -renamed 'main.py' to 'main_tracker' and made it into a class named 'GlobalTracker()'/ can call this directly.
    - added a input argument to pass the maximum number of trackings that can be performed at any given time. with 'MAX_TRACKERS'
    - modified the 'pipeline' function to return an array of [_boxes, out_scores_arr, out_classes_arr, img]      
