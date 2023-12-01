from pyvidbgreplacer import replace_video_bg_with_image_ishow,replace_video_bg_with_image_save_output

background_image_path = 'resource/beach_bg.jpeg'
'''
If you don't provide the optional keyword argument 'video_path,' it will access your webcam and replace the video background. 

Press Esc to exit the window.

'''
test_replace_vide_bg  = replace_video_bg_with_image_ishow(background_image_path) 


'''
Uncomment the line below if you want to replace the video background of your own video. For now, I have provided a sample video path. 

Press Esc to exit the window.
'''
sample_video_path = 'resource/sample_video.mp4'
# test_replace_vide_bg  = replace_video_bg_with_image_ishow(background_image_path,sample_video_path) 


'''
Uncomment the line below to save the output file.
'''
output_path = 'video_bg_replaced_output.mp4'
# video_path_of_video_after_proccesing = replace_video_bg_with_image_save_output(background_image_path,sample_video_path,output_path)