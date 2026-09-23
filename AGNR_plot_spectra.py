# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:51:13 2026

@author: cmier
"""

# general imports
import sys
import matplotlib.pyplot as plt 
from matplotlib import rc

# nanonis imports
#sys.path.append('C:/Users/jeandino/PythonScripts/GitHub/Nanonis/nanonis')  # path de Jose
sys.path.append('C:/Users/cmier/Python_projects/nanonis')  # path de Cris
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
Data_folder = 'Z:/STMDATA/Berlino/Nb(110)/2026-06-08 - DBBA on ProxyAu/2026-08-11 - porxyAu10ML_AGNRs_CO_depo/' # folder path in zanet

# file names 1st pair of spectra
#Filename_1 = 'S_260812_00160.dat' #surface
#Filename_2 = 'S_260812_00156.dat' #end1
#Filename_3 = 'S_260812_00153.dat' #end2

# file names 2nd pair of spectra
Filename_1 = 'S_260812_00141.dat' #surface
Filename_1 = 'S_260812_00160.dat' #surface
Filename_2 = 'S_260812_00143.dat' #end1
Filename_3 = 'S_260812_00145.dat' #end2

# load data
spectra1 = nanonis.biasSpectroscopy()
spectra2 = nanonis.biasSpectroscopy()
spectra3 = nanonis.biasSpectroscopy()
spectra1.load(str(Data_folder+Filename_1))
spectra2.load(str(Data_folder+Filename_2))
spectra3.load(str(Data_folder+Filename_3))

# normalize condcutance to the baseline
spectra1.normalizeRange([3.5e-3,4e-3])
spectra2.normalizeRange([3.5e-3,4e-3])
spectra3.normalizeRange([3.5e-3,4e-3])


#%% plot spectra

# create two different plots
fig1, ax1 = plt.subplots(figsize=(10*cm, 8*cm))
fig2, ax2 = plt.subplots(figsize=(10*cm, 8*cm))

# first end + substrate
ax1.plot(spectra1.bias*1e3,spectra1.conductance, linewidth = lw, color = 'k')
ax1.plot(spectra2.bias*1e3,spectra2.conductance, linewidth = lw, color = 'C3')

# second end + substrate
ax2.plot(spectra1.bias*1e3,spectra1.conductance, linewidth = lw, color = 'k')
ax2.plot(spectra3.bias*1e3,spectra3.conductance, linewidth = lw, color = 'C0')

# axis limits
ax1.set_xlim([-4.5, 4.5])
ax2.set_xlim([-4.5, 4.5])
ax1.set_ylim([-2.5, 18])
ax2.set_ylim([-2.5, 18])

# axis labels
ax1.set_xlabel('Sample bias (mV)')
ax2.set_xlabel('Sample bias (mV)')

ax1.set_ylabel(r'Conductance (G$_N$)')
ax2.set_ylabel(r'Conductance (G$_N$)')

#%% plot spectra same plot


fig3,axs = plt.subplots(1,2, figsize=(8*cm, 5*cm))

axs[1].plot(spectra1.bias*1e3,spectra1.conductance, linewidth = lw, color = 'k')
axs[1].plot(spectra2.bias*1e3,spectra2.conductance, linewidth = lw, color = 'C3')

axs[0].plot(spectra1.bias*1e3,spectra1.conductance, linewidth = lw, color = 'k')
axs[0].plot(spectra3.bias*1e3,spectra3.conductance, linewidth = lw, color = 'C0')

# axis limits
axs[0].set_xlim([-4.5, 4.5])
axs[1].set_xlim([-4.5, 4.5])
axs[0].set_ylim([-2.5, 18])
axs[1].set_ylim([-2.5, 18])

axs[0].set_ylim([-0.5, 8])
axs[1].set_ylim([-0.5, 8])

# axis labels
axs[0].set_xlabel('Sample bias (mV)')
axs[1].set_xlabel('Sample bias (mV)')

axs[0].set_ylabel(r'Conductance (G$_N$)')
fig3.tight_layout(pad=0.5) 

#fig3.savefig('Spectra_v2.png', 
#            dpi=600, # probably not needed for PDF, but I'm writing it anyway
#            transparent=True, # you probably want this one. Otherwise you'll have to remove background every time in Illustrator ...
#            bbox_inches = 'tight'
#            )


#%% plot spectra same plot vertically


fig3,axs = plt.subplots(2,1, figsize=(5.5*cm, 7.5*cm))

axs[1].plot(spectra1.bias*1e3,spectra1.conductance, linewidth = lw, color = 'grey')
axs[1].plot(spectra2.bias*1e3,spectra2.conductance, linewidth = lw, color = 'C3')

axs[0].plot(spectra1.bias*1e3,spectra1.conductance, linewidth = lw, color = 'grey')
axs[0].plot(spectra3.bias*1e3,spectra3.conductance, linewidth = lw, color = 'C0')

# axis limits
axs[0].set_xlim([-4.5, 4.5])
axs[1].set_xlim([-4.5, 4.5])
axs[0].set_ylim([-2.5, 18])
axs[1].set_ylim([-2.5, 18])

axs[0].set_ylim([-0.5, 8])
axs[1].set_ylim([-0.5, 8])

# axis labels
axs[1].set_xlabel('Sample bias (mV)')
#axs[1].set_xlabel('Sample bias (mV)')

axs[0].set_ylabel(r'Conductance (G$_N$)')
axs[1].set_ylabel(r'Conductance (G$_N$)')
#fig3.tight_layout(pad=0.3) 

fig3.savefig('Spectra_v3.png', 
            dpi=600, # probably not needed for PDF, but I'm writing it anyway
            transparent=True, # you probably want this one. Otherwise you'll have to remove background every time in Illustrator ...
            bbox_inches = 'tight'
            )



