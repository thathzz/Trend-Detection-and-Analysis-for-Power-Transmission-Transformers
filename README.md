# Trend-Detection-and-Analysis-for-Power-Transmission-Transformers
This repository implements advanced data analytics algorithms for Transformer Dissolved Gas Analysis (DGA) to aid asset management decisions. These tools integrate domain-specific knowledge, physics principles, and statistical methods to identify trends and forecast transformer conditions effectively.

## **Features**

- **Correct Sampling Intervals:** Resamples DGA data based on user-defined intervals, ensuring consistency in analysis.

- **Trend Identification:** Employs a custom algorithm to detect trends in gas levels, incorporating domain-specific expertise and statistical techniques.

- **Outlier Detection:** Identifies anomalous gas readings based on predefined thresholds.

- **Visualisation:** Generates clear and informative plots to illustrate trends and highlight outliers.

## **Usage**

**Functions**

  1. **`correct_sampling_intervals:`** Preprocesses raw DGA data by aligning it to uniform sampling intervals.

  2. **`find_trends:`** Applies a proprietary trend analysis algorithm to detect and quantify trends in gas concentration levels.

  3. **`find_outliers:`** Flags outlier gas readings based on customisable threshold values.

  4. **`plot_trends:`** Visualises gas trends and highlights outliers for detailed analysis.

## **Example Workflow**

  1. Import your DGA data as a `.csv` file.

  2. Use `correct_sampling_intervals` to preprocess the data.

  3. Apply `find_trends` to analyse trends.

  4. Detect outliers using `find_outliers`.

  5. Visualise results with `plot_trends`.

## **Documentation**

Please refer to the [PhD Thesis](https://research.manchester.ac.uk/en/studentTheses/data-analytics-for-transformer-dissolved-gas-analysis-to-aid-asse) and the [IEEE Transactions on Power Delivery Publication](https://ieeexplore.ieee.org/abstract/document/10752917) for detailed explanations of the algorithms and methodologies employed in this project.

## **License**

This repository is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License**.

You may:
- Share the material in any medium or format, as long as you provide proper attribution.
- Not use the material for commercial purposes.
- Not remix, transform, or build upon the material.

For more details, see the [full license text](LICENSE) or visit [Creative Commons](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## **Acknowledgments**

This work draws upon domain expertise and research conducted as part of a PhD program at the University of Manchester. Special thanks to the Transfomer Reserarch Consortium at the University of Manchester.
