import numpy as np
import torch
import torch.nn as nn
import sys
import os

from testUtils.testRunner import TestRunner, TestRunnerArgumentParser



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
    
    def inputs(self):
        return self.__inputs
    
    def outputs(self):
        return self.__outputs

    def save(self, path):
        onnxFile = path + "network.onnx"
        inputFile = path + "inputs.npz"
        outputFile = path + "outputs.npz"

        if not os.path.exists(path):
            os.makedirs(path)

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
    def __init__(self, seed : int = 0):
        self.__setSeed(seed)
        self.__currentTestCase : TestCase = None
    
    def __setSeed(self, seed):
        self.__seed = seed
        torch.manual_seed(self.__seed)
        np.random.seed(self.__seed)

    def generateTestCase(self, inputShape : tuple):
        self.__currentTestCase = TestCase(inputShape)
        self.__currentTestCase.generate()
    
    def singletest(self, inputShape : tuple, logIO : bool = False, path : str = None):
        self.generateTestCase(inputShape)
        
        if logIO:
            print("inputs : \n", self.__currentTestCase.inputs())
            print("outputs : \n", self.__currentTestCase.outputs())

        path = "Tests/GlobalAveragePool" if path is None else path
        self.__currentTestCase.save(path)
        
        print("Saved New Test case in path")


        argumentParser = TestRunnerArgumentParser(tiling_arguments=False, description="Arguments For a single testcase.")
        sys.argv = ["completeGAPTest.py", "-t", path]
        argumentParser.parse_args()

        testRunner = TestRunner(platform = "Generic", simulator = "host", tiling = False, argument_parser = argumentParser)

        try:
            testRunner.run()
        except RuntimeError as e:
            print("$$ ERROR OCCURED DURING TEST :", "\n", str(e))
            return False
        
        return True

    def MultipleTest(self, iterations : int, range_high = int, seed : int = 0, logIO : bool = False):
        if seed != self.__seed:
            self.__setSeed(seed)
        
        for i in range(iterations):
            print(f"###### Test No. {i} Started : ", end="")
            N, C, W, H = np.random.randint(low=0, high=range_high, size=4)
            inputShape = (N, C, W, H)
            print(f"#### N C H W = {inputShape}")

            
            if not self.singletest(inputShape, logIO=logIO, path=f"Tests/GlobalAveragePool_{i}/"):
                return
            
            print(f"###### Test No. {i} Passed successfully.")




def main():
    tester = GAPLayerTester(seed=21)
    tester.MultipleTest(1, 50, 12, False)

if __name__ == "__main__" :
    main()
    
