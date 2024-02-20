original_list = ["1804 Bodo", "1806 Narvik", "1811 Bindal", "1812 Somna", "1813 Bronnoy", "1815 Vega", "1816 Vevelstad",
    "1818 Heroy", "1820 Alstahaug", "1822 Leirfjord", "1824 Vefsn", "1825 Grane", "1826 Hattfjelldal", "1827 Donna",
    "1828 Nesna", "1832 Hemnes", "1833 Rana", "1834 Luroy", "1835 Trena", "1836 Rodoy", "1837 Meloy", "1838 Gildeskal",
    "1839 Beiarn", "1840 Saltdal", "1841 Fauske", "1845 Sorfold", "1848 Steigen", "1851 Lodingen", "1853 Evenes",
    "1856 Rost", "1857 Veroy", "1859 Flakstad", "1860 Vestvagoy", "1865 Vagan", "1866 Hadsel", "1867 Bo", "1868 Oksnes",
    "1870 Sortland", "1871 Andoy", "1874 Moskenes", "1875 Hamaroy"]

number_list = []
string_list = []

for item in original_list:
    if isinstance(item, str):
        split_item = item.split(' ', 1)
        number_list.append(int(split_item[0]))
        string_list.append(split_item[1])
    else:
        number_list.append(item)

print("Number List:", number_list)
print("String List:", string_list)
