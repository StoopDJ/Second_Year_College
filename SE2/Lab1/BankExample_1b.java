
class Customer {
    private final String name;
    public Customer(final String n) {
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
    
    public BankAccount( final Customer c) {
        accNo = Integer.toString(++nextAccNo);
        customer = c;
        balance = 0;
    }
    
    public void deposit(final int x) throws Exception {
        if (x <= 0) throw new Exception("Amount <= 0\n");
        
        balance = balance + x;
    }	
    
    public abstract void withdraw(int a) throws Exception;
    
    public String toString(){
        final String result = "\nHolder of account number " + accNo + " is " + customer.getName() 
          +  ", balance = " + Integer.toString(balance);
        return result;
    }
    
}

class CurrentAccount extends BankAccount {
    private final int overdraft_limit;
    
    public CurrentAccount(final Customer c, final int limit)  {
        super(c);
        overdraft_limit = limit;        
    }    

    public void withdraw(int a) throws Exception{

        if (a <= 0) throw new Exception("Amount <= 0\n");
        
        balance = balance - a;
        
    }
}

class SavingsAccount extends BankAccount{
    private final float rate;
    
    public SavingsAccount(final Customer c) {
        super(c);
        rate = 0.05f;
    }

    public void withdraw(int a) throws Exception{

        if (a <= 0) throw new Exception("Amount <= 0\n");
        
        balance = balance - a;

    }
}

class BankExample_1b {
    public static void main(final String[] arg) {
        System.out.println("\nBank Program to test class model");
        
        final Customer john = new Customer("John Smith");
        final BankAccount b = new SavingsAccount(john);
        System.out.println(b);
        
        try {
            b.deposit(150);
        } catch( final Exception e) {
            System.out.println("Bank transaction exception: " + e);
        }

        System.out.println(b);  
        
        // the next line will cause an exception to be thrown
        try {
            b.deposit(-200);
        } catch( final Exception e) {
            System.out.println("Bank transaction exception: " + e);
        }
        
        System.out.println(b);  
    }
}