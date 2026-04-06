# Claude Code 任务指令

## 项目路径
/Users/stefana/Desktop/pvart

## 论文标题
"From visual pattern to electrical performance: image-derived descriptors 
and experimental validation for coloured photovoltaic facades"

## 论文结构 → 代码对应关系

论文共需要以下计算和图表，请按顺序执行：

### Section 2: Image-Derived Descriptor Framework
需要运行的脚本：`scripts/02_extract_image_descriptors.py`

任务：对以下图片提取6个描述符（CCR, EAR, SF, ED, DSV, PUI），保存到 data/extracted_descriptors/

- data/pattern_images/algorithm_steps/step5_energy_oriented.jpg (--split 3)
- data/pattern_images/algorithm_steps/step5_graphic_oriented.jpg (--split 3)  
- data/pattern_images/algorithm_steps/step5_balanced_oriented.jpg (--split 3)
- data/pattern_images/algorithm_steps/dot_size_gradient.png (--split 4 --grid 2)

### Section 5.1: Single-descriptor analysis
需要新脚本：`scripts/03_single_descriptor_regression.py`

任务：
- 用 M-5, M-9, M-8, M-7 数据做 CCR → η 的线性回归和二次回归
- 计算 R², RMSE, 残差
- 生成 Figure: coverage vs efficiency scatter + regression lines
- 生成 Figure: residual plot

### Section 5.2: Multi-descriptor analysis  
需要新脚本：`scripts/04_multi_descriptor_analysis.py`

任务：
- 合并 image_descriptors.csv 和 lab_scale_SERIS.csv
- 对同 CCR (26.48%) 的 5 个模块，分析 SF、ED、DSV 与 Isc/efficiency 的关系
- 做多元回归: η = f(CCR, ED, SF)
- 生成 Figure: descriptor correlation heatmap
- 生成 Figure: partial dependence plots

### Section 5.3: Optical loss decomposition
需要新脚本：`scripts/05_loss_decomposition.py`

任务：
- 读取 loss_decomposition.csv
- 计算每个模块的 ΔIsc/Isc, ΔVoc/Voc, ΔFF/FF 贡献
- 生成 Figure: stacked bar chart of loss components

### Section 5.4: Effective shading model
需要新脚本：`scripts/06_shading_model.py`

任务：
- 读取 shading_coefficients.csv
- 建立模型: Isc = Isc_baseline × (1 - α × CCR)
- 分析 α 与 dot size / pattern type 的关系
- 生成 Figure: Isc vs CCR with α model lines
- 生成 Figure: α vs pattern descriptors

### Section 5.5: Hotspot risk Monte Carlo simulation
需要新脚本：`scripts/08_hotspot_simulation.py`

任务：
- 模拟一个 60-cell 串联模块
- 对比两种着色策略:
  (a) Algorithm method: 每个 cell 的 CCR = 26.48% ± 2% (PUI ≈ 0)
  (b) Full-image print: 每个 cell 的 CCR 从 5% 到 80% 不等（模拟真实图像的明暗变化）
- 用单二极管模型计算每个 cell 在不同 CCR 下的 Isc
- 找出 current-limiting cell，计算 mismatch loss
- 蒙特卡洛 1000 次，统计:
  - 最大 cell 温差
  - hotspot 发生概率（定义: 任一 cell 反偏功率 > 1W）
  - 模块总功率损失
- 生成 Figure: cell-level irradiance distribution (algorithm vs full-print)
- 生成 Figure: hotspot probability histogram

### Section 5.6: Product-scale validation
需要新脚本：`scripts/09_product_validation.py`

任务：
- 读取 product_scale_fullsize.csv
- 绘制 EG-PF1~3 vs SERIS 的对比 bar chart
- 雷达图: 多参数综合对比
- 将 lab-scale 预测（从描述符模型）与 product-scale 实测对比
- 生成 Figure: predicted vs measured efficiency (model validation)

### 汇总 Figure List
需要新脚本：`scripts/10_compile_all_figures.py`

将所有 figure 按论文顺序重命名:
- Fig1_algorithm_workflow.jpg  (手动准备)
- Fig2_descriptor_definition.png (从脚本生成)
- Fig3_coverage_efficiency_regression.png
- Fig4_multi_descriptor_correlation.png
- Fig5_loss_decomposition.png
- Fig6_shading_model.png
- Fig7_Isc_shading_model.png  (from script 01, shading model)
- Fig8_hotspot_simulation.png
- Fig9_product_validation.png
- Fig10_pv_art_applications.jpg (手动拼图)

## 执行方式

在 Claude Code 中输入:
```
看一下 /Users/stefana/Desktop/pvart 项目，
按照 docs/TASK_LIST.md 中的任务顺序，
从 scripts/03 开始逐个创建和运行脚本，
每个脚本运行后将结果保存到 data/extracted_descriptors/ 
和 figures/ 中，然后 git commit
```
