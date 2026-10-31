#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:00:44 2026

@author: cristinamiergonzalez
"""

#general imports
import sys
import matplotlib.pyplot as plt 
from matplotlib import rc

# nanonis import
sys.path.append('/Users/cristinamiergonzalez/Python_code/nanonis')  # path de Mac Cris
import nanonis
spectra = nanonis.biasSpectroscopy()
linescan = nanonis.linescan()
topo_file =nanonis.simpleScan()

#%% Plotting cosmetics

rc('font',**{'family':'sans-serif','sans-serif':['Arial']}) # Sets font of everything (I think)

plt.rcParams['axes.linewidth'] = 0.5   # sets the line thickness for the axes

plt.rc('axes', labelsize=7)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=7)    # fontsize of the tick labels
plt.rc('ytick', labelsize=7)    # fontsize of the tick labels
plt.rc('legend', fontsize=7)    # fontsize of the tick labels
lw = 1.2

cm = 1/2.54 # converts inch to cm

#%% load data and analysis
#Data_folder = 'Z:/STMDATA/Berlino/Nb(110)/2026-06-08 - DBBA on ProxyAu/2026-08-11 - porxyAu10ML_AGNRs_CO_depo/' # folder path in zanet
Data_folder = '/Users/cristinamiergonzalez/Library/CloudStorage/OneDrive2-AsociacionCicNanogune/Projects_articles/ProxyAu_AGNR/key_data/YSR_surface_manipulation/'

# initial state spectra
SC_file_name = 'S_260813_00065.dat' ### good spectra of the SC surface
edge1_0_filename = 'S_260813_00039.dat'
edge2_0_filename = 'S_260813_00037.dat'
# move 1
#edge1_1_filename = 'S_260813_00055.dat'
edge1_1_filename = 'S_260813_00056.dat'
edge2_1_filename = 'S_260813_00064.dat'
# move 2
edge1_2_filename = 'CS01_260813_00015.dat'
#edge1_2_filename = 'CS01_260813_00016.dat'
edge2_2_filename = 'S_260813_00071.dat'
#move 3
edge1_3_filename = 'S_260813_00076.dat'
edge2_3_filename = 'S_260813_00086.dat'

# load data
# initial state
spectra_SC = nanonis.biasSpectroscopy()
spectra_ed1_0 = nanonis.biasSpectroscopy()
spectra_ed2_0 = nanonis.biasSpectroscopy()
spectra_SC.load(str(Data_folder+SC_file_name))
spectra_ed1_0.load(str(Data_folder+edge1_0_filename))
spectra_ed2_0.load(str(Data_folder+edge2_0_filename))
# move 1
spectra_ed1_1 = nanonis.biasSpectroscopy()
spectra_ed2_1 = nanonis.biasSpectroscopy()
spectra_ed1_1.load(str(Data_folder+edge1_1_filename))
spectra_ed2_1.load(str(Data_folder+edge2_1_filename))
# move 2
spectra_ed1_2 = nanonis.biasSpectroscopy()
spectra_ed2_2 = nanonis.biasSpectroscopy()
spectra_ed1_2.load(str(Data_folder+edge1_2_filename))
spectra_ed2_2.load(str(Data_folder+edge2_2_filename))
# move 3
spectra_ed1_3 = nanonis.biasSpectroscopy()
spectra_ed2_3 = nanonis.biasSpectroscopy()
spectra_ed1_3.load(str(Data_folder+edge1_3_filename))
spectra_ed2_3.load(str(Data_folder+edge2_3_filename))

# normalize condcutance to the baseline
spectra_SC.normalizeRange([3.5e-3,4e-3])
spectra_ed1_0.normalizeRange([3.5e-3,4e-3])
spectra_ed2_0.normalizeRange([3.5e-3,4e-3])
# move 1
spectra_ed1_1.normalizeRange([3.5e-3,4e-3])
spectra_ed2_1.normalizeRange([3.5e-3,4e-3])
# move 2
spectra_ed1_2.normalizeRange([3.5e-3,4e-3])
spectra_ed2_2.normalizeRange([3.5e-3,4e-3])
# move 3
spectra_ed1_3.normalizeRange([3.5e-3,4e-3])
spectra_ed2_3.normalizeRange([3.5e-3,4e-3])

#%% plot spectra

# create different plots
# initial state + substrate
fig1, ax1 = plt.subplots(figsize=(10*cm, 8*cm))
ax1.plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = lw, color = 'k')
ax1.plot(spectra_ed1_0.bias*1e3, spectra_ed1_0.conductance, linewidth = lw, color = 'C3')
ax1.plot(spectra_ed2_0.bias*1e3, spectra_ed2_0.conductance, linewidth = lw, color = 'C0')
# axis limits
ax1.set_xlim([-4.5, 4.5])
#ax1.set_ylim([-2.5, 18])
# axis labels
ax1.set_xlabel('Bias (mV)')
ax1.set_ylabel(r'Conductance (G$_N$)')
ax1.set_title('initial state')

# move 1
fig2, ax2 = plt.subplots(figsize=(10*cm, 8*cm))
ax2.plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = lw, color = 'k')
ax2.plot(spectra_ed1_1.bias*1e3, spectra_ed1_1.conductance, linewidth = lw, color = 'C3')
ax2.plot(spectra_ed2_1.bias*1e3, spectra_ed2_1.conductance, linewidth = lw, color = 'C0')
# axis limits
ax2.set_xlim([-4.5, 4.5])
#ax1.set_ylim([-2.5, 18])
# axis labels
ax2.set_xlabel('Bias (mV)')
ax2.set_ylabel(r'Conductance (G$_N$)')
ax2.set_title('Move 1')

# move 2
fig3, ax3 = plt.subplots(figsize=(10*cm, 8*cm))
ax3.plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = lw, color = 'k')
ax3.plot(spectra_ed1_2.bias*1e3, spectra_ed1_2.conductance, linewidth = lw, color = 'C3')
ax3.plot(spectra_ed2_2.bias*1e3, spectra_ed2_2.conductance, linewidth = lw, color = 'C0')
# axis limits
ax3.set_xlim([-4.5, 4.5])
#ax1.set_ylim([-2.5, 18])
# axis labels
ax3.set_xlabel('Bias (mV)')
ax3.set_ylabel(r'Conductance (G$_N$)')
ax3.set_title('Move 2')

# move 2
fig4, ax4 = plt.subplots(figsize=(10*cm, 8*cm))
ax4.plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = lw, color = 'k')
ax4.plot(spectra_ed1_3.bias*1e3, spectra_ed1_3.conductance, linewidth = lw, color = 'C3')
ax4.plot(spectra_ed2_3.bias*1e3, spectra_ed2_3.conductance, linewidth = lw, color = 'C0')
# axis limits
ax4.set_xlim([-4.5, 4.5])
#ax1.set_ylim([-2.5, 18])
# axis labels
ax4.set_xlabel('Bias (mV)')
ax4.set_ylabel(r'Conductance (G$_N$)')
ax4.set_title('Move 3')


#%% paper plots

fig, axs = plt.subplots(1, 4, figsize=(18*cm, 3.5*cm))
page_width, page_height = 24*cm, 3.5*cm
fig.set_size_inches(page_width, page_height)

axs[0].plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = 0.8*lw, color = 'grey')
axs[0].plot(spectra_ed1_0.bias*1e3, spectra_ed1_0.conductance, linewidth = lw, color = 'C3')
axs[0].plot(spectra_ed2_0.bias*1e3, spectra_ed2_0.conductance, linewidth = lw, color = 'C0')
axs[0].set_xlim([-4.5, 4.5])
axs[0].set_xlabel('Bias (mV)')
axs[0].set_ylabel(r'dI/dV (arb. units)')

axs[1].plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = 0.8*lw, color = 'grey')
axs[1].plot(spectra_ed1_1.bias*1e3, spectra_ed1_1.conductance, linewidth = lw, color = 'C3')
axs[1].plot(spectra_ed2_1.bias*1e3, spectra_ed2_1.conductance, linewidth = lw, color = 'C0')
axs[1].set_xlim([-4.5, 4.5])
axs[1].set_xlabel('Bias (mV)')
axs[1].set_yticks([0, 10, 20])

axs[2].plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = 0.8*lw, color = 'grey')
axs[2].plot(spectra_ed1_2.bias*1e3, spectra_ed1_2.conductance, linewidth = lw, color = 'C3')
axs[2].plot(spectra_ed2_2.bias*1e3, spectra_ed2_2.conductance, linewidth = lw, color = 'C0')
axs[2].set_xlim([-4.5, 4.5])
axs[2].set_xlabel('Bias (mV)')

axs[3].plot(spectra_SC.bias*1e3, spectra_SC.conductance, linewidth = 0.8*lw, color = 'grey')
axs[3].plot(spectra_ed1_3.bias*1e3, spectra_ed1_3.conductance, linewidth = lw, color = 'C3')
axs[3].plot(spectra_ed2_3.bias*1e3, spectra_ed2_3.conductance, linewidth = lw, color = 'C0')
axs[3].set_xlim([-4.5, 4.5])
axs[3].set_xlabel('Bias (mV)')

#%%



fig.savefig('spectra_SupFig_v1.pdf', 
            dpi=600, # probably not needed for PDF, but I'm writing it anyway
            transparent=True, # you probably want this one. Otherwise you'll have to remove background every time in Illustrator ...
            bbox_inches = 'tight'
            )









