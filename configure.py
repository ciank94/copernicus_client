import copernicusmarine as cop
import sys


class File:

    def __init__(self, outfile_path, config_path, key, y):
        self.case = "full_"
        self.month_end = None
        self.month_start = None
        self.config_duration()  # Uses case to specify start and end dataes extracted from cmems
        self.min_depth = 70
        self.max_depth = 100
        self.min_lon = -70
        self.max_lon = -31
        self.min_lat = -73
        self.max_lat = -50
        self.config_path = config_path
        self.outfile_path = outfile_path
        self.start_date = y + self.month_start
        self.end_date = y + self.month_end

        if key == 'DPHY':
            save_key = 'CMEMS_GLPHYS_D_'
            self.data_id = 'cmems_mod_glo_phy_my_0.083deg_P1D-m'
            self.var = ["uo", "vo", "thetao"]
        elif key == 'DBIO':
            save_key = 'CMEMS_GLBIO_D_'
            self.data_id = 'cmems_mod_glo_bgc_my_0.25deg_P1D-m'
            self.var = ["chl", "o2"]
        elif key == 'TEMP':
            save_key = 'CMEMS_TEMP_'
            self.data_id = 'cmems_mod_glo_bgc_my_0.25deg_P1D-m'
            self.var = ["uo", "vo", "thetao"]
            self.min_lon = -41
            self.max_lon = -32
            self.min_lat = -56
            self.max_lat = -51
            y1 = str(2006)
            y2 = str(2021)
            self.start_date = y1 + self.month_start
            self.end_date = y2 + self.month_end
        else:
            sys.exit("Invalid key for downloading file")


        self.outfile = (self.outfile_path + save_key + self.case + self.start_date[:4] + '.nc')
        self.download_set()
        return

    def download_set(self):
        print(" ##################### ")
        print("Preparing to download dataset")
        print("filename = " + self.outfile)
        print(" ##################### ")
        cop.subset(dataset_id=self.data_id,
                   variables= self.var,
                   start_datetime=self.start_date,
                   end_datetime=self.end_date,
                   minimum_longitude=self.min_lon,
                   maximum_longitude=self.max_lon,
                   minimum_latitude=self.min_lat,
                   maximum_latitude=self.max_lat,
                   minimum_depth=self.min_depth,
                   maximum_depth=self.max_depth,
                   output_filename=self.outfile,
                   output_directory=self.outfile_path,
                   credentials_file=self.config_path + ".copernicusmarine-credentials",
                   force_download=True
                   )
        return

    def config_duration(self):
        if self.case == "SG_S_":
            print("DOWNLOADING: Case SG_short")
            month_start = "-05-01"
            month_end = "-09-30"
        elif self.case == "test_":
            self.min_depth = 0
            self.max_depth = 1
            month_start = "-05-01"
            month_end = "-05-10"
            print("DOWNLOADING test file")
        else:
            print("DOWNLOADING standard file")
            month_start = "-01-01"
            month_end = "-12-31"

        self.month_start = month_start + "T00:00:00"
        self.month_end = month_end + "T23:59:59"
        return
