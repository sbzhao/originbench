# OriginBench

## OriginBench介绍
OriginBench是用于对本源芯片进行基准测试(Benchmark)的Python软件包。主要由以下几个模块组成：
- `bench`: 此模块定义了不同基准测试实验类
- `circ_builder`: 此模块用于实现不同基准测试的线路构造
- `chip_topology`: 此模块处理不同的芯片拓扑结构
- `data_processor`: 此模块处理不同基准测试线路运行的结果

下面详细介绍各部分的功能。

## 功能模块

### `bench`
`bench`模块中`BaseBench`类抽象了基准测试类的接口，一个基本的基准测试实验由以下几个步骤组成：
1. prepare()
2. build_circuits()
3. run()
4. get_results()
5. analyze()

其中，`prepare()`方法用于进行构造量子线路前的准备，如初始化量子比特映射关系、初始化线路参数等，具体实现由特定的基准测试类自己实现；`build_circuits()`根据设置好的参数，生成批量量子线路列表，这里量子线路以`OriginIR`字符串形式保存；`run()`函数则将量子线路批量提交至量子计算后端进行计算，并返回相应的任务ID；`get_results()`根据任务ID获取任务的计算结果；`analyze()`对得到的量子线路运行结果进行分析以及可视化展示，这种可视化方式因基准测试类型不同而不同，由具体基准测试类实现。

在OriginBench中，我们将基准测试类分为两类，即系统级基准测试和应用程序级基准测试，这两种基准测试的基类分别为`SysBench`和`AppBench`。

> 注：用户自定义的系统级基准测试类和应用程序级基准测试类直接继承`SysBench`类和`AppBench`，禁止直接继承`BaseBench`.

### `circ_builder`
`circ_builder`模块用于实现不同基准测试实验的量子线路构造器，用户在实现自己的基准测试类的同时，要实现相应的量子线路构造器。

### `chip_topology`
`chip_topology`模块用于表示芯片的拓扑连接关系，量子线路构造器根据芯片拓扑连接关系完成量子线路中逻辑比特到实际物理比特的映射。

### `data_processor`
`data_processor`数据处理器用于对基准测试结果的处理，由于不同的基准测试对数据处理的方式不同，可视化方式也不同，因此用户在实现自己的基准测试类时，也要相应的实现数据处理类，其中对数据的处理也包括自动可视化。

## 如何构造自定义的基准测试类型
我们这里的架构设计，使得基准测试线路构造、任务计算、数据处理等功能的隔离，使得用户可以轻松地实现自己的基准测试类型，从而简单高效的进行芯片基准测试实验。下面我们介绍一下如何构造自定义的基准测试类型，主要分为三步：

### 第一步：构造自定义基准测试类
首先，假设我们要定义的基准测试为系统级基准测试`QV`，即量子体积（Quantum Volume），详情可参见[Validating quantum computers using randomized model circuits](
https://doi.org/10.48550/arXiv.1811.12926). 我们定义一个QV基准测试类`QVBench`继承`SysBench`(类似的，应用程序级基准测试类继承`AppBench`，这里不做进一步介绍)。

做法如下，在`originbench/bench`目录下，新建`qv_bench.py`，其内容如下：
```Python
from .sysbench import SysBench

class QVBench(SysBench):
    pass
```
### 第二步：构造对应基准测试类型的量子线路构造器
然后，我们要定义`QVBench`基准测试对应的量子线路构造器，用于构造`QV`基准测试实验的量子线路，做法如下：
在`originbench/circ_builder`目录下，新建`qv_circ_builder.py`，其内容如下：
```Python
from .circ_builder import CircBuilder

class QVCircBuilder(CircBuilder):
    pass
```

### 第三步：构造对应基准测试类型的数据处理器
接下来，我们要实现QV基准测试对应的数据处理器，做法如下：
在`originbench/data_processor`目录下，新建`qv_data_processor.py`，其内容大致如下：
```Python
class QVDataProcessor:
    pass
```