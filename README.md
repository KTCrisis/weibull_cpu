# cost_preventive
Class to calculate best preventive time based on Weibull Distribution

 init CPU with parameters
 
 wb_beta = Beta of Weibull Distribution
 wb_eta = Eta of Weibull Distribution
 cost_ca = Cost of Corrective Repair
 cost_pa = Cost of Preventive Repair
 
 Example: cpu = CPU(wb_beta = 2, wb_eta = 500, cost_ca= 100, cost_pa = 5)
 
 Possible method
 Plot Unreliability : plot_Ft(xmin, xmax, step) -> Create the x axis for the plot from 0 to 100 hours with 1 hour step
 Example: cpu.plot_Ft(0,100, 100)
 
 Plot Reliability : plot_Rt(xmin, xmax, step)
 Plot Cost Per Unit: plot_cput(xmin, xmax, step)
 
