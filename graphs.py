import os 
import pandas as pd
currentWorkingDir =  os.getcwd()
outputDataDir = currentWorkingDir + '/dep/kalman-soc/data/'
dfProcessedSensorDataEnhanced = pd.read_csv(outputDataDir + 'EVLKpN_20210817-20210830_enhanced_processed_sensor_data.zip')  

#Matplotlib
#dfProcessedSensorDataEnhanced.plot()
#plt.show()

#Plotly
pd.options.plotting.backend = "plotly"
fig = dfProcessedSensorDataEnhanced.plot()
fig.update_layout(title_text='<b> Overview  </b>', title_x=0.5)
fig.show()
fig.write_image("overview.pdf")
-m 