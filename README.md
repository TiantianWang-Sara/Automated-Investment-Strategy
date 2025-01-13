- Project Overview
This project focuses on constructing and optimizing investment portfolios using historical return data for S&P 500 constituents. By calculating the Sharpe ratio for various portfolios, we identify the optimal portfolio with the highest risk-adjusted return. The process involves data preparation, function development, and portfolio selection based on the Sharpe ratio.

- Key Steps
1. Data Collection & Cleaning:
We sourced monthly returns for S&P 500 companies, the S&P 500 index, and 30-day Treasury bill rates from WRDS, covering the period 2010–2022. Data was cleaned, and key metrics such as average monthly returns, variance, and covariance were computed.

2. Portfolio Optimization:
We wrote functions to calculate portfolio returns, standard deviations, and Sharpe ratios:

Expected returns: Calculated as the weighted average of individual stock returns.
Portfolio standard deviation: Derived using covariance and portfolio weights.
Sharpe ratio: Computed to evaluate risk-adjusted returns, considering the risk-free rate.

3. Monte Carlo Simulation:
Random weight sets (1000 simulations) were generated for 435 stocks, and the Sharpe ratio for each portfolio was computed. The optimal portfolio with the highest Sharpe ratio was identified.

- Results & Reporting:
The portfolio with the highest Sharpe ratio (0.308) was identified, with the largest weight allocated to AMGEN INC. The corresponding weights for all 435 stocks were exported to an Excel file for further analysis.

- Conclusion
This analysis provides valuable insights into constructing an optimal portfolio based on risk-return trade-offs, helping investors make informed decisions when optimizing their investment strategies.
