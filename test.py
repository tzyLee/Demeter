import numpy as np
import cv2
import torch
from torchvision import transforms
from model import Network
import os
device = 'cuda' if torch.cuda.is_available() else 'cpu'

def load_model(path):
    net = Network(pretrained = False)
    net = net.to(device)
    net.load_state_dict(torch.load(path, map_location='cpu'))
    return net.eval()

def prepro_image(img):
    img = cv2.resize(img, (224, 224), interpolation = cv2.INTER_CUBIC)
    return (transforms.ToTensor()(img)).unsqueeze(0).to(device)

model_path = os.path.join('weights.ckpt')
quality_evaluator = load_model(model_path)

def inference(img):
   img = prepro_image(img)
   label = np.argmax(quality_evaluator(img).detach().cpu().numpy())
   return label
