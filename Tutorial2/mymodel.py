
## this example file shows how to submit the custom model for HW2 (if you use one)

import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.layer1 = nn.Linear(29,100)
        self.activation = nn.ReLU()
        self.layer2 = nn.Linear(102,2)
        
    def forward(self, x_cat,x_cont):
        
        
        batch_sz = cont_x.shape[0]
        
        
        return torch.stack((5*torch.ones(batch_sz,requires_grad=True),torch.zeros(batch_sz,requires_grad=True)),dim=1)