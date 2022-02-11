import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;

import javax.swing.JPanel;

@SuppressWarnings("serial")
public class GamePanel extends JPanel implements ActionListener {

    static final int SCREEN_WIDTH = 594;
    static final int SCREEN_HEIGHT = 594;
    static final int UNIT_SIZE = 66;
    static final int BOARD_WIDTH = 330;
    static final int BOARD_HEIGHT = 330;
    static final int BOARD_X = 132;
    static final int BOARD_Y = 132;
    static final int[] L_ONE_X = { 132, 198, 198, 198, 198, 198, 264, 264, 264, 330, 330, 396 };
    static final int[] L_ONE_Y = { 198, 132, 198, 264, 330, 396, 264, 330, 396, 330, 396, 264 };
    final ArrayList<Integer> yesX = new ArrayList<Integer>();
    final ArrayList<Integer> yesY = new ArrayList<Integer>();
    final ArrayList<Integer> noX = new ArrayList<Integer>();
    final ArrayList<Integer> noY = new ArrayList<Integer>();
    final ArrayList<Integer> markX = new ArrayList<Integer>();
    final ArrayList<Integer> markY = new ArrayList<Integer>();
    int health = 3;
    int currentLevel = 1;
    boolean running = false;

    GamePanel() {
	this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
	this.setBackground(Color.black);
	this.setFocusable(true);
	this.addMouseListener(new MyMouseAdapter());
	startGame();
    }

    public void startGame() {
	running = true;
    }

    public void paintComponent(Graphics g) {
	super.paintComponent(g);
	draw(g);
    }

    public void draw(Graphics g) {
	if (running) {
		g.setColor(Color.darkGray);
		for (int i = 2; i < (SCREEN_HEIGHT / UNIT_SIZE) - 1; i++) {
		    // g.drawLine(x1, y1, x2, y2);
		    g.drawLine(i * UNIT_SIZE, UNIT_SIZE, i * UNIT_SIZE, SCREEN_HEIGHT - (2 * UNIT_SIZE));
		    g.drawLine(UNIT_SIZE, i * UNIT_SIZE, SCREEN_WIDTH - (2 * UNIT_SIZE), i * UNIT_SIZE);
		}
		drawHealth(g);
		g.setColor(Color.white);
		g.drawRect(BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT);
		if (currentLevel == 1) {
		    drawLevelOne(g);
		}
		// Draw the yes, nos, and marks.
		g.setColor(Color.yellow);
		for (int i = 0; i < markX.size(); i++) {
		    g.drawLine(markX.get(i), markY.get(i), markX.get(i) + UNIT_SIZE, markY.get(i) + UNIT_SIZE);
		    g.drawLine(markX.get(i), markY.get(i) + UNIT_SIZE, markX.get(i) + UNIT_SIZE, markY.get(i));
		}
		g.setColor(Color.white);
		for (int j = 0; j < yesX.size(); j++) {
		    g.fillRect(yesX.get(j), yesY.get(j), UNIT_SIZE, UNIT_SIZE);
		}
		g.setColor(Color.red);
		for (int k = 0; k < noX.size(); k++) {
		    g.drawLine(noX.get(k), noY.get(k), noX.get(k) + UNIT_SIZE, noY.get(k) + UNIT_SIZE);
		    g.drawLine(noX.get(k), noY.get(k) + UNIT_SIZE, noX.get(k) + UNIT_SIZE, noY.get(k));
		}
	} else {
	    if (health == 0) {
		currentLevel = -1;
		gameOver(g);
	    } else {
		currentLevel = -2;
		complete(g);
	    }
	}
    }

