class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def add_last(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        print(f"Node {data} ditambahkan.\n")

    def delete_node(self, key):
        if not self.tail:
            print("List kosong.\n")
            return

        curr = self.tail.next
        prev = self.tail

        while True:
            if curr.data == key:
                if curr == self.tail and curr.next == self.tail:
                    self.tail = None
                else:
                    prev.next = curr.next
                    if curr == self.tail:
                        self.tail = prev
                print(f"Node {key} dihapus.\n")
                return
            prev = curr
            curr = curr.next
            if curr == self.tail.next:
                break
        print(f"Node {key} tidak ditemukan.\n")

    def display(self):
        if not self.tail:
            print("List kosong.\n")
            return
        curr = self.tail.next
        print("Isi Circular Linked List:")
        while True:
            print(f"{curr.data}", end=" -> ")
            curr = curr.next
            if curr == self.tail.next:
                break
        print("(kembali ke awal)\n")

def menu():
    cll = CircularLinkedList()
    while True:
        print("===== MENU =====")
        print("1. Tambah Node")
        print("2. Hapus Node")
        print("3. Tampilkan List")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            data = int(input("Masukkan data: "))
            cll.add_last(data)
        elif pilihan == '2':
            key = int(input("Masukkan data yang ingin dihapus: "))
            cll.delete_node(key)
        elif pilihan == '3':
            cll.display()
        elif pilihan == '4':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    menu()
