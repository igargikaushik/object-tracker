# Real Time Object Tracking
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
