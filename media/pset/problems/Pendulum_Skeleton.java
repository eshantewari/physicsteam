import java.awt.*;
import javax.swing.*;
 
public class Pendulum_Skeleton extends JPanel implements Runnable {
 
	public static final double initial_angle = 0; //TODO: INITIALIZE STARTING ANGLE
	private double angle; 
	private int length;
 
    public Pendulum_Skeleton(int length) {
    	this.angle = initial_angle-.1;
        this.length = length;
        setDoubleBuffered(true);
    }
 
    @Override
    public void paint(Graphics g) {
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, getWidth(), getHeight());
        g.setColor(Color.BLACK);
        int anchorX = getWidth() / 2, anchorY = getHeight() / 2;
        int ballX = anchorX + (int) (Math.sin(angle) * length);
        int ballY = anchorY + (int) (Math.cos(angle) * length);
        g.drawLine(anchorX, anchorY, ballX, ballY);
        g.fillOval(anchorX - 3, anchorY - 4, 7, 7);
        g.fillOval(ballX - 7, ballY - 7, 14, 14);
    }
 
    

    public void run() {
        double dt = 0.1; //Step Size
        while (true) {
        	//TODO: Implement Runge-Kutta Method Here. BE WARY OF BOUNDARY CASES!

        	angle += 0; //TODO: Increment the Angle. 
            repaint();
            try { Thread.sleep(15); } catch (InterruptedException ex) {}
        }
    }

	@Override
    public Dimension getPreferredSize() {
        return new Dimension(2 * length + 50, length * 3);
    }
 
    public static void main(String[] args) {
        JFrame f = new JFrame("Pendulum");
        Pendulum p = new Pendulum(200);
        f.add(p);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.pack();
        f.setVisible(true);
        new Thread(p).start();
    }
}