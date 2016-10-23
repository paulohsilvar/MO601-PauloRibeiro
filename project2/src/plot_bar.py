#!/net/edatools/algorete/2013.12/loopy/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

def autolabel(rects, ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


if __name__ == '__main__' : 

  #------------ Lendo csv e armazenando dados -----------------#
  entradas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  bench4k = [];
  bench4m = [];

  for arg in sys.argv: #interpret the argv
    if(arg[-4:] == '.csv'):
      files.append((arg[:-4], arg));


  mcf4k = np.loadtxt("mcf-4kb.csv");
  mcf4m = np.loadtxt("mcf-4mb.csv");
  milck = np.loadtxt("milc-4kb.csv");
  milcm = np.loadtxt("milc-4mb.csv");
  libquantumk = np.loadtxt("libquantum-4kb.csv");
  libquantumm = np.loadtxt("libquantum-4mb.csv");
  hmmerk = np.loadtxt("hmmer_1-4kb.csv");
  hmmerm = np.loadtxt("hmmer_1-4mb.csv");
  gcck = np.loadtxt("gcc_3-4kb.csv");
  gccm = np.loadtxt("gcc_3-4mb.csv");
  leslie3dk = np.loadtxt("leslie3d-4kb.csv");
  leslie3dm = np.loadtxt("leslie3d-4mb.csv");
  lbmk = np.loadtxt("lbm-4kb.csv");
  lbmm = np.loadtxt("lbm-4mb.csv");
  soplexk = np.loadtxt("soplex_1-4kb.csv");
  soplexm = np.loadtxt("soplex_1-4mb.csv");
  omnetppk = np.loadtxt("omnetpp-4kb.csv");
  omnetppm = np.loadtxt("omnetpp-4mb.csv");
  zeusmpk = np.loadtxt("zeusmp-4kb.csv");
  zeusmpm = np.loadtxt("zeusmp-4mb.csv");
  bench4k.append(milck);
  bench4k.append(libquantumk); 
  bench4k.append(hmmerk); 
  bench4k.append(mcf4k);
  bench4k.append(gcck);
  bench4k.append(leslie3dk); 
  bench4k.append(lbmk); 
  bench4k.append(soplexk);
  bench4k.append(omnetppk); 
  bench4k.append(zeusmpk); 

  bench4m.append(milcm); 
  bench4m.append(libquantumm);
  bench4m.append(hmmerm); 
  bench4m.append(mcf4m); 
  bench4m.append(gccm); 
  bench4m.append(leslie3dm);
  bench4m.append(lbmm); 
  bench4m.append(soplexm); 
  bench4m.append(omnetppm);
  bench4m.append(zeusmpm);

  #------------ Salvando valores avalidados separadamente -----------------#

  maik = []; #mai->memory access instruction | mad-> memory access dados
  madk = [];
  tlbmik = [];#tlbmi->tlb misses instruction  | tlbmd->tlb misses dados
  tlbmdk = [];
  tpaik = [];#tpai->table pages access instruction | tpad->table pages access dados
  tpadk = [];

  for bench in bench4k:
    maik.append(bench[0]);
    tlbmik.append(bench[1]);
    tpaik.append(bench[2]);
    madk.append(bench[3]);
    tlbmdk.append(bench[4]);
    tpadk.append(bench[5]);

  maim = [];
  madm = [];
  tlbmim = [];
  tlbmdm = [];
  tpaim = [];
  tpadm = []
  for bench in bench4m:
    maim.append(bench[0]);
    tlbmim.append(bench[1]);
    tpaim.append(bench[2]);
    madm.append(bench[3]);
    tlbmdm.append(bench[4]);
    tpadm.append(bench[5]);
 
  #------------ Constantes do grafico -----------------#

  N = 10;
  width = 0.48; 
  ind = np.arange(N);

  #------------ Figura 1 -----------------#

  fig1, ax1 = plt.subplots();
  bar1 = ax1.bar(ind,       maik, width, color='w');
  bar2 = ax1.bar(ind+width, maim, width, color='k');

  ax1.set_ylabel("Valor Medido");
  ax1.set_title("Avaliacao para Instrucao");
  ax1.set_xticks(ind+width);
  ax1.set_ylim([0, 3000000]);
  ax1.set_xticklabels(('milc', 'libquantum', 'hmmer_1', 'mcf', 'gcc_3', 'leslie3d', 'lbm', 'soplex_1', 'omnetppm', 'zeusmp'))
  ax1.legend((bar1[0], bar2[0]), ("Total Memory Access for Instruction - TLB 4KB", "Total Memory Access for Instruction - TLB 4MB"), loc=1);

  #------------ Figura 2 -----------------#

  fig2, ax2 = plt.subplots();
  bar3 = ax2.bar(ind, tlbmik, width, color='w');
  bar4 = ax2.bar(ind+width, tlbmim, width, color='k');

  ax2.set_ylabel("Valor Medido");
  ax2.set_title("Avaliacao por Instrucao");
  ax2.set_xticks(ind+width);
  ax2.set_ylim([0,250]);
  ax2.set_xticklabels(('milc', 'libquantum', 'hmmer_1', 'mcf', 'gcc_3', 'leslie3d', 'lbm', 'soplex_1', 'omnetppm', 'zeusmp'))
  ax2.legend((bar3[0], bar4[0]), ("TLB misses - TLB 4KB", "TLB misses - Tlb 4MB"), loc=1);

  #------------ Figura 3 -----------------#

  fig3, ax3 = plt.subplots();
  bar5 = ax3.bar(ind, tpaik, width, color='w');
  bar6 = ax3.bar(ind+width, tpaim, width, color='k');

  ax3.set_ylabel("Valor Medido");
  ax3.set_title("Avaliacao por Instucao");
  ax3.set_xticks(ind+width);
  ax3.set_ylim([0, 700]);
  ax3.set_xticklabels(('milc', 'libquantum', 'hmmer_1', 'mcf', 'gcc_3', 'leslie3d', 'lbm', 'soplex_1', 'omnetppm', 'zeusmp'))
  ax3.legend((bar5[0], bar6[0]), ("Total Table Pages Access - TLB 4KB", "Total Table Pages Access - TLB 4MB"), loc=1);
  
  #------------ Figura 4 -----------------#

  fig4, ax4 = plt.subplots();
  bar7 = ax4.bar(ind, madk, width, color='w');
  bar8 = ax4.bar(ind+width, madm, width, color='k');

  ax4.set_ylabel("Valor Medido");
  ax4.set_title("Avaliacao por Dados");
  ax4.set_xticks(ind+width);
  ax4.set_ylim([0,100000000]);
  ax4.set_xticklabels(('milc', 'libquantum', 'hmmer_1', 'mcf', 'gcc_3', 'leslie3d', 'lbm', 'soplex_1', 'omnetppm', 'zeusmp'))
  ax4.legend((bar7[0], bar8[0]), ("Total Memory Access for Data - TLB 4KB", "Total Memory Access for Data - TLB4MB"), loc=1);
  
  #------------ Figura 5 -----------------#

  fig5, ax5 = plt.subplots();
  bar9  = ax5.bar(ind, tlbmdk, width, color='w');
  bar10 = ax5.bar(ind+width, tlbmdm, width, color='k');

  ax5.set_ylabel("Valor Medido");
  ax5.set_title("Avaliacao por Dados");
  ax5.set_xticks(ind+width);
  ax5.set_ylim([0,80000000]); 
  ax5.set_xticklabels(('milc', 'libquantum', 'hmmer_1', 'mcf', 'gcc_3', 'leslie3d', 'lbm', 'soplex_1', 'omnetppm', 'zeusmp'))
  ax5.legend((bar9[0], bar10[0]), ("TLB misses - 4KB", "TLB misses - 4MB"), loc=1);

  #------------ Figura 6 -----------------#

  fig6, ax6 = plt.subplots();
  bar11 = ax6.bar(ind, tpadk, width, color='w');
  bar12 = ax6.bar(ind+width, tpadm, width, color='k');

  ax6.set_ylabel("Valor Medido");
  ax6.set_title("Avaliacao por Dados");
  ax6.set_xticks(ind+width);
  ax6.set_ylim([0,250000000]);
  ax6.set_xticklabels(('milc', 'libquantum', 'hmmer_1', 'mcf', 'gcc_3', 'leslie3d', 'lbm', 'soplex_1', 'omnetppm', 'zeusmp'))
  ax6.legend((bar11[0], bar12[0]), ("Total Table Pages Access - TLB 4KB", "Total Table Pages Access - TLB 4MB"), loc=1);

  #------------ Inserindo valor na barra -----------------#

  autolabel(bar1, ax1);
  autolabel(bar2, ax1);
  autolabel(bar3, ax2);
  autolabel(bar4, ax2);
  autolabel(bar5, ax3);
  autolabel(bar6, ax3);
  autolabel(bar7, ax4);
  autolabel(bar8, ax4);
  autolabel(bar9, ax5);
  autolabel(bar10, ax5);
  autolabel(bar11, ax6);
  autolabel(bar12, ax6);

  plt.show();
