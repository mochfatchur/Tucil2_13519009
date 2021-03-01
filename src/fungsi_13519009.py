# CATATAN : Jika ingin mengubah file.txt yang akan diuji pada program ini
#           dapat mengubah '../test/test5.txt' yang terdapat pada
#           bagian PATH, ubah test5.txt dengan file.txt lainnya yang
#           terdapat pada folder test.

# PATH
path = '../test/test3.txt'

# =========== Fungsi - Fungsi yang berhubungan dengan Graph ===========

# Fungsi Buka File Text dan Membuat List Adjacencynya
def makeListAdja():
    listAdjacency = []
    with open(path, 'r') as file:
        for datas in file:
            listTemp = []
            stringTemp = ''
            data = datas.replace('\n','')
            for data_i in data:
                if(data_i ==','):
                    listTemp = listTemp + [stringTemp]
                    stringTemp = ''
                elif(data_i == '.'):
                    listTemp = listTemp + [stringTemp]
                    listAdjacency = listAdjacency + [listTemp]
                    listTemp = []
                elif(data_i != ' '):
                    stringTemp = stringTemp + data_i
    
    return listAdjacency

# Fungsi Mencari Panjang list
def listLength(lis):
    leng = 0
    for data in lis:
        leng += 1
    return leng


# Fungsi Membuat list Vertex 
def makeListVertex():
    listAdja = makeListAdja()
    lengList = listLength(listAdja)
    listVertex = []

    for i in range(lengList):
        listVertex = listVertex + [listAdja[i][0]]

    return listVertex


# Fungsi Menghitung Vertex
def countVertex(V):
    count = 0
    for i in V :
        count += 1
    return count


# Fungsi Membuat Adjacency Matrix
def makeAdjaMatrix(listAdja,listVertex):
    lengMatrix = listLength(listVertex)
    AdjaMatrix = [[0 for j in range(lengMatrix)] for i in range(lengMatrix)]

    lengListAdja = listLength(listAdja)
    lengListVertex = listLength(listVertex)

    for vi in listVertex:
        i_loop = 0
        found = False
        i = 0
        while(i_loop<lengListAdja and (not found)):
            if(vi == listAdja[i_loop][0]):
                found = True
                i = i_loop
                i_loop = 0
            else:
                i_loop += 1
        found = False
        
        # isi Adjacency Matrix
        lengListAdjai = listLength(listAdja[i])
        for j in range(1,lengListAdjai):
            for k in range(lengListVertex):
                if(listAdja[i][j] == listVertex[k]):
                    AdjaMatrix[k][i] += 1

    return AdjaMatrix


# Fungsi Menghitung degree-in (din) pada suatu Vertex
def dinV(j,AdjaMatrix):
    lengAdjaMatrix = listLength(AdjaMatrix)
    din = 0
    for i in range(lengAdjaMatrix):
        din += AdjaMatrix[i][j]
    
    return din


# Fungsi untuk Mengetahui Apakah keduanya tetangga-an
def isTetangga(i,j):
    listAdj = makeListAdja()
    listVer = makeListVertex()
    adjaMatrix = makeAdjaMatrix(listAdj, listVer)
    
    if(adjaMatrix[i][j] == 1 or adjaMatrix[j][i] == 1):
        return True
    else:
        return False


# Fungsi untuk mengetahui index dari suatu Vertex
def getIndexVertex(V):
    listVer = makeListVertex()
    index = -1
    x = 0
    for vertex in listVer:
        if(V == vertex):
            index = x
        x += 1
    if(index == -1):
        print("\nSimpul tersebut tidak ada di list Vertex ini")
    else:
        return index


# Algoritma Topological Sorting dengan Decrease and Conquer
def TopologicalSorting(listAdja,listVertex):

    AdjaMatrix = makeAdjaMatrix(listAdja,listVertex)
    lengAdjaMatrix = listLength(AdjaMatrix)
    lengListVertex = listLength(listVertex)
    
    listSorted = []
    listVertexIn = [False for j in range(lengListVertex)]

    allVertexListed = False
    vertexIn = 0
    nVertex = countVertex(listVertex)

    while(not allVertexListed):
        for j in range (lengListVertex):
            # cek apakah sudah dimasukkan ke list Sorted
            In = listVertexIn[j]
            if(not In):
                din = dinV(j,AdjaMatrix)
                if(din == 0):
                    listSorted = listSorted + [listVertex[j]]
                    listVertexIn[j] = True
                    vertexIn += 1
                    # Menghapus Vertex listVertex[j] pada AdjaMatrix
                    for i in range(lengListVertex):
                        AdjaMatrix[j][i] = 0
            
        # Cek apakah semua vertex sudah masuk ke listSorted
        if(vertexIn == nVertex):
            allVertexListed = True
    
    return listSorted

# =========== Tulis ===========

# Prosedur Tulis Semester
def printSemester(i_semester, matkul):
    listSemester = ['I','II','III','IV','V','VI','VII','VIII']
    if(i_semester == 0 or i_semester == 4):
        print("Semester",listSemester[i_semester],'   :',matkul)
    elif(i_semester == 1 or i_semester == 3 or i_semester == 5):
        print("Semester",listSemester[i_semester],'  :',matkul)
    elif(i_semester == 2 or i_semester == 6):
        print("Semester",listSemester[i_semester],' :',matkul)
    else:
        print("Semester",listSemester[i_semester],':',matkul)


# Prosedur Tulis Solusi
def printSolusi(Solusi):
    lengSolusi = listLength(Solusi)
    nSemester = 8
    listMatkul = makeListVertex()

    semester_i = 0
    i_listSolusi = 0
    i_v = getIndexVertex(Solusi[i_listSolusi])
    j_v = getIndexVertex(Solusi[i_listSolusi+1])
    countMatkul = 0
    complete = False
    
    while(semester_i < nSemester and (not complete)):
        strMatkulSemester_i = Solusi[i_listSolusi]
        i_listSolusi += 1
        countMatkul += 1
        tetangga = isTetangga(i_v, j_v)
        # Melakukan pendataan mata kuliah (Vertex) apa yang bisa dimasukkan pada semester ini
        while(not tetangga and (not complete)):
            strMatkulSemester_i = strMatkulSemester_i + ', ' + listMatkul[j_v]
            countMatkul += 1
            if(countMatkul == lengSolusi):
                complete = True
            else:
                i_listSolusi += 1
                j_v = getIndexVertex(Solusi[i_listSolusi])
                tetangga = isTetangga(i_v,j_v)
        # Melakukan pencetakan ke layar matkul semester ini
        printSemester(semester_i, strMatkulSemester_i)
        # melakukan pengecekan untuk anggota listSolusi selanjutnya
        if(lengSolusi - countMatkul >= 2):
            i_v = getIndexVertex(Solusi[i_listSolusi])
            j_v = getIndexVertex(Solusi[i_listSolusi+1])
        else:
            if(countMatkul == lengSolusi):
                complete = True

        semester_i += 1


# Prosedur Tulis Soal
def printSoal():
    print("Daftar Mata kuliah dan prequisitennya : ")
    with open(path,'r') as file:
        soal = file.read()
    print(soal,'\n')


















