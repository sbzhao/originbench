"""
@brief 本模块提供基准测试类的抽象，是系统级基准测试类SysBench和应用程序级基准测试类AppBench的基类。


"""

from typing import Dict, Any, List
from abc import ABC, abstractclassmethod

class BaseBench(ABC):
    """
    @brief BaseBench类
    @var _type: 基准测试的类型，系统级基准测试类型为:"system", 应用程序级基准测试类型为："application"
    @var _param: 基准测试类的参数，不同的基准测试类型具有不同的参数列表
    """
    
    def __init__(self, type: str) -> None:
        super().__init__()
        self._type = type
        self._param = None

    @abstractclassmethod
    def prepare(self, param:Dict[str, Any]) -> None:
        """
        @brief 基准测试开始前的准备工作
        @param param: 基准测试准备所需的参数
        @exception 
        """
        self._param = param
        pass

    @abstractclassmethod
    def build_circuits(self) -> List[str]:
        """
        @brief 构造基准测试量子线路
        @return: 构造的量子线路列表，量子线路以OriginIR字符串表示
        """
        pass

    @abstractclassmethod
    def run(self, circuits: List[str]):
        """
        @brief 批量运行量子线路
        @param circuits: OriginIR量子线路列表
        """
        pass

    @abstractclassmethod
    def get_results(self):
        pass

    @abstractclassmethod
    def analyze(self):
        pass