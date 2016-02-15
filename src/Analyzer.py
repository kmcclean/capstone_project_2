__author__ = 'casey & kevin'


class Analyzer:

    def best_units_total(self, best_selling_list):
        f = open("best_selling_merch.txt", "w")
        for item in best_selling_list:
            f.write(str(item) + "\n")
        f.close()

    def best_units_gross(self, gross_selling_list):
        f = open("best_gross_merch.txt", "w")
        for item in gross_selling_list:
            f.write(str(item) + "\n")
        f.close()

    def best_units_net(self, net_selling_list):
        f = open("net_gross_merch.txt", "w")
        for item in net_selling_list:
            f.write(str(item) + "\n")
        f.close()
