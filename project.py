# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 22:05:10 2023
"""

import pandas as pd
import numpy as np

# %% Part A
# 1
df = pd.read_excel('all data.xlsx', parse_dates=['MthCalDt'])
pivot_table = pd.pivot_table(df, values='MthRet', index='MthCalDt', columns='PERMNO')
code = pd.read_excel('all data.xlsx', sheet_name="Code")
pivot_table = pivot_table[code["PERMNO"]]
pivot_table = pivot_table.dropna(axis=1)
print(pivot_table)

# 2
average_monthly_rtn = pivot_table.mean(axis=0)
print(average_monthly_rtn)

# 3
var = pivot_table.var(axis=0)
var_matrix = np.matrix(var)
print(var_matrix)
var_matrix.shape

cov = pivot_table.cov()
cov_matrix = np.matrix(cov)
print(cov_matrix)

# 4
N = pivot_table.shape[1]
print(N)

# %% Part B
# 5


def F_PortRtn(r_i, w_i):
    if len(r_i) != len(w_i):
        print("Lengths of average returns and weights are not the same.")
    else:
        rtn = np.array(r_i)
        weight = np.array(w_i)
        port_rtn = np.sum(rtn*weight)
        return port_rtn

# 6


def F_PortStd(cov, w_i):
    covariance = np.matrix(cov)
    weight = np.matrix(w_i)
    port_var = np.dot(weight, np.dot(covariance, weight.T))
    port_std = np.sqrt(port_var)
    return port_std

# 7


def F_Sharpe(r_p, r_f, s_p):
    excess_rtn = r_p - r_f
    average_excess_rtn = np.mean(excess_rtn)
    SR = average_excess_rtn / s_p
    return SR


# %% Part C
# 8
np.random.seed(662823343)
weights = np.random.uniform(low = 0.0, high = 1.0, size = (1000, N))
weights
a = weights.sum(axis=1, keepdims=True)
random_weights = weights / a
random_weights

# 9
df2 = pd.read_excel('all data.xlsx', sheet_name='t30ret', parse_dates=['caldt'])
pivot_table2 = pd.pivot_table(df2, values='t30ret', index='caldt')
print(pivot_table2)
risk_free_rate = pivot_table2['t30ret'].mean()
risk_free_rate

sharpe_ratios = []
for w in random_weights:
    portfolio_return = F_PortRtn(average_monthly_rtn, w)
    portfolio_std = F_PortStd(cov_matrix, w)
    sharpe_ratio = F_Sharpe(portfolio_return, risk_free_rate, portfolio_std)[0,0]
    sharpe_ratios.append(sharpe_ratio)

print(sharpe_ratios)

# 10
max(sharpe_ratios)
max_index = np.argmax(sharpe_ratios)
print(max_index)
optimal_w = random_weights[max_index]
print(optimal_w)

# 11
column_title = pivot_table.columns
print(column_title)
optimal_portfolio_1 = pd.DataFrame({'Optimal portfolio’s constituent weights': optimal_w, 'PERMNO': column_title})
print(optimal_portfolio_1)
optimal_portfolio_2 = pd.merge(optimal_portfolio_1, code[['PERMNO', 'Company Name']], on = 'PERMNO', how = 'left')
print(optimal_portfolio_2)
optimal_portfolio = optimal_portfolio_2.set_index('PERMNO')
print(optimal_portfolio)
optimal_portfolio.to_excel("Optimal portfolio.xlsx")

