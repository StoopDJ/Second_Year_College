package ie.tudublin;

import processing.core.PApplet;

public class Loops extends PApplet
{	
	public void settings()
	{
		size(500, 500);
	}

	public void setup() 
	{
		colorMode(HSB);
		
	}

	
	public void keyPressed()
	{
		if (key == ' ')
		{
			
		}
	}	


	public void draw()
	{	
		noStroke();
			colorMode(HSB, 500);
			for (int i = 0; i < 500; i++) {
			  for (int j = 0; j < 500; j++) {
				stroke(i, j, 500);
				point(i, j);
			  }
			}
		
	
	}
}
