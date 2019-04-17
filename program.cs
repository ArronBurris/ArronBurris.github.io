using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Hello World");

            String userChoice;

            do
            {
                Console.WriteLine("Please enter your favorite color:");
                userChoice = Console.ReadLine();
                //Console.WriteLine("You chose:" + userChoice);//
            } while (userChoice == null);


            switch (userChoice)
            {
                case "red":
                    Console.WriteLine("You chose Red!");
                    break;
                case "blue":
                    Console.WriteLine("You chose Blue!");
                    break;
                default:
                    Console.WriteLine("You chose something else");
                    break;

            }





            Console.ReadKey();
        }
    }
}
