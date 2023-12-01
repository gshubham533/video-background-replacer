# pyvidbgreplacer

`pyvidbgreplacer` is a Python module that provides functions to replace the background of a video with an image using the Mediapipe library for selfie segmentation. This module can be useful for creating interesting video effects or virtual backgrounds in video conferencing.

## Installation

To use `pyvidbgreplacer`, follow these steps:

1. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary libraries, including `numpy`, `mediapipe`, and `opencv-python`.

## Usage

### Example

To run the example code, you can use the provided `example.py` file. Uncomment the relevant lines in the file based on your preference. The examples demonstrate how to replace the background using your webcam or a specified video file.

```python
from pyvidbgreplacer import replace_video_bg_with_image_ishow, replace_video_bg_with_image_save_output

background_image_path = 'resource/beach_bg.jpeg'

# To replace the video background using the webcam (press Esc to exit window)
# replace_video_bg_with_image_ishow(background_image_path)

# To replace the video background of a specific video file (press Esc to exit window)
# sample_video_path = 'resource/sample_video.mp4'
# replace_video_bg_with_image_ishow(background_image_path, sample_video_path)

# To save the output video with the replaced background
# output_path = 'video_bg_replaced_output.mp4'
# video_path_of_video_after_proccesing = replace_video_bg_with_image_save_output(background_image_path, sample_video_path, output_path)
```

### Documentation

#### `replace_video_bg_with_image_ishow(bg_img_path, video_path='')`

This function replaces the background of a video with the specified image in real-time using your webcam or a specified video file.

- `bg_img_path`: The path to the image file used as the background.
- `video_path`: (Optional) The path to the input video file. If not provided, the webcam will be used.

#### `replace_video_bg_with_image_save_output(bg_img_path, video_path, output_path)`

This function replaces the background of a video with the specified image and saves the output as a new video file.

- `bg_img_path`: The path to the image file used as the background.
- `video_path`: The path to the input video file.
- `output_path`: The path to save the output video.

## Run the Example

After installing the requirements, run the `example.py` file to see the module in action. Uncomment the relevant lines in the file based on your preferences.

```bash
python example.py
```

This will execute the chosen example and showcase the background replacement effect.

Feel free to experiment with different background images and video files to achieve the desired visual effects.