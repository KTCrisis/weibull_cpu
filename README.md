# Python Class for Preventive Time Calculation based on Cost Per Unit
This python script has for goal to plot and find the optimal time for preventime maintenance.
It's useful for reliability and maintenance engineer who define when to repair units before failure.

Read : https://www.weibull.com/hotwire/issue96/relbasics96.htm for more details

# Init CPU with parameters
 
 - wb_beta = Beta of Weibull Distribution
 
 - wb_eta = Eta of Weibull Distribution
 
 - cost_ca = Cost of Corrective Repair
 
 - cost_pa = Cost of Preventive Repair
 
 
 Example: cpu = CPU(wb_beta = 2, wb_eta = 500, cost_ca= 100, cost_pa = 5)
 
 # Possible method:
 
 - Plot Unreliability : plot_Ft(xmin, xmax, step) -> Create the x axis for the plot from 0 to 1000 hours with 10 hours step
 Example: cpu.plot_Ft(0, 1000, 100)
 
 - Plot Reliability : plot_Rt(xmin, xmax, step)
 
 - Plot Cost Per Unit: plot_cput(xmin, xmax, step)
 
![ScreenShot](https://raw.github.com/KTCrisis/cost_preventive/master/cost_per_unit.png)
