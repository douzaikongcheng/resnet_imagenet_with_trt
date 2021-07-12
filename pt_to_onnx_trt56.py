import torchvision
import torch
from torch.autograd import Variable
import onnx
print(torch.__version__)

input_name = ['input']
output_name = ['output']
input = Variable(torch.randn(1, 3, 224, 224)).cuda()
model = torchvision.models.resnet18(pretrained=True).cuda()
torch.onnx.export(model, input, 'resnet18.onnx', input_names=input_name, output_names=output_name, verbose=True)
