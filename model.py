import torch.nn as nn
from torchvision import models

class Network(nn.Module):
    def __init__(self, pretrained = True):
        super(Network, self).__init__()
        self.feature_extractor = models.vgg16(pretrained = pretrained).features
        self.classifier = nn.Sequential(
                nn.Linear(25088, 4096, bias = True),
                nn.ReLU(inplace = True),
                nn.Dropout(0.5),
                nn.Linear(4096, 4096, bias = True),
                nn.ReLU(inplace = True),
                nn.Dropout(0.5),
                nn.Linear(4096, 3, bias = True)
                )
        
    def forward(self, x):
        features = self.feature_extractor(x)
        features = features.view(features.shape[0], -1)
        return self.classifier(features)