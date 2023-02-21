#include <iostream>
#include <string>
using namespace std;

int main() {

    string alphabet {"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"};
    string key      {"XZNLWEBGJHQDYVTKFUOMPCIASRxznlwebgjhqdyvtkfuompciasr"};

    // cout<<"Enter your secret message: ";
    // string s1;
    // string s2;
    // getline(cin,s1);                                    //read input from keyboard till null character
    // for (size_t i{0};i<s1.length();i++){
    //     int dex=alphabet.find(s1[i]);                   //Get index from alphabet
    //     if (dex!=string::npos)                          //if character found in alphabet
    //     s2+=key[dex];                                   //use index in key and add it to s2 string
    //     else                                            //else use the charcter provided from s1
    //     s2+=s1[i];

    // }
    //     cout<<"\nEncrypting message..."<<endl;
    //     cout<<"\nEncrypted message: "<<s2<<endl;
    //     cout<<"\nDecrypting message..."<<endl;
    //     cout<<"\nDecrypted message: "<<s1<<endl;
    //     cout<<endl;

//                                              Frank's Soultion

string secret_message {};
    cout << "Enter your secret message : ";
    getline(cin, secret_message);

    string encrypted_message {};

    cout << "\nEncrypting message..." << endl;

    for (char c: secret_message) {
        size_t position = alphabet.find(c);
        if (position != string::npos) {
            char new_char {  key.at(position) };
            encrypted_message += new_char;
        } else {
            encrypted_message += c;
        }
    }

    cout << "\nEncrypted message: " << encrypted_message << endl;

    string decrypted_message {};
    cout << "\nDecrypting message..." << endl;

    for (char c: encrypted_message) {
        size_t position = key.find(c);
        if (position != string::npos) {
            char new_char { alphabet.at(position) };
            decrypted_message += new_char;
        } else {
            decrypted_message += c;
        }
    }

    cout << "\nDecrypted message: " << decrypted_message << endl;

    cout << endl;

    return 0;
}