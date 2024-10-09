#include <iostream>
#include <string>
using namespace std;

// Hàm mã hóa Vigenère
string vigenereEncrypt(string plaintext, string key) {
    string ciphertext = "";
    int keyLength = key.length();
    for (int i = 0; i < plaintext.length(); i++) {
        char p = plaintext[i] - 'A';
        char k = key[i % keyLength] - 'A';
        char c = (p + k) % 26 + 'A';
        ciphertext += c;
    }
    return ciphertext;
}

// Hàm giải mã Vigenère
string vigenereDecrypt(string ciphertext, string key) {
    string plaintext = "";
    int keyLength = key.length();
    for (int i = 0; i < ciphertext.length(); i++) {
        char c = ciphertext[i] - 'A';
        char k = key[i % keyLength] - 'A';
        char p = (c - k + 26) % 26 + 'A';
        plaintext += p;
    }
    return plaintext;
}

int main() {
    string plaintext, ciphertext, key;
    cout << "Nhap van ban can ma hoa (viet hoa): ";
    cin >> plaintext;
    cout << "Nhap van ban can giai ma (viet hoa): ";
    cin >> ciphertext;
    cout << "Nhap khoa (viet hoa): ";
    cin >> key;

    string encryptedText = vigenereEncrypt(plaintext, key);
    cout << "Van ban da ma hoa: " << encryptedText << endl;

    string decryptedText = vigenereDecrypt(ciphertext, key);
    cout << "Van ban giai ma: " << decryptedText << endl;

    return 0;
}
