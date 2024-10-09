using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PlayFair.DataEncryption
{
    public interface IDataEncryption
    {
        string Encrypt(string plainText, string key);
        string Decrypt(string cipherText, string key);
    }
}
