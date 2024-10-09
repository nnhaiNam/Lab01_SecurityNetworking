namespace PlayFair
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*  PlayFair_Algorithm fair_Algorithm = new PlayFair_Algorithm();
              Console.WriteLine("Enter plaintext: ");
              string plaintext = Console.ReadLine();
              Console.WriteLine("Enter key: ");
              string key=Console.ReadLine();

              PlayFair_Algorithm playFair_Algorithm = new PlayFair_Algorithm();
              string result=playFair_Algorithm.Decrypt(plaintext, key); 
              Console.WriteLine(result);*/

            bool loop = true;
            while(loop)
            {
                int choice;
                Console.WriteLine();
                Console.WriteLine("------------------------------");
                Console.WriteLine("Please select your choice: ");
                Console.WriteLine("1.Encryption Data");
                Console.WriteLine("2.Decryption Data");
                Console.WriteLine("3. Exit");
                Console.WriteLine("------------------------------");
                
                choice=int.Parse(Console.ReadLine());
                switch (choice)
                {
                    case 1:
                        {
                            Console.WriteLine("Enter your plaintext: ");
                            string plainttext = Console.ReadLine();
                            Console.WriteLine("Enter key: ");
                            string key = Console.ReadLine();
                            Console.WriteLine();
                            Console.WriteLine("=================");
                            PlayFair_Algorithm playFair_Algorithm = new PlayFair_Algorithm();
                            string result = playFair_Algorithm.Encrypt(plainttext, key);
                            Console.WriteLine("=================");
                            Console.WriteLine();
                            Console.WriteLine("CipherText: ");
                            Console.WriteLine(result);


                            break;
                        }
                       
                    case 2:
                        {
                            Console.WriteLine("Enter your ciphertext: ");
                            string ciphertext = Console.ReadLine();
                            Console.WriteLine("Enter key: ");
                            string key = Console.ReadLine();
                            Console.WriteLine();
                            Console.WriteLine("=================");
                            PlayFair_Algorithm playFair_Algorithm = new PlayFair_Algorithm();
                            string result = playFair_Algorithm.Decrypt(ciphertext, key);
                            Console.WriteLine("=================");
                            Console.WriteLine();
                            Console.WriteLine("PlainText: ");
                            Console.WriteLine(result);
                            break;
                        }
                       

                    case 3:

                        Console.WriteLine("Goodbye!");
                        loop = false;
                        break;

                    default:

                        Console.WriteLine("Goodbye!");
                        loop = false;
                        break;
                }


            }


        }
    }
}
