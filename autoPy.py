from datetime import datetime
filename=datetime.now().strftime('%Y%m%d_%H_%M_%S')+'.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(datetime.now().strftime('%Y%m%d-%H:%M:%S'))
