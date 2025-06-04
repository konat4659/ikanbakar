class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        print(f"Node {data} ditambahkan.\n")

    def delete_node(self, key):
        if self.head is None:
            print("List kosong.\n")
            return

        curr = self.head
        while curr:
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next  # Node pertama
                if curr.next:
                    curr.next.prev = curr.prev
                print(f"Node {key} dihapus.\n")
                return
            curr = curr.next

        print(f"Node {key} tidak ditemukan.\n")

    def display_forward(self):
        if self.head is None:
            print("List kosong.\n")
            return
        print("Isi Linked List (maju):")
        curr = self.head
        while curr:
            print(f"{curr.data}", end=" <-> ")
            curr = curr.next
        print("None\n")

    def display_backward(self):
        if self.head is None:
            print("List kosong.\n")
            return
        print("Isi Linked List (mundur):")
        curr = self.head
        while curr.next:
            curr = curr.next
        while curr:
            print(f"{curr.data}", end=" <-> ")
            curr = curr.prev
        print("None\n")

def menu():
    dll = DoublyLinkedList()
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