    public void drawHealth(Graphics g) {
	if(health == 0 ) {
	    g.setColor(Color.white);
	    g.drawOval(3*UNIT_SIZE, 7*UNIT_SIZE, UNIT_SIZE, UNIT_SIZE);
	} else {
	    g.setColor(Color.red);
	    g.fillOval(3 * UNIT_SIZE, 7 * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE);
	}
	if (health <= 1) {
	    g.setColor(Color.white);
	    g.drawOval(4 * UNIT_SIZE, 7 * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE);
	} else {
	    g.setColor(Color.red);
	    g.fillOval(4 * UNIT_SIZE, 7 * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE);
	}
	if (health <= 2) {
	    g.setColor(Color.white);
	    g.drawOval(5 * UNIT_SIZE, 7 * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE);
	} else {
	    g.setColor(Color.red);
	    g.fillOval(5 * UNIT_SIZE, 7 * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE);
	}
	
    }

    public void drawLevelOne(Graphics g) {
	g.setColor(Color.white);
	g.setFont(new Font("Ink Free", Font.BOLD, 25));
	FontMetrics metrics1 = getFontMetrics(g.getFont());
	g.drawString("1", (2 * UNIT_SIZE) + ((int) ((UNIT_SIZE - metrics1.stringWidth("1")) / 2)), (2 * UNIT_SIZE) - 8);
	g.drawString("5", (3 * UNIT_SIZE) + ((int) ((UNIT_SIZE - metrics1.stringWidth("5")) / 2)), (2 * UNIT_SIZE) - 8);
	g.drawString("3", (4 * UNIT_SIZE) + ((int) ((UNIT_SIZE - metrics1.stringWidth("3")) / 2)), (2 * UNIT_SIZE) - 8);
	g.drawString("2", (5 * UNIT_SIZE) + ((int) ((UNIT_SIZE - metrics1.stringWidth("2")) / 2)), (2 * UNIT_SIZE) - 8);
	g.drawString("1", (6 * UNIT_SIZE) + ((int) ((UNIT_SIZE - metrics1.stringWidth("1")) / 2)), (2 * UNIT_SIZE) - 8);

	g.drawString("1", ((2 * UNIT_SIZE) - (8 + metrics1.stringWidth("1"))),
		(2 * UNIT_SIZE) + ((int) ((UNIT_SIZE + 25) / 2)));
	g.drawString("2", ((2 * UNIT_SIZE) - (8 + metrics1.stringWidth("2"))),
		(3 * UNIT_SIZE) + ((int) ((UNIT_SIZE + 25) / 2)));
	g.drawString("2", ((2 * UNIT_SIZE) - (16 + metrics1.stringWidth("2") + metrics1.stringWidth("1"))),
		(4 * UNIT_SIZE) + ((int) ((UNIT_SIZE + 25) / 2)));
	g.drawString("1", ((2 * UNIT_SIZE) - (8 + metrics1.stringWidth("1"))),
		(4 * UNIT_SIZE) + ((int) ((UNIT_SIZE + 25) / 2)));
	g.drawString("3", ((2 * UNIT_SIZE) - (8 + metrics1.stringWidth("3"))),
		(5 * UNIT_SIZE) + ((int) ((UNIT_SIZE + 25) / 2)));
	g.drawString("3", ((2 * UNIT_SIZE) - (8 + metrics1.stringWidth("3"))),
		(6 * UNIT_SIZE) + ((int) ((UNIT_SIZE + 25) / 2)));
    }

    public void checkCorrect(int x, int y) {
	boolean correct = false;
	for (int i = 0; i < L_ONE_X.length; i++) {
	    if (x == L_ONE_X[i] && y == L_ONE_Y[i]) {
		correct = true;
		break;
	    }
	}
	if (correct) {
	    yesX.add(x);
	    yesY.add(y);
	    if (yesX.size() == L_ONE_X.length) {
		running = false;
	    }
	} else {
	    noX.add(x);
	    noY.add(y);
	    health -= 1;
	    if (health == 0) {
		running = false;
	    }
	}
    }

