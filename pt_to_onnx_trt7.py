import torchvision
import torch
from torch.autograd import Variable
import onnx
print(torch.__version__)

input_name = ['input']
output_name = ['output']
batch_size = 1  # batch_size设1或其它都可以
input = Variable(torch.randn(batch_size, 3, 224, 224), requires_grad=False).cuda()
model = torchvision.models.resnet18(pretrained=True).cuda()
torch.onnx.export(model, input, 'resnet18.onnx', input_names=input_name, output_names=output_name, verbose=True
)





