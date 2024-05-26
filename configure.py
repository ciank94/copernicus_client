import copernicusmarine as cop


class File:

    def __init__(self, cmems_path, data_id, y1, y2):
        self.case = "norm_"
        self.month_end = None
        self.month_start = None
        self.config_duration()  # Uses case to specify start and end dataes extracted from cmems
        self.min_depth = 40
        self.max_depth = 80
        self.min_lon = -70
        self.max_lon = -31
        self.min_lat = -73
        self.max_lat = -50
        self.data_id = data_id
        self.cmems_path = cmems_path
        self.start_date = y1 + self.month_start
        self.end_date = y2 + self.month_end
        self.var = ["uo", "vo"]
        if y1 == y2:
            self.cmems_data = (self.cmems_path + 'CMEMS_GLPHYS_D_' + self.case + self.start_date[:4] + '.nc')
        else:
            self.cmems_data = (self.cmems_path + 'CMEMS_GLPHYS_D_' + self.case + self.start_date[:4] +
                               '_' + self.end_date[:4] + '.nc')
        return

    def download_set(self):

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
                   output_filename=self.cmems_data,
                   output_directory=self.cmems_path
                   )
        return

    def config_duration(self):
        if self.case == "SG_S_":
            print("DOWNLOADING: Case SG_short")
            month_start = "-05-01"
            month_end = "-09-30"
        else:
            print("DOWNLOADING standard file")
            month_start = "-01-01"
            month_end = "-12-31"

        self.month_start = month_start + "T00:00:00"
        self.month_end = month_end + "T23:59:59"
        return
