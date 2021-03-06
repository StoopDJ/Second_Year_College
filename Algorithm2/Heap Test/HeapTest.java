// heapTest.java
// Simple array based implementation of a Heap;
import java.util.*;

class Heap
{
    private int[] a;
	private int[] hPos;
    private int N;
	private int v;

    private static int hmax = 100;
    
    public Heap()
    {
        a = new int[hmax + 1];
		hPos = new int[hmax + 1];
        N = 0;
    }

    public Heap(int _hmax)
    {
        a = new int[_hmax + 1];
        N = 0;
    }

    public void insert(int x)
    {
		//v = a[k];
        a[++N] = x;
	    hPos[v] = k;  
        siftUp(N);
    }
  
    public void siftUp(int k)
    {
        v = a[k];
		a[0] = Integer.MAX_VALUE;
		while (v > a[(k/2)])
		{
			a[k] = a[(k / 2)];
			hPos[a[k]] = k;
			k = (k / 2);
		}
		
		a[k] = v;
		hPos[v] = k;
    }

    public void display() 
    {
        System.out.println("{0}" + a[1]);

        for(int i = 1; i <= N/2; i = i * 2) {
            for(int j = 2*i; j < 4*i && j <= N; ++j)
                System.out.println("{0} " + a[j]);
            System.out.println("\n");
        }
    }
}

class heapTest
{
    public static void main(String[] args)
    {
        Heap h = new Heap();

        Random r = new Random();

        int i, x;
        for (i = 0; i < 10; ++i)
        {
            x = r.nextInt(99);
            System.out.println("\nInserting {0} " + x);
            h.insert(x);
            h.display();
        }

        //x = h.remove();
        //System.out.println("\nRemoving {0} ", x);
       // h.display();
    }
}
