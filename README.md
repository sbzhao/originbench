# OriginBench

## OriginBench介绍
OriginBench是用于对本源芯片进行基准测试(Benchmark)的Python软件包。主要由以下几个模块组成：
- `bench`: 此模块定义了不同基准测试实验类
- `circ_builder`: 此模块用于实现不同基准测试的线路构造
- `chip_topology`: 此模块处理不同的芯片拓扑结构
- `data_processor`: 此模块处理不同基准测试线路运行的结果

下面详细介绍各部分的功能。

## `bench`
`bench`模块中`BaseBench`类抽象了基准测试类的接口，一个基本的基准测试实验由以下几个步骤组成：
1. prepare()
2. build_circuits()
3. run()
4. get_results()
5. analyze()

其中，`prepare()`方法用于进行构造量子线路前的准备，如初始化量子比特映射关系、初始化线路参数等，具体实现由特定的基准测试类自己实现；`build_circuits()`根据设置好的参数，生成批量量子线路列表，这里量子线路以`OriginIR`字符串形式保存；`run()`函数则将量子线路批量提交至量子计算后端进行计算，并返回相应的任务ID；`get_results()`根据任务ID获取任务的计算结果；`analyze()`对得到的量子线路运行结果进行分析以及可视化展示，这种可视化方式因基准测试类型不同而不同，由具体基准测试类实现。

在OriginBench中，我们将基准测试类分为两类，即系统级基准测试和应用程序级基准测试，这两种基准测试的基类分别为`SysBench`和`AppBench`。

> 注：用户自定义的系统级基准测试类和应用程序级基准测试类直接继承`SysBench`类和`AppBench`，禁止直接继承`BaseBench`.

## `circ_builder`

## `chip_topology`

## `data_processor`