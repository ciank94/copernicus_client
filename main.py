from configure import File
config_path = '/cluster/projects/nn9828k/Cian_sinmod/copernicus_client/'
outfile_path = config_path + 'results/'  # 'Create results folder
data_id = "cmems_mod_glo_phy_my_0.083deg_P1D-m"
y_start = 2000
y_end = 2010
for y_i in range(y_start, y_end + 1):
    y1 = str(y_i)
    y2 = str(y_i)
    print('Iteration: ' + y1)
    File(outfile_path, config_path, data_id, y1, y2)





