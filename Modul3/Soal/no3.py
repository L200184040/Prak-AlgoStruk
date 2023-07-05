# Terkait linked list, buatlah fungsi untuk:
# # 1. Mencari data yang isinya tertentu: cari(head,yang_dicari)
def cari(head,yang_dicari):
    curNode=head
    while curNode is not None:
        if curNode.data==yang_dicari:
            return True
        curNode=curNode.next
    return False

# 2. Menambah suatu simpul di awal: tambahDepan(head)
def tambahDepan(head,data):
    newNode=Node(data)
    newNode.next=head
    return newNode

# 3. Menambah suatu simpul di akhir: tambahAkhir(head)
def tambahAkhir(head,data):
    newNode=Node(data)
    curNode=head
    while curNode.next is not None:
        curNode=curNode.next
    curNode.next=newNode
    return head

# 4. Menyisipkan suatu simpul di mana saja: tambah(head,posisi)
def tambah(head,posisi,data):
    newNode=Node(data)
    curNode=head
    while curNode.data!=posisi:
        curNode=curNode.next
    newNode.next=curNode.next
    curNode.next=newNode
    return head

# 5. Menghapus suatu simpul di awal, di akhir, atau di mana saja: hapus(posisi)
def hapus(head,posisi):
    curNode=head
    if curNode.data==posisi:
        head=curNode.next
        return head
    while curNode.next.data!=posisi:
        curNode=curNode.next
    curNode.next=curNode.next.next
    return head