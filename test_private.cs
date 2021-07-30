using System;
using System.Reflection;

class Money {
    private double balance = 0;
    public void Print() 
    {
        Console.WriteLine($"Balance is {balance}");
    }
}

class Program
{
    public void Main(string[] args)
    {
        Money m = new Money();
        m.balance = 10000;
        m.Print();
    }
}