import pandas as pd
import numpy as np
from numpy import log as ln
import os
from scipy.stats import linregress
import scipy.integrate as integrate
from scipy.stats import exponweib
from math import exp
import matplotlib.pyplot as plt


class CPU(object):

    def __init__(self, wb_beta, wb_eta, cost_ca, cost_pa):
        self.wb_beta = wb_beta
        self.wb_eta = wb_eta
        self.cost_ca = cost_ca
        self.cost_pa = cost_pa

    def _Rt(self, x):
        wb_beta, wb_eta = self.wb_beta, self.wb_eta
        return exp(-(x/wb_eta)**wb_beta)

    def _Ft(self, x):
        wb_beta, wb_eta = self.wb_beta, self.wb_eta
        return 1-exp(-(x/wb_eta)**wb_beta)

    def cput(self, x):
            """
            Return the solution of the equation (cost_pa * Rt + cost_ca * Ft) / integral(Rsds)
            """
        cost_ca, cost_pa = self.cost_ca, self.cost_pa
        a = (cost_pa * self._Rt(x) + cost_ca * self._Ft(x))
        b = integrate.quad(lambda x: self._Rt(x), 0, x)[0]
        with np.errstate(divide='ignore'):
            c = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
        return c

    def plot_Rt(self, x_min, x_max, num=100):
        x = np.linspace(x_min, x_max, num)
        rel = [self._Rt(time) for time in x]
        fig, ax1 = plt.subplots(figsize=(20, 10))
        ax1.plot(x,rel)
        ax1.set_xlabel('time', fontsize=20)
        ax1.tick_params('x', labelsize=20)
        ax1.set_ylabel('Rt', fontsize=20)
        ax1.tick_params('y', labelsize=20)

        plt.show()

    def plot_Ft(self, x_min, x_max, num=100):
        x = np.linspace(x_min, x_max, num)
        unrel = [self._Ft(time) for time in x]
        fig, ax1 = plt.subplots(figsize=(20, 10))
        ax1.plot(x,unrel)
        ax1.set_xlabel('time', fontsize=20)
        ax1.tick_params('x', labelsize=20)
        ax1.set_ylabel('Ft', fontsize=20)
        ax1.tick_params('y', labelsize=20)
        plt.show()

    def plot_cput(self, x_min, x_max, num=100):
        x = np.linspace(x_min, x_max, num)
        cput = [self.cput(time) for time in x]
        dydt = np.diff(cput)/np.diff(x)

        fig, ax1 = plt.subplots(figsize=(20, 10))
        ax1.plot(x[1:], cput[1:], 'b-')
        ax1.set_xlabel('time', fontsize=20)
        ax1.tick_params('x', labelsize=20)
        ax1.set_yscale('log')
        ax1.set_ylabel('CPUT', fontsize=20)
        ax1.tick_params('y', labelsize=20)

        ax2 = ax1.twinx()
        ax2.plot(x[1:-1], dydt[1:], c="cornflowerblue", linestyle=':')
        ax2.set_ylabel('dy/dt', fontsize=20)
        ax2.tick_params('y',labelsize=20)

        plt.title('Cost with Time', fontsize=20)

        d = {'CPUT': cput[1:-1] , 'dydt': dydt[1:], 'time': x[1:-1] }
        df = pd.DataFrame(d)
        dy_pos = df[df['dydt'] > 0]
        if len(dy_pos) > 0:
            optimum = int(dy_pos['time'].iloc[0])
            plt.axvline(x=optimum, label = str(optimum) + "days", c='k', linestyle='dashed')
            plt.legend(loc='lower right',prop={'size': 30})
        else :
            optimum = 'No optimum '
            plt.axvline(x=max(x), label = str(optimum) + "day found", c='k', linestyle='dashed')
            plt.legend(loc='lower right',prop={'size': 30})

        fig.tight_layout()
        plt.show()
