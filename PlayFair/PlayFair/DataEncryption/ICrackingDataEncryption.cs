using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PlayFair.DataEncryption
{
    public interface ICrackingDataEncryption: IDataEncryption
    {
        IEnumerable<string> CrackingDecrypt(string cipherText);
    }
}
