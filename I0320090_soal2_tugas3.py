#Soal no 2 tugas 3

dict = {'Nama': 'Salma Ardelia Irfani',
        'Hobi': ['fotografi' , 'jalan-jalan', 'membaca novel'],
        'Sosialmedia': {
                'Instagram': 'salmaardelia_',
                'Line': 'salmaardelia_',
                'Twitter': '@salmaardelia24'},
        'Lagufavorit': ['Drivers Lisence' , 'Back At One', 'Imagination'],
        'Makananfavorit': ['Nasi uduk' , 'Ayam goreng' , 'Nasi goreng'] }
print(dict)

#Mengubah salah satu hobi dan sosial media
dict['Hobi'][2] = 'Mendengarkan musik'
dict['Sosialmedia'] ['Instagram'] = 'sardel.ia'

print(dict)

#Menghapus 2 makanan favorit
del dict ['Makananfavorit'][1]
del dict ['Makananfavorit'][0]

print(dict)

#Menambah 1 hobi
#dict.update({'Hobi':'Tidur'})
dict['Hobi'].append('tidur')
print(dict)