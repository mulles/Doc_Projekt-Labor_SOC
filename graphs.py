import os 
import pandas as pd
from matplotlib.pylab import *
currentWorkingDir =  os.getcwd()
outputDataDir = currentWorkingDir + '/dep/kalman-soc/data/'
# dfProcessedSensorDataEnhanced = pd.read_csv(outputDataDir + 'mppt-1210-hus_2021-05-28T20:10:00.000Z-2021-05-29T02:19:00.000Z_enhanced_processed_sensor_data.zip')  
# #mppt-1210-hus_2021-05-05T16:11:00.000Z-2021-05-29T00:19:00.000Z_enhanced_processed_sensor_data.zip
# x = dfProcessedSensorDataEnhanced.index /60
# yEKF = dfProcessedSensorDataEnhanced.kalman_soc * 10
# ySoCLS = dfProcessedSensorDataEnhanced.SoC_LibreSolar * 10
# # deviation = yEKF/ySoCLS *100 # in % 
# # rc('text', usetex=True)
# # rc('font', **{'family':'serif', 'serif':['Times']})
# # rc('font', size=10.0)			
# # rc('legend', fontsize=10.0)
# #x = linspace(0, 3*pi)
# #figure(figsize=(6,2))
# plot(x,yEKF,label='kalman_soc') 
# plot(x,ySoCLS,label='SoC_LibreSolar') #,linestyle='dashed'
# #plot(x,deviation)
# xlabel(r'time (min)')
# ylabel(r'SoC (%)')
# grid()
# #xticks(arange(0, 4*pi, pi), ('$0$',
# #'$\pi$', '$2\pi$', '$3\pi$'))
# #axis([0, 3*pi, -1, 1])
# legend(loc='lower right')
# savefig('mppt-1210-hus-2021-05-28T20:10:00.000Z-2021-05-29T02:19:00.000Z-librevskalman.pdf', bbox_inches='tight')
# dfProcessedSensorDataEnhanced.plot()
# xlabel(r'time (min)')
# grid()
# #plt.show()
# #savefig('matplotnotworking.pdf')

dfProcessedSensorDataEnhanced = pd.read_csv(outputDataDir + 'EVLKpN_20210817-20210830_enhanced_processed_sensor_data.zip')  
dfProcessedSensorDataEnhanced.index = dfProcessedSensorDataEnhanced.index  *5 / 60
x = dfProcessedSensorDataEnhanced.index
yEKF = dfProcessedSensorDataEnhanced.kalman_soc * 10
ySoCLS = dfProcessedSensorDataEnhanced.SoC_LibreSolar * 10
# rc('text', usetex=True)
# rc('font', **{'family':'serif', 'serif':['Times']})
# rc('font', size=10.0)			
# rc('legend', fontsize=10.0)
#x = linspace(0, 3*pi)
#figure(figsize=(6,2))
plot(x,yEKF,label='kalman_soc') 
plot(x,ySoCLS,label='SoC_LibreSolar') #,linestyle='dashed'
xlabel(r'time (h)')
ylabel(r'SoC (%)')
grid()
#xticks(arange(0, 4*pi, pi), ('$0$',
#'$\pi$', '$2\pi$', '$3\pi$'))
#axis([0, 3*pi, -1, 1])
legend(loc='lower right')
savefig('EVLKpN_20210817-20210830-librevskalman.pdf', bbox_inches='tight')
dfProcessedSensorDataEnhanced.plot()
xlabel(r'time (h)')
grid()
plt.show()
#savefig('matplotnotworking.pdf')