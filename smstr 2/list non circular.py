class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        print(f"Node {data} ditambahkan.\n")

    def delete_node(self, key):
        if not self.head:
            print("List kosong.\n")
            return

        curr = self.head
        prev = None

        while curr:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                print(f"Node {key} dihapus.\n")
                return
            prev = curr
            curr = curr.next

        print(f"Node {key} tidak ditemukan.\n")

    def display(self):
        if not self.head:
            print("List kosong.\n")
            return
        print("Isi Linked List:")
        curr = self.head
        while curr:
            print(f"{curr.data}", end=" -> ")
            curr = curr.next
        print("None\n")

def menu():
    ll = LinkedList()
    while True:
        print("===== MENU =====")
        print("1. Tambah Node")
        print("2. Hapus Node")
        print("3. Tampilkan List")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            data = int(input("Masukkan data: "))
            ll.add_last(data)
        elif pilihan == '2':
            key = int(input("Masukkan data yang ingin dihapus: "))
            ll.delete_node(key)
        elif pilihan == '3':
            ll.display()
        elif pilihan == '4':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    menu()
