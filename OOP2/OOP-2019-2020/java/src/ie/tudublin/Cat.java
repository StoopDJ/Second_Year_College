package ie.tudublin;

public class Cat extends Animal
{
    private int numLives;

    public Cat(String name)
    {
        // Constructor chaining to the superclass
        super(name);
        setNumLives(9);        
    }

    // Accessor method for reading the private field
    public int getNumLives() {
        return numLives;
    }

    // Accessor method for writing to the private field
    public void setNumLives(int numLives) {
        this.numLives = numLives;
    }

    // Virtual function
    // Dynamic function binding
    public void speak()
    {
        System.out.println("Meow!");
    }
}