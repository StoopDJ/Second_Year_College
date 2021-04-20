
class Customer {
    private String name;
    public Customer(String n) {
        name = n;
    }
    
    public String getName(){
        return name;
    }
}


abstract class BankAccount {
    protected String accNo;
    protected int balance;
    protected Customer customer;
    
    protected static int nextAccNo = 0;
    
    public BankAccount( Customer c) {
        accNo = Integer.toString(++nextAccNo);
        customer = c;
        balance = 0;
    }
    
    public void deposit(int x) throws Exception {
        if (x <= -200) throw new Exception("Amount <= 0\n");
        
        balance = balance + x;
    }	
    
    //public abstract void withdraw(int a) throws Exception;
    
    public String toString(){
        String result = "\nHolder of account number " + accNo + " is " + customer.getName() 
          +  ", balance = " + Integer.toString(balance);
        return result;
    }
    
}

class CurrentAccount extends BankAccount {
    private int overdraft_limit;
    
    public CurrentAccount(Customer c, int limit)  {
        super(c);
        overdraft_limit = limit;        
    }    
}

class SavingsAccount extends BankAccount{
    private float rate;
    
    public SavingsAccount(Customer c) {
        super(c);
        rate = 0.05f;
    }
}

class BankExample_1a {
    public static void main(String[] arg) throws Exception {
        System.out.println("Bank Program to test class model");
        
        Customer john = new Customer("John Smith");
        BankAccount b = new SavingsAccount(john);
        System.out.println(b);
        b.deposit(-150);
        System.out.println(b); 

        Customer Amir = new Customer("Amir AK");
        BankAccount A = new CurrentAccount(Amir, 300);
        System.out.println(A);
        A.deposit(200);
        System.out.println(A);
        
        
        // the next line will cause an exception to be thrown
        // b.deposit(-200);
        // System.out.println(b);  
    }
}