class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
        print(f"Node {data} ditambahkan.\n")

    def delete_node(self, key):
        if self.head is None:
            print("List kosong.\n")
            return

        curr = self.head
        while True:
            if curr.data == key:
                if curr.next == curr:  # hanya satu node
                    self.head = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head:
                        self.head = curr.next
                print(f"Node {key} dihapus.\n")
                return
            curr = curr.next
            if curr == self.head:
                break
        print(f"Node {key} tidak ditemukan.\n")

    def display_forward(self):
        if self.head is None:
            print("List kosong.\n")
            return
        print("Isi Linked List (maju):")
        curr = self.head
        while True:
            print(f"{curr.data}", end=" <-> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(kembali ke awal)\n")

    def display_backward(self):
        if self.head is None:
            print("List kosong.\n")
            return
        print("Isi Linked List (mundur):")
        curr = self.head.prev
        while True:
            print(f"{curr.data}", end=" <-> ")
            curr = curr.prev
            if curr == self.head.prev:
                break
        print("(kembali ke akhir)\n")

def menu():
    dll = DoublyCircularLinkedList()
    while True:
        print("===== MENU =====")
        print("1. Tambah Node")
        print("2. Hapus Node")
        print("3. Tampilkan List (maju)")
        print("4. Tampilkan List (mundur)")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            data = int(input("Masukkan data: "))
            dll.add_last(data)
        elif pilihan == '2':
            key = int(input("Masukkan data yang ingin dihapus: "))
            dll.delete_node(key)
        elif pilihan == '3':
            dll.display_forward()
        elif pilihan == '4':
            dll.display_backward()
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    menu()
