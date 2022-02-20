# Que3 Get Process of Server and create a report in CSV and HTML format

print('Harry Goyal')
# code start
import psutil
import pandas as pd
# Iterate over all running process
process = []
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object
        processName = proc.name()
        processID = proc.pid
        dic = {'process_name': processName, 'process_id': processID}
        process.append(dic)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
df = pd.DataFrame(data=process)
df.to_csv(r'que3_process.csv', index=False, header=True)  # csv file created with processes
df.to_html('que3_process.html')                           # html file created with processes
#code end