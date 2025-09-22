import cv2
import torch
import numpy as np



def restore_image(input_path, output_path):
    image = cv2.imread(input_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype(np.float32) / 255.0
    tensor = torch.from_numpy(image).permute(2,0,1).unsqueeze(0) # HWC -> CHW
    restored_tensor = tensor.clone()
    restored_image = restored_tensor.squeeze(0).permute(1,2,0) #CHW -> HWC
    restored_image = (restored_image * 255).clip(0, 255).astype(np.uint8)
    restored_bgr = cv2.cvtColor(restored_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, restored_bgr)