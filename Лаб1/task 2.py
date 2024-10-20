# TODO Найдите количество книг, которое можно разместить на дискете
#Информационный объем дискеты равен
inform_V_disceti_Mb = 1.44
inform_V_disceti_Kb = 1.44 * 1024
inform_V_disceti_bytes = inform_V_disceti_Kb * 1024
pages_in_book = 100
stripes_in_page = 50
simbols_in_page = 25
one_simbol_memory = 4
summary_simbols_in_book = simbols_in_page * stripes_in_page * pages_in_book
summary_memory_for_one_book = one_simbol_memory * summary_simbols_in_book
kolichestvo_knig_na_diskete = inform_V_disceti_bytes // summary_memory_for_one_book
print("Количество книг, помещающихся на дискету:", int(kolichestvo_knig_na_diskete))
