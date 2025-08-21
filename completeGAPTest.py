import numpy as np
import torch
import torch.nn as nn


class SimpleAveragePool(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.globalAveragePoolLayer = nn.AdaptiveAvgPool2d((1, 1))
    
    def forward(self, x):
        return self.globalAveragePoolLayer(x)


class TestCase():
    def __init__(self, inputSize : tuple):
        self.__sampleNum, self.__channelNum, self.__height, self.__width = inputSize
        self.__model = SimpleAveragePool().eval()
    
    def generate(self):
        self.__inputs = torch.randn(self.__sampleNum, self.__channelNum, self.__height, self.__width, dtype=torch.float32)
        self.__outputs = self.__model(self.__inputs)
    

    def save(self, path):
        onnxFile = path + "network.onnx"
        inputFile = path + "inputs.npz"
        outputFile = path + "outputs.npz"

        torch.onnx.export(
            self.__model,
            self.__inputs,
            onnxFile,
            export_params=True,
            opset_version=13,
            do_constant_folding=True,
            input_names=["x"],
            output_names=["y"],
            dynamic_axes=None
        )
        np.savez(inputFile, x=self.__inputs.detach().cpu().numpy())
        np.savez(outputFile, y=self.__outputs.detach().cpu().numpy())

        return True



class GAPLayerTester():
    def __init__(self):
        pass