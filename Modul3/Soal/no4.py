#Terkait doubly linked list, buatlah fungsi untuk:
# 1. Mengunjungi dan mencetak data dari tiap simpul dari depan dan dari belakang
def kunjungi(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode=curNode.next

def kunjungiBalik(tail):
    curNode=tail
    while curNode is not None:
        print(curNode.data)
        curNode=curNode.prev

#2. Menambah suatu simpul di awal
def tambahAwal(head,data):
    newNode=Node(data)
    newNode.next=head
    head.prev=newNode
    return newNode

#3. Menambah suatu simpul di akhir
def tambahAkhir(tail,data):
    newNode=Node(data)
    newNode.prev=tail
    tail.next=newNode
    return newNode