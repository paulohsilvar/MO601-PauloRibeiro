#!/net/edatools/algorete/2013.12/loopy/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

def autolabel2(rects, ax, vector):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        print 'height %.2f' % vector + " - "
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.2f' % vector,
                ha='center', va='bottom')


if __name__ == '__main__' : 

  #------------ Lendo csv e armazenando dados -----------------#
  entradas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  proc_origin   = np.loadtxt("ipc_original.csv");
  proc_onebit   = np.loadtxt("ipc_1bit_predictor.csv");
  tcache_onebit = np.loadtxt("ipc_tcache_1bit_predictor.csv");
  tcache_origin = np.loadtxt("ipc_tcache_original.csv");

  #------------ Constantes do grafico -----------------#

  N = 1;
  width = 0.1; 
  ind = np.arange(N);

  #------------ Figura 1 -----------------#

  fig1, ax1 = plt.subplots();

  b1 = ax1.bar(ind+(width*0), proc_origin, width, color='w');
  b2 = ax1.bar(ind+(width*1), proc_onebit, width, color='k');
  b3 = ax1.bar(ind+(width*2), tcache_origin, width, color='b');
  b4 = ax1.bar(ind+(width*3), tcache_onebit, width, color='r');

  ax1.set_ylabel("IPC");
  ax1.set_xlabel("FFT Benchmark");
  ax1.set_title("IPC for the Various Fetch Mechanisms");
  ax1.set_ylim([0, 2.5]);
  ax1.set_xticks(ind);
  ax1.legend((b1[0], b2[0], b3[0], b4[0]), ("Simulador Original", "Seq.1", "Simulador com Trace Cache", "Seq.1 com Trace Cache"), loc=1);

  #------------ Inserindo valor na barra -----------------#

  autolabel2(b1, ax1, proc_origin);
  autolabel2(b2, ax1, proc_onebit);
  autolabel2(b3, ax1, tcache_origin);
  autolabel2(b4, ax1, tcache_onebit);

  plt.show();

