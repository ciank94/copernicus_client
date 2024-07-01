from configure import File
config_path = '/cluster/projects/nn9828k/Cian_sinmod/copernicus_client/'
outfile_path = config_path + 'results/'  # 'Create results fo
key = 'DPHY'
y_start = 2016
y_end = 2022
for y_i in range(y_start, y_end + 1):
    y = str(y_i)
    print('Iteration: ' + y)
    File(outfile_path, config_path, key, y)





