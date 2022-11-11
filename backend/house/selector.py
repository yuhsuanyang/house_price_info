from .update_db import house2df


class ItemSelector(object):

    def __init__(self):
        self.all_data = house2df()
        self.all_data['num_rooms'] = self.all_data['room'].replace(
            ['開放式格局', ''], ['0房', '0房'])
        self.all_data['num_rooms'] = self.all_data['num_rooms'].apply(
            lambda x: int(x[0]))
        self.error_message = 'query condition invalid'

    def query_by_str(self, col_name, value):
        assert col_name in ['region_name', 'section_name'], self.error_message
        self.all_data = self.all_data[self.all_data[col_name] == value]
        return self.all_data

    def query_by_range(self, col_name, min_, max_):
        min_ = int(min_) if min_ != '' else 0
        max_ = int(max_) if max_ != '' else None
        assert col_name in ['price', 'area', 'houseage'], self.error_message
        if not max_:
            self.all_data = self.all_data[self.all_data[col_name] >= min_]
        else:
            self.all_data = self.all_data[(self.all_data[col_name] >= min_)
                                          & (self.all_data[col_name] <= max_)]
        return self.all_data

    def query_by_num(self, col_name, value):
        assert col_name in ['num_rooms'], self.error_message
        value = int(value)
        if value:  # !0
            self.all_data = self.all_data[self.all_data[col_name] == value]

        return self.all_data
