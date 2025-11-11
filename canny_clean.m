function img_clean = canny_clean(img_canny,threshold_area)
    img_bw = img_canny;

    % Detecting individual components
    cc = bwconncomp(img_bw,8);             % connectivity=8
    num_of_objects = cc.NumObjects;
    % disp("No of objects(un-filtered Image) = "+string(num_of_objects))
    
    % Calculating areas
    properties = regionprops(img_bw,"Area","PixelIdxList");
    all_area = [properties.Area];

    % Filter image
    img_bw_filtered = false(size(img_bw));  % An empty binary mask
    
    % Loop through each connected component and keep only the large ones
    for i = 1:num_of_objects
        if all_area(i) > threshold_area    
            img_bw_filtered(properties(i).PixelIdxList) = true;
        end
    end
    cc_new = bwconncomp(img_bw_filtered,8);
    img_clean = img_bw_filtered;
    % disp("No of objects (filtered image) = "+string(cc_new.NumObjects))
end