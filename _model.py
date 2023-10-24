from PIL import Image
import torch
import gradio as gr

model2 = torch.hub.load(
    "AK391/animegan2-pytorch:main",
    "generator",
    pretrained=True,
    device="cuda",
    progress=False
)
model1 = torch.hub.load("AK391/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v1",  device="cuda")
face2paint = torch.hub.load(
    'AK391/animegan2-pytorch:main', 'face2paint', 
    size=512, device="cuda",side_by_side=False
)
def inference(img, ver):
    if ver == 'version 2 (🔺 robustness,🔻 stylization)':
        out = face2paint(model2, img)
    else:
        out = face2paint(model1, img)
    return out

# raw = Image.open("wp.png")
# v1 = inference(raw, 'v1')
# v2 = inference(raw, 'version 2 (🔺 robustness,🔻 stylization)')
# v1.save('v1.jpg')
# v2.save('v2.jpg')
