import os 
import pandas as pd
from matplotlib.pylab import *
currentWorkingDir =  os.getcwd()
outputDataDir = currentWorkingDir + '/dep/kalman-soc/data/'
dfProcessedSensorDataEnhanced = pd.read_csv(outputDataDir + 'EVLKpN_20210817-20210830_enhanced_processed_sensor_data.zip')  

x = dfProcessedSensorDataEnhanced.index *5/60
yEKF = dfProcessedSensorDataEnhanced.kalman_soc * 10
ySoCLS = dfProcessedSensorDataEnhanced.SoC_LibreSolar * 10
# rc('text', usetex=True)
# rc('font', **{'family':'serif', 'serif':['Times']})
# rc('font', size=10.0)			
# rc('legend', fontsize=10.0)
#x = linspace(0, 3*pi)
figure(figsize=(6,2))
plot(x,yEKF,label='kalman_soc') 
plot(x,ySoCLS,label='SoC_LibreSolar') #,linestyle='dashed'
xlabel(r'time (h)')
ylabel(r'SoC (%)')
grid()
#xticks(arange(0, 4*pi, pi), ('$0$',
#'$\pi$', '$2\pi$', '$3\pi$'))
#axis([0, 3*pi, -1, 1])
legend(loc='lower right')
savefig('librevskalman.pdf', bbox_inches='tight')
dfProcessedSensorDataEnhanced.plot()
plt.show()
savefig('matplotoverview.pdf')
