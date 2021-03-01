# Tucil2_13519009

## Implementasi Algoritma Decrease and Conquer pada Topological Sorting
- Data kode kuliah dan pre-requisitenya direpresentasikan dalam DAG (Directed Acyclic Graph)
- Untuk setiap simpul/vertex (dalam hal ini adalah kode kuliah) yang memiliki degree-in sama dengan 0, akan dihilangkan dari DAG, dan kemudian di list
- Untuk setiap simpul/vertex(kode kuliah) yang keluar dari simpul tersebut degree-nya akan dikurangi 1
- Lakukan kedua langkah tersebut hingga semua simpul/vertex terlist

## Requirement Program
- Untuk menjalankan program ini cukup install python 3.0

## Cara Menjalankan Program
- Jalankan main_13519009.py
- Untuk mengganti file test.txt dapat dilakukan dengan membuka fungsi_13519009.py, kemudian ubah path yaitu '../test/test2.txt'
  pada bagian test2.txt dapat dirubah dengan file test.txt lainnya yang terdapat pada folder test
  
## Author
Mochammad Fatchur Rochman (13519009)