    public void mark(int x, int y) {
	boolean added = false;
	int index = 0;
	for (int i = 0; i < markX.size(); i++) {
	    if (x == markX.get(i) && y == markY.get(i)) {
		added = true;
		index = i;
		break;
	    }
	}
	if (!added) {
	    markX.add(x);
	    markY.add(y);
	} else {
	    markX.remove(index);
	    markY.remove(index);
	}
    }


    public void gameOver(Graphics g) {
	g.setColor(Color.red);
	g.setFont(new Font("Ink Free", Font.BOLD, 75));
	FontMetrics metrics1 = getFontMetrics(g.getFont());
	g.drawString("Game Over", (SCREEN_WIDTH - metrics1.stringWidth("Game Over")) / 2, SCREEN_HEIGHT / 2);

	g.fillRect((SCREEN_WIDTH / 2) - ((3 * UNIT_SIZE) / 2), 6 * UNIT_SIZE, 3 * UNIT_SIZE, UNIT_SIZE);
	g.setColor(Color.black);
	g.setFont(new Font("Ink Free", Font.BOLD, 30));
	FontMetrics metrics2 = getFontMetrics(g.getFont());
	g.drawString("Retry?", (SCREEN_WIDTH - metrics2.stringWidth("Retry?")) / 2, ((int) ((13 * UNIT_SIZE) / 2)) + 5);
    }

    public void complete(Graphics g) {
	g.setColor(Color.white);
	g.setFont(new Font("Ink Free", Font.BOLD, 75));
	FontMetrics metrics = getFontMetrics(g.getFont());
	g.drawString("Congrats!", (SCREEN_WIDTH - metrics.stringWidth("Congrats!")) / 2, SCREEN_HEIGHT / 2);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
	repaint();

    }

    public class MyMouseAdapter extends MouseAdapter {
	public void mouseClicked(MouseEvent e) {
	    // Get the mouse's X and Y coordinates
	    int mouseX = e.getX();
	    int mouseY = e.getY();
	    int gridX = ((int) (mouseX / UNIT_SIZE)) * UNIT_SIZE;
	    int gridY = ((int) (mouseY / UNIT_SIZE)) * UNIT_SIZE;
	    int button = e.getButton();
	    // System.out.println("Mouse: " + mouseX + " " + mouseY + ". Grid: " + gridX + "
	    // " + gridY);
	    if (currentLevel == 1) {
        	    boolean empty = true;
        	    // Check to make sure there's no yes or nos in that spot
        	    for (int i = 0; i < yesX.size(); i++) {
        		if (gridX == yesX.get(i) && gridY == yesY.get(i)) {
        		    empty = false;
        		    break;
        		}
        	    }
        	    for (int j = 0; j < noX.size(); j++) {
        		if (gridX == noX.get(j) && gridY == noY.get(j)) {
        		    empty = false;
        		    break;
        		}
        	    }
        	    if (gridX < BOARD_X || gridX > (BOARD_X + BOARD_WIDTH - 1) || gridY < BOARD_Y
        		    || gridY > (BOARD_Y + BOARD_HEIGHT - 1)) {
        		empty = false;
        	    }
        	    // If the spot is open...
        	    if (empty) {
        		// If left click, check if correct
        		if (button == MouseEvent.BUTTON1) {
        		    // System.out.println("Left click.");
        		    checkCorrect(gridX, gridY);
        		}
        		// If right click, create a marker
        		else if (button == MouseEvent.BUTTON3) {
        		    // System.out.println("Right click");
        		    mark(gridX, gridY);
        		}
        	    }
	    } else if (currentLevel == -1) {
		if (button == MouseEvent.BUTTON1) {
		    if (gridX >= 3 * UNIT_SIZE && gridX <= 5 * UNIT_SIZE && gridY == 6 * UNIT_SIZE) {
			running = true;
			currentLevel = 1;
			yesX.clear();
			yesY.clear();
			noX.clear();
			noY.clear();
			markX.clear();
			markY.clear();
			health = 3;
		    }
		}
	    }
	    repaint();
	}
    }

}
