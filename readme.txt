代码参考https://blog.csdn.net/qq_23116521/article/details/107617442

文件名后面的数字代表tensorrt的版本，tensorrt5，6和tensorrt7代码不一样

使用前请先安装tensorrt，onnx，pycuda


成功运行案例的结果
nano@nano-desktop:~/Desktop/trt$ python3 test_trt7.py 
Loading ONNX file from path resnet18.onnx...
Beginning ONNX file parsing
Completed parsing of ONNX file
Building an engine from file resnet18.onnx; this may take a while...
Completed creating Engine
TensorRT ok
Pytorch ok!
Inference time with the TensorRT engine: 0.10561108589172363
Inference time with the PyTorch model: 92.89923238754272
MSE Error = 3.784883864654809e-12
All completed!