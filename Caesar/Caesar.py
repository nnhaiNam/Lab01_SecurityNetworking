def caesar(text, key, mode='ma'):
    kq = ""
    for c in text:
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            if mode == 'ma':
                n = (ord(c) - offset + key) % 26
            else:
                n = (ord(c) - offset - key) % 26
            kq += chr(n + offset)
        else:
            kq += c
    return kq

def ma_hoa(text, key):
    return caesar(text, key, 'ma')

def giai_ma(text, key):
    return caesar(text, key, 'giai')

def vet_can(text):
    results = []
    for k in range(26):
        decrypted = giai_ma(text, k)
        preview = decrypted[:50] + "..." if len(decrypted) > 50 else decrypted
        results.append((k, preview))
    return results

def show_full_result(text, key):
    print(f"\nKết quả đầy đủ cho khóa {key}:")
    print(giai_ma(text, key))

def main():
    menu = {
        '1': ('Mã hóa', ma_hoa),
        '2': ('Giải mã', giai_ma),
        '3': ('Tấn công vét cạn', vet_can),
        '4': ('Thoát', exit)
    }

    while True:
        print("\nChương trình Mã hóa Caesar")
        for key, (name, _) in menu.items():
            print(f"{key}. {name}")
        
        chon = input("Chọn (1-4): ")
        
        if chon not in menu:
            print("Lựa chọn không hợp lệ. Thử lại.")
            continue
        
        if chon == '4':
            print("Tạm biệt!")
            break
        
        text = input(f"Nhập văn bản cần {menu[chon][0].lower()}: ")
        if chon in ['1', '2']:
            key = int(input("Nhập khóa (0-25): "))
            print("Kết quả:", menu[chon][1](text, key))
        else:
            results = menu[chon][1](text)
            for key, preview in results:
                print(f"Khóa {key}: {preview}")
            
            while True:
                view_full = input("\nNhập số khóa để xem kết quả đầy đủ (hoặc 'q' để quay lại): ")
                if view_full.lower() == 'q':
                    break
                try:
                    key = int(view_full)
                    if 0 <= key <= 25:
                        show_full_result(text, key)
                    else:
                        print("Khóa không hợp lệ. Vui lòng nhập số từ 0 đến 25.")
                except ValueError:
                    print("Vui lòng nhập một số hợp lệ hoặc 'q' để quay lại.")

if __name__ == "__main__":
    main()