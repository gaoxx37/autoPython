from datetime import datetime
filename=datetime.now().strftime('%Y%m%d-%H:%M:%S')+'.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(datetime.now().strftime('%Y%m%d-%H:%M:%S'))
