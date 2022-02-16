using System;

namespace ATM_Interface
{
    class Program
    {
        //one way i can make this a littl ebit better is to make where individuals have their own seperate values
        //to do this i will have to move most of this into a seperate file 
        //Main method will nott be the thing doing most of the computing 
        //main should be used to make a profile or choose who you are
        static void Main(string[] args)
        {
            int Balance = 1000, withdraw, deposit;
            Console.WriteLine("Welcome to the ATM.");
            Console.WriteLine("How can I help you today?");
            Console.WriteLine("Choose 1 for a Withdrawl");
            Console.WriteLine("Choose 2 to Deposit");
            Console.WriteLine("Choose 3 to Check Balance");
            Console.WriteLine("Choose 4 to EXIT");
            while (true)
            {
                int num = 0;
                string choice = Console.ReadLine(); //this must have an input else it'll break
                num = Convert.ToInt32(choice);

                switch (num)
                {
                    case 1:
                        Console.Write("Entre the amount you would like to withdraw: ");
                        withdraw = Convert.ToInt32(Console.ReadLine());
                        while (withdraw > Balance)
                        {
                            Console.WriteLine("Insufficient Funds please enter an amount lower than " + withdraw);
                            withdraw = Convert.ToInt32(Console.ReadLine());
                        }
                        Withdraw(withdraw);
                        Balance = Balance - withdraw;
                        break;

                    case 2:
                        Console.Write("Enter the amount you would like to Deposit: ");
                        deposit = Convert.ToInt32(Console.ReadLine());
                        while (deposit < 0)
                        {
                            Console.WriteLine("Please deposit a positive amount" );
                            deposit = Convert.ToInt32(Console.ReadLine());
                        }
                        Balance = Balance + deposit;
                        deposit = 0;
                        Console.WriteLine("What else would you like to do?");
                        break;

                    case 3:
                        Console.WriteLine("Your current Balance is: " + Balance);
                        Console.WriteLine("What else would yo ulike to do?");
                        break;

                    case 4:
                        Console.WriteLine("Are You sure you want to exit? Press Y|N");
                        string answer = Console.ReadLine();
                        if ((answer == "y") || (answer == "Y"))
                        {
                            return;
                        }
                        Console.WriteLine("Please select a valid option");
                        break;
                        


                    default:
                        Console.WriteLine("Please select a valid option");
                        break;



                }
            }
        }
        private static int Withdraw(int amount)
        {
            Console.WriteLine("Please collect your cash below.");
           
            return amount;
        }
    }
}
