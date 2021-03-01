# NIM/Nama      : 13519009/Mochammad Fatchur Rochman
# Program       : Program Aplikasi Topology Sorting dengan Decrease and Conquer

        
# import file
import fungsi_13519009 as f

# ================== Main Program ==================
listAdja = f.makeListAdja()
listVertex = f.makeListVertex()
AdjaMatrix = f.makeAdjaMatrix(listAdja,listVertex)

# Print Soal dari file test.txt yang ada di folder test
f.printSoal()
# Print Hasil data file test.txt setelah dilakukan Topological Sorting
print("Urutan Penyusunan Mata Kuliah (dari kiri ke kanan) Setelah dilakukan Topological Sorting : ")
print(f.TopologicalSorting(listAdja,listVertex))
print()
# Print Solusi Penyusunan Mata Kuliah yang memungkinkan
print("Penyusunan rencana kuliah yang memungkinkan adalah sebagai berikut : ")
Solusi = f.TopologicalSorting(listAdja,listVertex)
f.printSolusi(Solusi)
print()
