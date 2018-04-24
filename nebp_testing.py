import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
from nebp_response_functions import response_matrix
from experimental_data import unfiltered1
from sandii import iterate
from spectrum import Spectrum
from nebp_spectrum import FluxNEBP
from nebp_unfolded_data import unfolded_data


# nice plots
rc('font', **{'family': 'serif'})
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['lines.linewidth'] = 1.85
rcParams['axes.labelsize'] = 15
rcParams.update({'figure.autolayout': True})

nebp = FluxNEBP(250)

R = response_matrix
f_i = nebp.values
N = unfiltered1.values
sig = unfiltered1.error

sol = iterate(f_i, N, sig, R)
solution = Spectrum(nebp.edges, sol)

from_gravel = unfolded_data['e1_ne_gr']

fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.plot(nebp.step_x, nebp.step_y, color='k', label='Default Spectrum', linewidth=0.7,)
ax.plot(solution.step_x, solution.step_y, color='indigo', label='My Sand-II', linewidth=0.7,)
ax.plot(from_gravel.step_x, from_gravel.step_y, color='goldenrod', label='Gravel', linestyle='--', linewidth=0.7,)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Energy $MeV$')
ax.set_ylabel('Flux $cm^{-2}s^{-1}MeV^{-1}$')
ax.set_xlim(1E-9, 20)
plt.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(frameon=False)
plt.savefig('comparison.png', dpi=300)

# plot difference
fig = plt.figure(1)
ax = fig.add_subplot(111)
percent_error = ((solution.step_y - from_gravel.step_y) / from_gravel.step_y) * 100
ax.plot(solution.step_x, percent_error, color='indigo', label='Differences', linewidth=0.7,)
ax.set_xscale('log')
ax.set_xlabel('Energy $MeV$')
ax.set_ylabel('% Error')
ax.set_xlim(1E-9, 20)
plt.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(frameon=False)
plt.savefig('diffs.png', dpi=300)