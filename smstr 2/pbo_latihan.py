class LoginSystem:
    def __init__(self):
        # Private list 2 dimensi: [ [username, password], ... ]
        self.__users = [
            ["admin", "admin123"],
            ["user1", "password1"],
            ["user2", "password2"]
        ]

    def login(self):
        print("\n=== LOGIN ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if self.__authenticate(username, password):
            print(f"Login berhasil! Selamat datang, {username}.")
        else:
            print("Login gagal! Username atau password salah.")

    def __authenticate(self, username, password):
        # Private method untuk autentikasi
        for user in self.__users:
            if user[0] == username and user[1] == password:
                return True
        return False

# --- Program utama ---

if __name__ == "__main__":
    system = LoginSystem()
    system.login()
