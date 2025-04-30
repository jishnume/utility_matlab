% video_file_path: this can be a filepath or the filename itself
function video_frame_export_function(video_file_path,show_video_prop,frame_indices)

% Reading the videofile
video_file = VideoReader(video_file_path);   % video_file_path: is a string variable


% Showing some of the essential video properties based on user's argument
if show_video_prop==true
    % video frame height
    video_frame_height = video_file.Height ;
    disp("Video frame height = "+string(video_frame_height)+" pixels")
    
    
    % video frame width
    video_frame_width = video_file.Width ;
    disp("Video frame width = "+string(video_frame_width)+" pixels")
    
    % Total number of frames
    tot_num_frame = video_file.NumFrames ;
    disp("Total number of frames = "+string(tot_num_frame))
    
    % Average Frame rate
    avg_frame_rate = video_file.FrameRate ;
    disp("Average frame rate = "+string(avg_frame_rate)+" frames per sec")
end

frame_vector=frame_indices;

for i=1:length(frame_indices)
    img=read(video_file,frame_vector(i));
    imwrite(img,"frame_"+string(frame_vector(i))+".png");
end

disp("Code is fully executed!!")
end